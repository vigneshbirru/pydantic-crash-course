from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Annotated


class Address(BaseModel):
    city: str
    state: str
    pin: str
    
class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address
    
address_dict = {'city': 'New York', 'state': 'NY', 'pin': '10001'}

address1 = Address(**address_dict)

patient_info = {'name': 'vighnesh', 'gender': 'male', 'age': 30, 'address': address1}

patient1 = Patient(**patient_info)
print("Patient :", patient1)
temp = patient1.model_dump_json()  # This will return a dictionary representation of the patient1 object

print(temp)
print(type(temp))
