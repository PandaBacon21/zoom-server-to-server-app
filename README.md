# Zoom Server-To-Server App Example

This repo is intended to serve as an example of how to create a server-to-server OAuth app to interact with Zoom's REST API. Click this link for instructions on how to create a [Zoom Server-To-Server App](https://developers.zoom.us/docs/internal-apps/). 

# Installation

Clone this project 

```
git clone https://github.com/PandaBacon21/zoom-server-to-server-app.git
```

Install dependencies

```
pip install -r requirements.txt
```

It is recommended to use a virtual environment to ensure no dependency conflicts. 

# Usage

You will need to create a ```.env``` file in the root of your project directory and include the following environment variable

```
ACCOUNT_ID = 'YourZoomAccountId'
CLIENT_ID = 'YourZoomClientId'
CLIENT_SECRET = 'YourZoomClientSecret'
DB_LOCATION = 'PathToYourDataBase'
```
I just used a SQLite database for this project but you can use any database that you'd prefer.

# Example GET Request

```
def list_users(req_headers):
    # Set the full_url for the API request
    endpoint = '/users'
    full_url = base_url+endpoint

    # Send the request to the full_url and save the response object in a variable named 'response'
    response = requests.get(url=full_url, headers=req_headers)
    
    print(f'endpoint: {endpoint}, status code: {response.status_code}')
    
    r_content = json.loads(response.content)

    # takes the response content and dumps to a new json file called 'users.json'
    with open('users.json', 'w') as outfile: 
        json.dump(r_content, outfile, indent=4)

```

# Example POST Request 

```
def create_meeting(user_id, req_headers):
    # Set the full_url for the API request
    endpoint = f'/users/{user_id}/meetings'
    full_url = base_url+endpoint
    # Pass any data needed for the POST request in the payload
    payload = {
        'agenda': 'Meeting was created',
        'scheduled_for': f'{user_id}',
    }
    # Send the request to the full_url and save the response object in a variable named 'response'
    response = requests.post(url=full_url, headers=req_headers, json=payload)
    r_content = json.loads(response.content)
    # if the request was successful, print details to the console and save the meeting details to a new json file
    if response.status_code == 201:
        print(f'endpoint: {endpoint}, status code: {response.status_code}, Meeting Created!')
        # takes the response and dumps to a new json file called 'meeting_details.json'
        with open('meeting_details.json', 'w') as outfile:
            json.dump(r_content, outfile, indent=4)
    else: 
        print(f'ERROR: Status Code: {response.status_code}')
```



# License

This app is intended to serve as an example and the use of Zoom's API is subject to [Zoom's Terms of Use]()
