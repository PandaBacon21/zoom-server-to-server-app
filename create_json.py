import json 
from datetime import datetime

data = {
    'access_token': '1234',
    'expire': datetime(2023, 12, 20, 13, 33, 1).strftime('%Y-%m-%d %H:%M:%S')
}

with open('token.json', 'w') as f:
    json.dump(data, f, indent=4)


