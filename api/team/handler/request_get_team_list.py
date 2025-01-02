from interface.abstract_handler import AbstractHandler


class RequestGetTeamList(AbstractHandler):
    def __init__(self, request_id, args):
        self.request_id = request_id
        self.args = args

    def do_process(self):
        print(f"RequestGetTeamList: request_id={self.request_id}, args={self.args}")
        return "RequestGetTeamList: OK"