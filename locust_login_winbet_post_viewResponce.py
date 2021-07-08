#http://newtours.demoaut.com/login.php

'''action:process
username:qamile1@gmail.com
password:qamile
login.x:16
login.y:9'''

from locust import HttpUser,task,TaskSet
class Behaviour(TaskSet):
    @task
    def login(self):
        resp=self.client.post("https://www.google-analytics.com/g/collect?v=2&tid=G-DR45FWMDQJ&gtm=2oe6u0&_p=20924399&sr=1366x768&ul=hy-am&cid=917347990.1619003753&_s=2&dl=https%3A%2F%2Fbet.priotix.xyz%2Fesports%2Fhome%2Fmatches%3Faction%3DsignIn&dr=https%3A%2F%2Fbet.priotix.xyz%2Fesports%2Fhome%2Fmatches&dt=All%20Upcoming%20Esports%20Matches&sid=1625648810&sct=109&seg=1&en=page_view&_et=21805")
        # print(resp.status_code)
        # print(resp.headers)
        # print(resp.request.headers)
        # print(resp.text)

#to get a log file type in terminal:
#locust -f locust_login_winbet_post_viewResponce.py --logfile=locust.log

class User(HttpUser):
    tasks = [Behaviour]
    min_wait = 2000
    max_wait = 5000
    host = "https://bet.priotix.xyz/esports/home/matches?action=signIn"