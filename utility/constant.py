class Constant:
    service_port = 5015
    service = "team-management-service"


    base_url = "http://localhost:"
    dao_port = "5010"

    dao = {
        "create": "/api/create",
        "read": "/api/read",
        "list": "/api/read_list",
        "update": "/api/update",
        "delete": "/api/delete"
    }

    table = {
        "TEAM": "team",
    }

    delimeter = {
        "TEAM": "__",

    }


    files = {
        "metadata": "-metadata.json"
    }


