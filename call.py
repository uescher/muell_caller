import requests,sys
from datetime import datetime,timedelta

def tell(text):
    print(text)
    import requests
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = {'text': text}
    requests.post("http://kiosk.shack:8080/say/",
            data=json.dumps(data), headers=headers)

# alert 1 day before
alert_offset= timedelta(days=1)
# latest call is at 9AM
last_call= timedelta(hours=9)
ret= requests.get('http://openhab.shack/muellshack/gelber_sack').json()
next_date = datetime.strptime(ret['gelber_sack'],'%Y-%m-%d') + last_call
now = datetime.now() # + timedelta(days=int(sys.argv[1]))

if next_date - alert_offset < now  < next_date:
    tell('es ist gelber sack tag' )
else:
    #tell('es ist kein gelber sack tag')
    pass


