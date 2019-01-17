import requests
import json

"""
Modify these please
"""
url='http://192.168.10.60/ins'
switchuser='admin'
switchpassword='Passw0rd1'

def vty_nx():
   myheaders={'content-type':'application/json'}
   payload={
     "ins_api": {
     "version": "1.0",
     "type": "cli_conf",
     "chunk": "0",
     "sid": "2",
     "input": "line vty  ;  session-limit 5 ;  exec-timeout 10",
     "output_format": "json"
     }
    }
   response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
if __name__ == "__main__":
    vty_nx()
    print "VTY created"