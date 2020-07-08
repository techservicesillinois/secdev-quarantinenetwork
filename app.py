from flask import Flask, jsonify
from typing import Any, Dict, List, Tuple
import functools
import os
import requests
import sys


app = Flask(__name__)


BASE_URL: str = os.environ.get(
    'BASE_URL',
    'https://cplab1.techservices.illinois.edu:443/api'
)
CLIENT_ID: str = os.environ['CLIENT_ID']
CLIENT_SECRET: str = os.environ['CLIENT_SECRET']


def handle_exception(func):
    """
    Handles exceptions and logging for any decorated
    function.
    """
    @functools.wraps(func)
    def wrapper(*args, ** kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            sys.stderr.write(f'{func.__name__} threw exception {e}.')
    return wrapper


@app.route('/canary')
def canary() -> Tuple[Any, int]:
    """
    Check any external dependencies (api, database, etc...)
    that the API has. If any dependency is unavailable return an
    error message.
    """
    messages: List[str] = []
    status_code: int = 200
    try:
        # Check Clearpass API dependency
        token: str = get_clearpass_token(CLIENT_ID, CLIENT_SECRET)
        if not token:
            messages.append('No token returned from clearpass API.')
            status_code = 503
    except requests.RequestException:
        message = 'Request error ocurred during canary check'
        messages.append(message)
        status_code = 503

        sys.stderr.write(message)
    except Exception:
        message = 'Error ocurred during canary check.'
        messages.append(message)
        status_code = 503

        sys.stderr.write(message)
    return jsonify({'messages': messages}), status_code


def get_clearpass_token(client_id: str, client_secret: str) -> str:
    """
    Authenticate with the Clearpass API and return a status code,
    token, and error message if applicable.

        Parameters:
            client_id (str): The Clearpass Client ID used to authenticate.
            client_secret (str): The client secret associated with the given
                                 Client ID.

        Returns:
            token_result (dict): Dictionary containing http status code,
                                 token, and error message if applicable.
    """
    url: str = f'{BASE_URL}/oauth'
    data: Dict[str, str] = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    token: str = ''

    response = requests.post(url, json=data)

    if response.status_code == 200:
        token = response.json()['access_token']

    return token


if __name__ == '__main__':
    app.run(host=app.config['host'])
