from fastapi import FastAPI, Request
from pydantic import BaseModel
from loguru import logger
from datetime import datetime
import os



# Create a "logs" folder if not exists
os.makedirs("logs", exist_ok=True)

# Remove default logger
logger.remove()

# Add custom log handler — writes to both file and console
logger.add(
    "logs/app.log",
    rotation="10 MB",          # create a new log file after 10MB
    retention="7 days",        # keep logs for 7 days
    level="INFO",              # log level
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    enqueue=True               # thread/process safe
)
logger.add(
    sink=lambda msg: print(msg, end=""),  # console output
    level="INFO",
    format="{time:HH:mm:ss} | {level} | {message}"
)
 
app = FastAPI(title="Loan Eligibility API with Loguru")

 
def is_eligible_for_loan(income: int, age: int, employment_status: str) -> bool:
    eligibility = (income > 50000) and (age > 18) and (employment_status.lower() == 'employed')
    logger.info(
        f"Eligibility Check: income={income}, age={age}, "
        f"status={employment_status}, eligible={eligibility}"
    )
    return eligibility

 
class Applicant(BaseModel):
    income: float
    age: int
    employment_status: str

 
@app.post("/loan_eligibility")
async def check_eligibility(applicant: Applicant, request: Request):
    client_host = request.client.host
    logger.info(f"Incoming request from {client_host} | Data={applicant.dict()}")

    eligibility = is_eligible_for_loan(
        income=applicant.income,
        age=applicant.age,
        employment_status=applicant.employment_status
    )

    response = {
        "eligible": eligibility,
        "timestamp": datetime.utcnow().isoformat()
    }

    logger.info(f"Response to {client_host} -> {response}")
    return response
