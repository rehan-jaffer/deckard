import time
from slackclient import SlackClient

token = os.environ['API_KEY'] # obtain API key from environment
sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        print sc.rtm_read()
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"
