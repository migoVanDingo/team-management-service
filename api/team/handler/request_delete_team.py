from interface.abstract_handler import AbstractHandler


class RequestDeleteTeam(AbstractHandler):
    def __init__(self, request_id, id):
        self.request_id = request_id
        self.id = id

    def do_process(self):
        print(f"RequestDeleteTeam: request_id={self.request_id}, id={self.id}")
        return "RequestDeleteTeam: OK"