from rest_framework import status
from rest_framework.test import APITestCase


class TeacherViewSetTestCase(APITestCase):
    fixtures = ["subjects.json", "users.json", "teachers.json", "schedules.json"]

    def setUp(self):
        self.user = self.client.login(
            email="john@example.com", password="Complexpass123"
        )
        self.teacher_count = 3

    def test_list_teachers_is_200_and_has_teachers(self):
        response = self.client.get("/api/teachers/teachers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.teacher_count)

    def test_retrieve_teacher_with_pk_1_is_200_and_has_teacher(self):
        response = self.client.get("/api/teachers/teachers/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_retrieve_teacher_with_pk_4_is_404(self):
        response = self.client.get("/api/teachers/teachers/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_teacher_with_valid_data_is_201_and_has_teacher(self):
        response = self.client.post(
            "/api/teachers/teachers/",
            {"user": 1, "subjects": [1, 2, 3]},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user"]["id"], 1)
        self.assertEqual(len(response.data["subjects"]), 3)

    def test_create_teacher_with_no_user_is_400(self):
        response = self.client.post(
            "/api/teachers/teachers/",
            {
                "subjects": [1, 2, 3],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_teacher_with_existing_user_is_400(self):
        response = self.client.post(
            "/api/teachers/teachers/",
            {
                "user": 4,
                "subjects": [1, 2, 3],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_teacher_with_pk_1_is_200_and_has_teacher(self):
        response = self.client.put(
            "/api/teachers/teachers/1/",
            {
                "user": 1,
                "subjects": [1, 2, 3],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"]["id"], 1)
        self.assertEqual(len(response.data["subjects"]), 3)

    def test_update_teacher_with_pk_4_is_404(self):
        response = self.client.put(
            "/api/teachers/teachers/4/",
            {
                "user": 1,
                "subjects": [1, 2, 3],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_teacher_with_pk_1_and_existing_user_is_400(self):
        response = self.client.put(
            "/api/teachers/teachers/1/",
            {
                "user": 4,
                "subjects": [1, 2, 3],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_teacher_with_pk_1_and_invalid_user_is_400(self):
        response = self.client.put(
            "/api/teachers/teachers/1/",
            {
                "user": 10,
                "subjects": [1, 2, 3],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_teacher_with_pk_1_and_invalid_subjects_is_400(self):
        response = self.client.put(
            "/api/teachers/teachers/1/",
            {
                "user": 1,
                "subjects": [10, 11, 12],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_teacher_with_pk_1_is_200(self):
        response = self.client.delete("/api/teachers/teachers/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_teacher_with_pk_4_is_404(self):
        response = self.client.delete("/api/teachers/teachers/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
