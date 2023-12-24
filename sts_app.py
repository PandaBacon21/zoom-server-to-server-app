import os
import json
import requests
from dotenv import load_dotenv

from utils.get_token import token

load_dotenv()

ACCOUNT_ID = os.environ.get('ACCOUNT_ID')

#Check token expiration. If expired, get a new token and save as access_token
access_token = token()
#print(access_token)
base_url = 'https://api.zoom.us/v2'

# GET A LIST OF ALL USERS - CAN THEN PARSE OUT DETAILS FROM THERE
def list_users(access_token):
    endpoint = '/users'
    full_url = base_url+endpoint
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {access_token}'
    }
    response = requests.get(url=full_url, headers=headers)
    print(full_url)
    print(response.status_code)

    r_content = json.loads(response.content)
    with open('users.json', 'w') as outfile: 
        json.dump(r_content, outfile, indent=4)
    return r_content



# Load Test User 
with open('test_user.json', 'r') as openfile:
    target_user = json.load(openfile)

# GET A SPECIFIC USER'S ID
def get_user_id(access_token, target_user):
    user_id = target_user['email'] # Could also parse out the ID from the list_user() response and use that in place of email. Email is also a valid input for user_id. 
    endpoint = f'/users/{user_id}'
    full_url = base_url+endpoint
    headers = {
        'content-type': 'application/json',
        'authorization': f"Bearer {access_token}"
    }
    response = requests.get(url=full_url, headers=headers)
    r_content = json.loads(response.content)
    with open('target.json', 'w') as outfile:
        json.dump(r_content, outfile, indent=4)

    return r_content['id']

# EXAMPLE OF HOW TO CREATE A MEETING ON BEHALF OF A USER

def create_meeting(access_token, user_id):
    endpoint = f'/users/{user_id}/meetings'
    full_url = base_url+endpoint
    headers = {
        'content-type': 'application/json',
        'authorization': f"Bearer {access_token}"
    }
    payload = {
        'agenda': 'Prove the meeting was created',
        'scheduled_for': f'{user_id}',
    }
    response = requests.post(url=full_url, headers=headers, json=payload)
    r_content = json.loads(response.content)
    if response.status_code == 201:
        print(f'Status Code: {response.status_code}. Meeting Created!')
        with open('meeting_details.json', 'w') as outfile:
            json.dump(r_content, outfile, indent=4)
    else: 
        print(f'ERROR: Status Code: {response.status_code}')
    



if __name__ == '__main__': 
    #list_users(access_token)
    #get_user_id(access_token, target_user)
    create_meeting(access_token, get_user_id(access_token, target_user))