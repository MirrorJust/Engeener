import random

import requests

activity_num = random.randint(1, 5)
url = "https://www.boredapi.com/api/activity"
params = {
    'participants': activity_num,
}

r = requests.get(url)
result = r.json()
print(result['activity'])
