from typing import Optional
from pydantic import BaseModel

class IInsertTeam(BaseModel):
    name:str
    description: Optional[str] = ""
    created_by: str

class PayloadTeam:
    @staticmethod
    def form_team_payload(data:dict) -> IInsertTeam:
        return {
            "name":data.get("name"),
            "description":data.get("description"),
            "created_by":data.get("user_id")
        }