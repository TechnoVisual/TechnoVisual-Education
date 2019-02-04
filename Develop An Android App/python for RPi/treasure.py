import pyrebase
import time
from gpiozero import LED

config = {
    "apiKey": "Your apiKey goes here",
    "authDomain": "Your hosting domain goes here",
    "databaseURL": "Your hosting URL goes here",
    "projectId": "Your project id",
    "storageBucket": "Your storage domain",
    "messagingSenderId": "Your sender id"
}

firebase = pyrebase.initialize_app(config)
numberOfTreasure = 3
led = {}
teams = {}
teams[0] = {"email":"test1@rpitest.com","led":17,"treasure":[]}
teams[1] = {"email":"test2@rpitest.com","led":18,"treasure":[]}
teams[2] = {"email":"test3@rpitest.com","led":22,"treasure":[]}
teams[3] = {"email":"test4@rpitest.com","led":23,"treasure":[]}

for f in range(len(teams)):
    led[f] = LED(teams[f]["led"])
    led[f].off()

db = firebase.database()

def processMessage(d):
    if(d != None):
        for v in d.values():
            updateTeam(v["email"], v["item"])
    
def ledFlash(t):
    for f in range(5):
        led[t].on()
        time.sleep(.2)
        led[t].off()
        time.sleep(.2)

def ledOn(t):
    led[t].on()
    
def updateTeam(t,i):
    for td in teams:
        if teams[td]["email"] == t:
            if i not in teams[td]["treasure"]:
                teams[td]["treasure"].append(i)
                if len(teams[td]["treasure"]) >= numberOfTreasure:
                    print(t+" complete!")
                    ledOn(td)
                else:
                    ledFlash(td)

def streamHandler(message):
    if message["event"] == "put" or message["event"] == "patch":
        processMessage(message["data"])

myStream = db.child("msg").stream(streamHandler)

while 1:
    time.sleep(.1)
    
