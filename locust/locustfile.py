import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        pass

    @task
    def services(self):
        self.client.get("/services/api/v1/services/")

    @task
    def home(self):
        self.client.get("/")

    @task
    def contact(self):
        self.client.get("/contact")
