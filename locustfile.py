from locust import HttpUser, task

class WebsiteUser(HttpUser):

    @task
    def test_home(self):
        self.client.get("/")
