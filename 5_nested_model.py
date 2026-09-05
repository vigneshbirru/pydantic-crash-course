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


print("Patient Name:", patient1.address.city)