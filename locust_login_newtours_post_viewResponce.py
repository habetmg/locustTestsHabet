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
        resp=self.client.post("/login.php",{"action":"process","username":"qamile1@gmail.com","password":"qamile","login.x":"16","login.y":"9"})
        # print(resp.status_code)
        # print(resp.headers)
        # print(resp.request.headers)
        print(resp.text)
#to get a log file type in terminal:
#locust -f locust_login_newtours_post_viewResponce.py --logfile=locust.log

class User(HttpUser):
    tasks=[Behaviour]
    min_wait = 5000
    max_wait = 10000
    host="http://newtours.demoaut.com"