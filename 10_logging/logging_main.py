from fastapi import FastAPI, Request
from pydantic import BaseModel
import logging
from datetime import datetime

# Logging Configuration
LOG_FILE = "test.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),  # Write logs to a file
        logging.StreamHandler()         # Also show logs in console
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI(title="Loan Eligibility API")

def is_eligible_for_loan(income: int, age: int, employment_status: str) -> bool:
    eligibility = (income > 50000) and (age > 18) and (employment_status.lower() == 'employed')
    logger.info(f"Eligibility Check -> Income: {income}, Age: {age}, Status: {employment_status}, Result: {eligibility}")
    return eligibility

class Applicant(BaseModel):
    income: float
    age: int
    employment_status: str


@app.post('/loan_eligibility')
async def check_eligibility(applicant: Applicant, request: Request):
    client_host = request.client.host
    logger.info(f"Incoming Request from {client_host} | Data: {applicant.dict()}")
    
    eligibility = is_eligible_for_loan(
        income=applicant.income,
        age=applicant.age,
        employment_status=applicant.employment_status
    )

    response = {'eligible': eligibility, 'timestamp': datetime.utcnow().isoformat()}
    logger.info(f"Response -> {response}")
    logger.info(" ========================== END ========================== ")

    return response
