from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class User(BaseModel):
    name: str = "kamal" # kamal is default value
    age: Optional[int] = None # if value is not exist so should be default None exist
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=6)
    
new_user = {'age': '25', 'email': 'kamal@gmail.com'} # is type coercing if value in str

user = User(**new_user)
# print(user)
user_dict = dict(user)
print(user_dict)
user_json = user.model_dump_json()
print(user_json)