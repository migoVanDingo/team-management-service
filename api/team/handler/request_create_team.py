import traceback
from flask import current_app
from api.team.payload.payload_team import PayloadTeam
from interface.abstract_handler import AbstractHandler
from utility.constant import Constant
from utility.error import ThrowError
from utility.request import Request


class RequestCreateTeam(AbstractHandler):
    def __init__(self, request_id, payload):
        self.request_id = request_id
        self.payload = payload

    def do_process(self):
        try:
            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} ---  Payload: {self.payload}")

            dao_request = Request()
            insert_team_response = dao_request.insert(self.request_id, Constant.table["TEAM"], PayloadTeam.form_team_payload(self.payload))

    

            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- {insert_team_response}")


            return insert_team_response['response']

        except Exception as e:
            current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- {traceback.format_exc()} --- {str(e)}")
            raise ThrowError(f"There was a problem in create the team: {str(e)}", 500)