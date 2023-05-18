from locust import HttpUser, task
from src.apps.locust.fakerExamples import *
import json

class LoadingTest(HttpUser):
    
    usersEndpoint = "api/users/users/"
    studentsEndpoint = "api/students/students/"
    relativesEndpoint = "api/students/relatives/"
    schoolsEndpoint = "api/schools/schools/"
    schoolsManagersEndpoint = "api/schools/schools_managers/"
    subjectsEndpoint = "api/subjects/subjects/"
    teachersEndpoint = "api/teachers/teachers/"
    schedulesEndpoint = "api/teachers/schedules/"
    requestsEndpoint = "api/requests/requests/"
    homeworksEndpoint = "api/homeworks/homeworks/"
    
    ## Users
    @task
    def get_users(self):
        self.client.get(self.usersEndpoint)
    
    @task 
    def post_users(self):
        self.user = createRandomUser()
        if self.user is not None:
            self.client.post(self.usersEndpoint, json=self.user, headers={"Content-Type": "application/json"})
    
    ## Students
    @task
    def get_students(self):
        self.client.get(self.studentsEndpoint)
        
    @task
    def post_students(self):
        self.student = createRandomStudent()
        if self.student is not None:
            self.client.post(self.studentsEndpoint, json=self.student, headers={"Content-Type": "application/json"})
    
    ## Relatives
    @task
    def get_relatives(self):
        self.client.get(self.relativesEndpoint)
    
    @task
    def post_relatives(self):
        self.relative = createRandomRelative()
        if self.relative is not None:
            self.client.post(self.relativesEndpoint, json=self.relative, headers={"Content-Type": "application/json"})
    
    ## Schools
    @task
    def get_schools(self):
        self.client.get(self.schoolsEndpoint)
    
    @task
    def post_schools(self):
        self.school = createRandomSchool()
        if self.school is not None:
            self.client.post(self.schoolsEndpoint, json=self.school, headers={"Content-Type": "application/json"})
    
    ##Subjects
    @task
    def get_subjects(self):
        self.client.get(self.subjectsEndpoint)
    
    ##Teachers
    @task
    def get_teachers(self):
        self.client.get(self.teachersEndpoint)
        
    ##Schedules
    @task
    def get_schedules(self):
        self.client.get(self.schedulesEndpoint)
    
    @task
    def post_schedules(self):
        self.schedule = createRandomSchedule()
        if self.schedule is not None:
            self.client.post(self.schedulesEndpoint, json=self.schedule, headers={"Content-Type": "application/json"})
    
    ## Requests
    @task
    def get_requests(self):
        self.client.get(self.requestsEndpoint)
    
    @task
    def post_requests(self):
        self.request = createRandomRequest()
        if self.request is not None:
            self.client.post(self.requestsEndpoint, json=self.request, headers={"Content-Type": "application/json"})
   
   ## Homeworks
    @task
    def get_homeworks(self):
        self.client.get(self.homeworksEndpoint)
    