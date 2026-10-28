from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    # gender: str = 'Male' -- default value 
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish','gender':'male' ,'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude={'address':['state']})
print(temp)
print(type(temp))


# temp = patient1.model_dump(exclude_unset=True) can be used if a default value is set to a field but is not used in object creation, so it will exclude that default value field from the output.

# temp1 = patient1.model_dump_json()
# print(temp1)
# print(type(temp1))