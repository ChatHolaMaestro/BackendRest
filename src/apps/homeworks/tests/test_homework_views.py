from rest_framework import status
from rest_framework.test import APITestCase


class HomeworkViewSetTestCase(APITestCase):
    fixtures = [
        "users.json",
        "subjects.json",
        "schools.json",
        "teachers.json",
        "relatives.json",
        "students.json",
        "requests.json",
        "homeworks.json",
    ]

    def setUp(self):
        self.user = self.client.login(
            email="john@example.com", password="Complexpass123"
        )
        self.homework_count = 3

    def test_list_homeworks_is_200_and_has_homeworks(self):
        response = self.client.get("/api/homeworks/homeworks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.homework_count)

    def test_retrieve_homework_with_pk_1_is_200_and_has_homework(self):
        response = self.client.get("/api/homeworks/homeworks/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_retrieve_homework_with_pk_4_is_404(self):
        response = self.client.get("/api/homeworks/homeworks/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_homework_with_pk_1_is_200(self):
        response = self.client.delete("/api/homeworks/homeworks/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_homework_with_pk_4_is_404(self):
        response = self.client.delete("/api/homeworks/homeworks/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
