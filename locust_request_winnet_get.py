from locust import TaskSet,task, HttpUser


class UserBehaviour(TaskSet):
    @task
    def launch_url(self):
        self.client.get("/bookmaker-comparison")

class User(HttpUser):
    tasks=[UserBehaviour]
    min_wait=2000
    max_wait=4000
    host="https://winners.net"