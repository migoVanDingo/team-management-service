from interface.abstract_handler import AbstractHandler


class RequestUpdateTeam(AbstractHandler):
    def __init__(self, request_id, id, payload):
        self.request_id = request_id
        self.id = id
        self.payload = payload

    def do_process(self):
        print(f"RequestUpdateTeam: request_id={self.request_id}, id={self.id}, payload={self.payload}")
        return "RequestUpdateTeam: OK"