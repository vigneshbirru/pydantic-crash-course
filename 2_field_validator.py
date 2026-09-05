from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name:str
    email: EmailStr

    age: int  

    weight: float

    married: bool
    allergies: List[str]

    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['gmail.com', 'yahoo.com', 'outlook.com']
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain '{domain_name}' is not allowed. Allowed domains are: {', '.join(valid_domains)}")
        return value
    
    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def age_validator(cls, value):
        if 0<value<100:
            return value
        else:
            raise ValueError("Age must be between 0 and 100")

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
    "age": '19',
    "weight": 70.5,
    "married": True,
    "allergies": ["dust", "pollen"],
    "contact_details": {
        "email": "vighnesh@example.com"
    }
}

patient = Patient(**patient_info)
patient_data(patient)
