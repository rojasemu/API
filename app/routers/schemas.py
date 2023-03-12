from pydantic import Field
from pydantic import BaseModel

class psid(BaseModel):
    psid: str = Field(
        ...,
        min_length=20,
        max_length=20,
     
        )  
    pid: int = Field(
           ...,
        gt=20,
        le=1000000000,       
        )
    
    
    
class ord(BaseModel):
    ord: str = Field(
           ...,
        min_length=10,
        max_length=15,        
        )
