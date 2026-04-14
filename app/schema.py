from pydantic import BaseModel, Field

class InsuranceInput(BaseModel):
    age: int = Field(..., ge=1, le=100)
    sex: str
    bmi: float = Field(..., ge=10, le=60)
    children: int = Field(..., ge=0, le=10)
    smoker: str
    region: str