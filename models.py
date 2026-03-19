from pydantic import BaseModel,Field
from typing import Optional



class Employee_leave_request_pydantic(BaseModel):
    name:str         =Field(...,min_length=1)
    department:str   =Field(...,min_length=1)
    reason:str       =Field(...,min_length=1)
    total_leaves:int 
    model_config = {"from_attributes": True}

class Employee_leave_respone_pydantic(BaseModel):
    id:int
    name:str
    department:str
    reason:str
    status: Optional[str] = None
    total_leaves:int
    model_config = {"from_attributes": True}
