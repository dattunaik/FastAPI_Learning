from pydantic import BaseModel, Field, StrictInt

class InputSchema(BaseModel):
    # longitude	latitude	housing_median_age	total_rooms	total_bedrooms	population	households	
    # median_income	median_house_value	ocean_proximity
    longitude : float
    latitude : float
    housing_median_age : int = Field(..., gt=0)
    total_rooms : StrictInt = Field(..., gt=0)
    total_bedrooms : StrictInt = Field(...,gt=0)
    population : int = Field(..., gt=0)
    households : StrictInt = Field(..., gt=0)
    median_income : float = Field(..., gt=0)

class OutputSchema(BaseModel):
    predicted_price : float 