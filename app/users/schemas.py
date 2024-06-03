from pydantic import BaseModel, ConfigDict, EmailStr



class SchemaUserAuth(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    
    
    email: EmailStr
    password: str