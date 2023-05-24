from rest_framework import status
from rest_framework.test import APITestCase


class SchoolManagerViewSetTestCase(APITestCase):
    fixtures = ["schools.json", "users.json", "school_managers.json"]

    def setUp(self):
        self.user = self.client.login(
            email="john@example.com", password="Complexpass123"
        )
        self.school_manager_count = 3

    def test_list_school_managers_is_200_and_has_school_managers(self):
        response = self.client.get("/api/schools/school_managers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.school_manager_count)

    def test_retrieve_school_manager_with_pk_1_is_200_and_has_school_manager(self):
        response = self.client.get("/api/schools/school_managers/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_retrieve_school_manager_with_pk_4_is_404(self):
        response = self.client.get("/api/schools/school_managers/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_school_manager_with_valid_data_is_201_and_has_school_manager(self):
        response = self.client.post(
            "/api/schools/school_managers/",
            {
                "user": 1,
                "school": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user"]["id"], 1)
        self.assertEqual(response.data["school"]["id"], 1)

    def test_create_school_manager_with_no_user_is_201(self):
        response = self.client.post(
            "/api/schools/school_managers/",
            {
                "school": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_school_manager_with_no_school_is_400(self):
        response = self.client.post(
            "/api/schools/school_managers/",
            {
                "user": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_school_manager_with_existing_user_is_400(self):
        response = self.client.post(
            "/api/schools/school_managers/",
            {
                "user": 7,
                "school": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_school_manager_with_pk_1_is_200_and_has_school_manager(self):
        response = self.client.put(
            "/api/schools/school_managers/1/",
            {
                "user": 1,
                "school": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"]["id"], 1)
        self.assertEqual(response.data["school"]["id"], 1)

    def test_update_school_manager_with_pk_4_is_404(self):
        response = self.client.put(
            "/api/schools/school_managers/4/",
            {
                "user": 1,
                "school": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_school_manager_with_pk_1_and_existing_user_is_400(self):
        response = self.client.put(
            "/api/schools/school_managers/1/",
            {
                "user": 7,
                "school": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_school_manager_with_pk_1_and_invalid_user_is_400(self):
        response = self.client.put(
            "/api/schools/school_managers/1/",
            {
                "user": 10,
                "school": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_school_manager_with_pk_1_and_invalid_school_is_400(self):
        response = self.client.put(
            "/api/schools/school_managers/1/",
            {
                "user": 1,
                "school": 4,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_school_manager_with_pk_1_is_200(self):
        response = self.client.delete("/api/schools/school_managers/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_school_manager_with_pk_4_is_404(self):
        response = self.client.delete("/api/schools/school_managers/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
