from pydantic import BaseModel


class ResponseCreator():
    @classmethod
    def create_response(cls, 
                     status_code:int = 200, 
                     status:str = "Completed", 
                     object:str|BaseModel|list[BaseModel] = "", 
                     message:str = ""):
        return {"status_code":status_code, "status":status, "object":object, "message":message}