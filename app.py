import json
import requests

from utils.get_token import token

# retrieve the access token
access_token = token()

base_url = 'https://api.zoom.us/v2'
headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {access_token}'
    }


'''EXAMPLE API CALL: GET ALL USERS'''

def list_users(req_headers):
    endpoint = '/users'
    full_url = base_url+endpoint

    response = requests.get(url=full_url, headers=req_headers)

    print(f'endpoint: {endpoint}, status code: {response.status_code}')

    r_content = json.loads(response.content)
    # takes the response and dumps to a new json file called 'users.json'
    with open('users.json', 'w') as outfile: 
        json.dump(r_content, outfile, indent=4)


'''EXAMPLE API CALL: CREATE A MEETING ON BEHALF OF A USER'''

# user_id can either be the user's actual user ID(from Zoom account) or their email address of their Zoom license
def create_meeting(user_id, req_headers):
    endpoint = f'/users/{user_id}/meetings'
    full_url = base_url+endpoint
    payload = {
        'agenda': 'Meeting was created',
        'scheduled_for': f'{user_id}',
    }
    response = requests.post(url=full_url, headers=req_headers, json=payload)
    r_content = json.loads(response.content)
    if response.status_code == 201:
        print(f'endpoint: {endpoint}, status code: {response.status_code}, Meeting Created!')
        # takes the response and dumps to a new json file called 'meeting_details.json'
        with open('meeting_details.json', 'w') as outfile:
            json.dump(r_content, outfile, indent=4)
    else: 
        print(f'ERROR: Status Code: {response.status_code}')
    


if __name__ == '__main__': 
    list_users(headers)