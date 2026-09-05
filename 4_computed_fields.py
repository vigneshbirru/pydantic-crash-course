from pydantic import BaseModel, Field, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: str
    age: int  
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi
    
def update_patient_data(patient: Patient):
    print("name", patient.name)
    print("email", patient.email) 
    print("age", patient.age)
    print("weight", patient.weight)
    print("height", patient.height)
    print("married", patient.married)
    print("allergies", patient.allergies)
    print("contact_details", patient.contact_details)
    print("BMI:", patient.calculate_bmi)
    print("Patient data is updated successfully.")
        

patient_info = {'name': 'vighnesh','email': 'vighnesh@example.com', 'age': 30, 'weight': 70.0, 'height': 1.75, 'married': True, 'allergies': ['peanuts'], 'contact_details': {'phone': '123-456-7890', 'address': '123 Main St'}}
    
patient = Patient(**patient_info)

update_patient_data(patient)

