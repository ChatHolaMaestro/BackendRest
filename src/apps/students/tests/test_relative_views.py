from rest_framework import status
from rest_framework.test import APITestCase


class RelativeViewSetTestCase(APITestCase):
    fixtures = ["schools.json", "users.json", "relatives.json", "students.json"]

    def setUp(self):
        self.user = self.client.login(
            email="john@example.com", password="Complexpass123"
        )
        self.relative_count = 3

    def test_list_relatives_is_200_and_has_relatives(self):
        response = self.client.get("/api/students/relatives/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.relative_count)

    def test_retrieve_relative_with_pk_1_is_200_and_has_relative(self):
        response = self.client.get("/api/students/relatives/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_retrieve_relative_with_pk_4_is_404(self):
        response = self.client.get("/api/students/relatives/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_relative_with_valid_data_is_201_and_has_relative(self):
        response = self.client.post(
            "/api/students/relatives/",
            {
                "first_name": "Johan",
                "last_name": "Doe",
                "identification_type": "CC",
                "identification_number": "440000000",
                "phone_number": "440000000",
                "students": [1],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data["students"]), 1)

    def test_create_relative_with_existing_identification_number_is_400(self):
        response = self.client.post(
            "/api/students/relatives/",
            {
                "first_name": "Johan",
                "last_name": "Doe",
                "identification_type": "CC",
                "identification_number": "110000000",
                "phone_number": "110000000",
                "students": [2],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_relative_with_invalid_students_is_400(self):
        response = self.client.post(
            "/api/students/relatives/",
            {
                "first_name": "Johan",
                "last_name": "Doe",
                "identification_type": "CC",
                "identification_number": "110000000",
                "phone_number": "110000000",
                "students": [10],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_relative_with_pk_1_is_200_and_has_relative(self):
        response = self.client.put(
            "/api/students/relatives/1/",
            {
                "first_name": "Johan",
                "last_name": "Doe",
                "students": [1],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "Johan")
        self.assertEqual(response.data["last_name"], "Doe")
        self.assertEqual(len(response.data["students"]), 1)

    def test_update_relative_with_pk_4_is_404(self):
        response = self.client.put(
            "/api/students/relatives/4/",
            {
                "first_name": "Johan",
                "last_name": "Doe",
                "students": [1],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_relative_with_pk_1_and_existing_identification_number_is_400(self):
        response = self.client.put(
            "/api/students/relatives/1/",
            {
                "identification_type": "CC",
                "identification_number": "220000000",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_relative_with_pk_1_and_invalid_students_is_400(self):
        response = self.client.put(
            "/api/students/relatives/1/",
            {
                "students": [10],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_relative_with_pk_1_is_200(self):
        response = self.client.delete("/api/students/relatives/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_relative_with_pk_4_is_404(self):
        response = self.client.delete("/api/students/relatives/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
