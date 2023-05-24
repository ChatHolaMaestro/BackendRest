from rest_framework import status
from rest_framework.test import APITestCase


class RequestViewSetTestCase(APITestCase):
    fixtures = [
        "users.json",
        "subjects.json",
        "schools.json",
        "teachers.json",
        "relatives.json",
        "students.json",
        "requests.json",
    ]

    def setUp(self):
        self.user = self.client.login(
            email="john@example.com", password="Complexpass123"
        )
        self.request_count = 3

    def test_list_requests_is_200_and_has_requests(self):
        response = self.client.get("/api/requests/requests/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.request_count)

    def test_retrieve_request_with_pk_1_is_200_and_has_request(self):
        response = self.client.get("/api/requests/requests/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_retrieve_request_with_pk_4_is_404(self):
        response = self.client.get("/api/requests/requests/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_request_with_valid_data_is_201_and_has_request(self):
        response = self.client.post(
            "/api/requests/requests/",
            {
                "status": "PENDIENTE",
                "request_type": "TAREAS",
                "student": 1,
                "subject": 2,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["status"], "PENDIENTE")
        self.assertEqual(response.data["request_type"], "TAREAS")
        self.assertEqual(response.data["student"]["id"], 1)
        self.assertEqual(response.data["subject"]["id"], 2)

    def test_create_request_without_student_is_400(self):
        response = self.client.post(
            "/api/requests/requests/",
            {
                "status": "PENDIENTE",
                "request_type": "TAREAS",
                "subject": 2,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_request_without_subject_is_400(self):
        response = self.client.post(
            "/api/requests/requests/",
            {
                "status": "PENDIENTE",
                "request_type": "TAREAS",
                "student": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_request_with_invalid_status_is_400(self):
        response = self.client.post(
            "/api/requests/requests/",
            {
                "status": "INVALID",
                "request_type": "TAREAS",
                "student": 1,
                "subject": 2,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_request_with_pk_1_and_valid_data_is_200_and_has_updated_request(
        self,
    ):
        response = self.client.put(
            "/api/requests/requests/1/",
            {"status": "COMPLETADO"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "COMPLETADO")

    def test_update_request_with_pk_1_and_invalid_data_is_400(self):
        response = self.client.put(
            "/api/requests/requests/1/",
            {"status": "INVALID"},
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_request_with_pk_4_is_404(self):
        response = self.client.put(
            "/api/requests/requests/4/",
            {"status": "COMPLETADO"},
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_request_with_pk_1_is_200(self):
        response = self.client.delete("/api/requests/requests/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_request_with_pk_4_is_404(self):
        response = self.client.delete("/api/requests/requests/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
