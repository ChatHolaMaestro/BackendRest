from rest_framework import status
from rest_framework.test import APITestCase


class SubjectViewSetTestCase(APITestCase):
    fixtures = ["subjects.json"]

    def setUp(self):
        self.user = self.client.login(
            email="john@example.com", password="Complexpass123"
        )
        self.subject_count = 3

    def test_list_subjects_is_200_and_has_subjects(self):
        response = self.client.get("/api/subjects/subjects/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.subject_count)

    def test_retrieve_subject_with_pk_1_is_200_and_has_subject(self):
        response = self.client.get("/api/subjects/subjects/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_retrieve_subject_with_pk_4_is_404(self):
        response = self.client.get("/api/subjects/subjects/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_subject_with_valid_data_is_201_and_has_subject(self):
        response = self.client.post(
            "/api/subjects/subjects/",
            {
                "name": "History",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "History")

    def test_create_subject_with_no_name_is_400(self):
        response = self.client.post(
            "/api/subjects/subjects/",
            {},
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_subject_with_existing_name_is_400(self):
        response = self.client.post(
            "/api/subjects/subjects/",
            {
                "name": "English",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_subject_with_pk_1_and_valid_data_is_200_and_has_updated_subject(
        self,
    ):
        response = self.client.put(
            "/api/subjects/subjects/1/",
            {
                "name": "History",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "History")

    def test_update_subject_with_pk_1_and_existing_name_is_400(self):
        response = self.client.put(
            "/api/subjects/subjects/1/",
            {
                "name": "English",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_subject_with_pk_1_is_200(self):
        response = self.client.delete("/api/subjects/subjects/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_subject_with_pk_4_is_404(self):
        response = self.client.delete("/api/subjects/subjects/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
