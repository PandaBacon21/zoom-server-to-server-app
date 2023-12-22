import os
import base64
import requests
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_ID = os.environ.get('ACCOUNT_ID')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

BASE_URL = 'https://api.zoom.us/v2/'
AUTH_URL = 'https://zoom.us/oauth/token'

message = f'{CLIENT_ID}:{CLIENT_SECRET}'
encoded = base64.b64encode(message.encode()).decode()

def get_token():
    new_access_token = {}
    headers = {
        'content-type': 'application/json',
        'authorization': f'Basic {encoded}'
    }
    FINAL_URL = f'{AUTH_URL}?grant_type=account_credentials&account_id={ACCOUNT_ID}'
    response = requests.post(url=FINAL_URL, headers=headers)

    r_content = json.loads(response.content)
    token_exp = datetime.now() + timedelta(seconds=r_content['expires_in'])

    access_token = r_content['access_token']
    #Update this to log rather than print once logging has been added

    #print(f'Current DateTime: {datetime.now()}')
    #print(f'Expires DateTime: {token_exp}')

    new_access_token['access_token'] = access_token
    new_access_token['expire'] = token_exp.strftime('%Y-%m-%d %H:%M:%S')
    with open('token.json', 'w') as outfile: 
        json.dump(new_access_token, outfile, indent=4)
    return new_access_token

def check_token_valid(access_token):
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if access_token['access_token'] == '':
        #change this to log rather than print once logging has been added
        print('No Saved Token. Retrieving Token')
        return get_token()

    elif (access_token['expire'] < current_datetime):
        #change this to log rather than print once logging has been added
        print('Token Is Expired. Retrieving New Token')
        return get_token()
    else:
        #change this to log rather than print once logging has been added
        print('Access Token Is Valid')
        return access_token
            
def token(access_token):
    valid_token = check_token_valid(access_token)
    #change this to log rather than print once logging has been added
    #print(f'This Is The Valid Access Token: {valid_token}')
    return valid_token['access_token']


#token(current_token)
