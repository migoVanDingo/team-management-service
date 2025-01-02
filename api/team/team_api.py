from flask import Blueprint, g, json, request

from api.team.handler.request_create_team import RequestCreateTeam
from api.team.handler.request_delete_team import RequestDeleteTeam
from api.team.handler.request_get_team import RequestGetTeam
from api.team.handler.request_get_team_list import RequestGetTeamList
from api.team.handler.request_update_team import RequestUpdateTeam


team_api = Blueprint('team_api', __name__)

# Create team
@team_api.route('/team', methods=['POST'])
def create_team():
    data = json.loads(request.data)
    request_id = g.request_id
    api_request = RequestCreateTeam(request_id, data)
    response = api_request.do_process()
    return response

# Read team
@team_api.route('/team', methods=['GET'])
def get_team():
    args = request.args
    request_id = g.request_id
    api_request = RequestGetTeam(request_id, args)
    response = api_request.do_process()
    return response


# Get team list
@team_api.route('/team/list', methods=['GET'])
def get_team_list():
    args = request.args
    request_id = g.request_id
    api_request = RequestGetTeamList(request_id, args)
    response = api_request.do_process()
    return response

# Update team
@team_api.route('/team', methods=['PUT'])
def update_team():
    data = json.loads(request.data)
    request_id = g.request_id
    api_request = RequestUpdateTeam(request_id, data)
    response = api_request.do_process()
    return response


# Delete team
@team_api.route('/team/<string:id>', methods=['DELETE'])
def delete_team(id):
    request_id = g.request_id
    api_request = RequestDeleteTeam(request_id, id)
    response = api_request.do_process()
    return response



