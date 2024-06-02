from functools import wraps
from flask import request, Response

VALID_API_KEYS = [
    "TEST_API_KEY"
]

def authenticate():
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Valid API Key Required"'})

def check_auth(api_key):
    if api_key in VALID_API_KEYS:
        return True
    return False

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        auth_str = auth.__str__()
        api_key = auth_str.split(" ")[1]
        if not auth and not check_auth(api_key):
            return authenticate()
        return f(*args, **kwargs)
    return decorated