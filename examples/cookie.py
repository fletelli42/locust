from locust import HttpUser, TaskSet, task, between

class CookieTasks(TaskSet):
    
    @task
    def set_cookie(self):
        response = self.client.get("/set_cookie")
        if response.cookies:
            print(f"Cookies set by the server: {response.cookies}")
    
    @task
    def send_with_cookie(self):
        cookies = {'session_id': 'abc123'}
        response = self.client.get("/read_cookie", cookies=cookies)
        print(f"Server response to cookie: {response.text}")

class WebsiteUser(HttpUser):
    tasks = [CookieTasks]
    wait_time = between(1, 3)
    host = "http://127.0.0.1:8089"