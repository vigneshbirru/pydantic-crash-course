from pydantic import BaseModel, Field, EmailStr, AnyUrl, model_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name:str
    email: EmailStr
    age: int  
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency(cls, model):
        if model.age> 60 and "emergency_contact" not in model.contact_details:
            raise ValueError("Patients over 60 must have an  emergency  contact.")

def update_patient_data(patient: Patient):
    print("name", patient.name)
    print("email", patient.email) 
    print("age", patient.age)
    print("weight", patient.weight)
    print("married", patient.married)
    print("allergies", patient.allergies)
    print("contact_details", patient.contact_details)
    print("Patient data is updated successfully.")


def patient_data(patient: Patient):
    print("name", patient.name)
    print("email", patient.email) 
    print("age", patient.age)
    print("weight", patient.weight)
    print("married", patient.married)
    print("allergies", patient.allergies)
    print("contact_details", patient.contact_details)
    print("Patient data is valid and processed successfully.")


patient_info = {
    "name": "vighnesh",
    "email": "adb@gmail.com",
    "Linkedin_url": "https://www.linkedin.com/in/vighnesh",
    "age": '88',
    "weight": 70.5,
    "married": True,
    "allergies": ["dust", "pollen"],
    "contact_details": {
        "email": "vighnesh@example.com",
        "emergency_contact":"5555554829"
    }
}

patient = Patient(**patient_info)
patient_data(patient)
