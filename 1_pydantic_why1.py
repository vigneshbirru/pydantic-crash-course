from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[str, Field(
        min_length=1,
        max_length=50,
        title="Patient Name",
        description="Patient name should not exceed 50 characters",
        examples=["John Doe", "Jane Smith"]
    )]

    email: EmailStr

    Linkedin_url: AnyUrl

    age: int = Field(gt=18, lt=60)

    weight: Annotated[float, Field(gt=0, strict=True)]

    allergies: Annotated[
        Optional[List[str]],
        Field(
            min_length=1,
            max_length=5,
            description="List of allergies, must contain between 1 and 5 items"
        )
    ]

    contact_details: Optional[Dict[str, str]] = None
    


def patient_data(patient: Patient):
    print("name", patient.name)
    print("email", patient.email)
    print("Linkedin_url", patient.Linkedin_url)
    print("age", patient.age)
    print("weight", patient.weight)
    print("allergies", patient.allergies)
    print("contact_details", patient.contact_details)
    print("Patient data is valid and processed successfully.")


patient_info = {
    "name": "vighnesh",
    "email": "adb@gmail.com",
    "Linkedin_url": "https://www.linkedin.com/in/vighnesh",
    "age": 19,
    "weight": 70.5,
    "allergies": ["dust", "pollen"],
    "contact_details": {
        "email": "vighnesh@example.com"
    }
}

patient = Patient(**patient_info)
patient_data(patient)
