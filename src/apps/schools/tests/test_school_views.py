from rest_framework import status
from rest_framework.test import APITestCase


class SchoolViewSetTestCase(APITestCase):
    fixtures = ["schools.json"]

    def setUp(self):
        self.user = self.client.login(
            email="john@example.com", password="Complexpass123"
        )
        self.school_count = 3

    def test_list_schools_is_200_and_has_schools(self):
        response = self.client.get("/api/schools/schools/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.school_count)

    def test_retrieve_school_with_pk_1_is_200_and_has_school(self):
        response = self.client.get("/api/schools/schools/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_retrieve_school_with_pk_4_is_404(self):
        response = self.client.get("/api/schools/schools/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_school_with_valid_data_is_201_and_has_school(self):
        response = self.client.post(
            "/api/schools/schools/",
            {
                "name": "New School",
                "address": "New Address",
                "has_morning_hours": True,
                "has_afternoon_hours": True,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "New School")
        self.assertEqual(response.data["address"], "New Address")
        self.assertEqual(response.data["has_morning_hours"], True)
        self.assertEqual(response.data["has_afternoon_hours"], True)

    def test_create_school_with_no_name_is_400(self):
        response = self.client.post(
            "/api/schools/schools/",
            {
                "address": "New Address",
                "has_morning_hours": True,
                "has_afternoon_hours": True,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_school_with_no_address_is_400(self):
        response = self.client.post(
            "/api/schools/schools/",
            {
                "name": "New School",
                "has_morning_hours": True,
                "has_afternoon_hours": True,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_school_with_existing_name_is_400(self):
        response = self.client.post(
            "/api/schools/schools/",
            {
                "name": "School 1",
                "address": "New Address",
                "has_morning_hours": True,
                "has_afternoon_hours": True,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_school_with_pk_1_and_valid_data_is_200_and_has_updated_school(
        self,
    ):
        response = self.client.put(
            "/api/schools/schools/1/",
            {
                "name": "Updated School",
                "address": "Updated Address",
                "has_morning_hours": False,
                "has_afternoon_hours": False,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated School")
        self.assertEqual(response.data["address"], "Updated Address")
        self.assertEqual(response.data["has_morning_hours"], False)
        self.assertEqual(response.data["has_afternoon_hours"], False)

    def test_update_school_with_pk_1_and_existing_name_is_400(self):
        response = self.client.put(
            "/api/schools/schools/1/",
            {
                "name": "School 2",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_school_with_pk_1_is_200(self):
        response = self.client.delete("/api/schools/schools/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_school_with_pk_4_is_404(self):
        response = self.client.delete("/api/schools/schools/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
