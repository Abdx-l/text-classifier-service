from locust import HttpUser,task,between
class User(HttpUser):
 wait_time=between(.1,1)
 @task
 def classify(self):self.client.post("/predict",json={"text":"The space shuttle launched into orbit."})
