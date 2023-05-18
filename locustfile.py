from locust import HttpUser, task
from src.apps.locust.fakerExamples import *
import json

class LoadingTest(HttpUser):
    
    ## Users
    usersEndpoint = "api/users/users/"
       
    @task
    def get_users(self):
        self.client.get(self.usersEndpoint)
    
    @task 
    def post_users(self):
        self.user = createRandomUser()
        if self.user is not None:
            self.client.post(self.usersEndpoint, json=self.user, headers={"Content-Type": "application/json"})
        
   