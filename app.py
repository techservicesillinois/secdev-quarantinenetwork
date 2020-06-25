from flask import Flask, jsonify
import requests
import os


app = Flask(__name__)

BASE_URL = os.environ.get('BASE_URL',
                          'https://cplab1.techservices.illinois.edu:443/api')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')


@app.route('/canary')
def canary():
    """
    Check any external dependencies (api, database, etc...)
    that the API has. If any dependency is unavailable return an
    error message.
    """
    canary_result = 'Ok'
    status_code = 200

    # Check Clearpass API dependency
    token_response = get_clearpass_token(CLIENT_ID, CLIENT_SECRET)

    if not token_response['token'] or token_response['status_code'] != 200:
        canary_result = {
            'Error': 'An error occured while checking dependencies.'
        }
        status_code = 503
        # TODO: Log more details for troubleshooting.

    return jsonify(canary_result), status_code


def get_clearpass_token(client_id, client_secret):
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
    url = f'{BASE_URL}/oauth'
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    token_result = {
        'status_code': 0,
        'token': '',
        'error_message': ''
    }

    try:
        response = requests.post(url, json=data)
        token_result['status_code'] = response.status_code

        if response.status_code == 200:
            token_result['token'] = response.json()['access_token']
    except Exception:
        # TODO: Log details
        token_result['status_code'] = 500

    return token_result


if __name__ == '__main__':
    app.run(host=app.config['host'])
