from rest_framework import status
from rest_framework.test import APITestCase


class StudentViewSetTestCase(APITestCase):
    fixtures = ["schools.json", "users.json", "relatives.json", "students.json"]

    def setUp(self):
        self.user = self.client.login(
            email="john@example.com", password="Complexpass123"
        )
        self.student_count = 3

    def test_list_students_is_200_and_has_students(self):
        response = self.client.get("/api/students/students/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.student_count)

    def test_retrieve_student_with_pk_1_is_200_and_has_student(self):
        response = self.client.get("/api/students/students/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_retrieve_student_with_pk_4_is_404(self):
        response = self.client.get("/api/students/students/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_student_with_valid_data_is_201_and_has_student(self):
        response = self.client.post(
            "/api/students/students/",
            {
                "first_name": "Johan",
                "last_name": "Doe",
                "identification_type": "TI",
                "identification_number": "400000000",
                "phone_number": "400000000",
                "grade": "7",
                "sex": "M",
                "age": 12,
                "working_hours": "M",
                "school": 1,
                "relatives": [2],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["school"]["id"], 1)
        self.assertEqual(len(response.data["relatives"]), 1)

    def test_create_student_with_no_school_is_400(self):
        response = self.client.post(
            "/api/students/students/",
            {
                "first_name": "Johan",
                "last_name": "Doe",
                "identification_type": "TI",
                "identification_number": "400000000",
                "phone_number": "400000000",
                "grade": "7",
                "sex": "M",
                "age": 12,
                "working_hours": "M",
                "relatives": [2],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_student_with_existing_identification_number_is_400(self):
        response = self.client.post(
            "/api/students/students/",
            {
                "first_name": "Johan",
                "last_name": "Doe",
                "identification_type": "TI",
                "identification_number": "100000000",
                "phone_number": "100000000",
                "grade": "7",
                "sex": "M",
                "age": 12,
                "working_hours": "M",
                "school": 1,
                "relatives": [2],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_student_with_invalid_relatives_is_400(self):
        response = self.client.post(
            "/api/students/students/",
            {
                "first_name": "Johan",
                "last_name": "Doe",
                "identification_type": "TI",
                "identification_number": "100000000",
                "phone_number": "100000000",
                "grade": "7",
                "sex": "M",
                "age": 12,
                "working_hours": "M",
                "school": 1,
                "relatives": [10],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_student_with_pk_1_is_200_and_has_student(self):
        response = self.client.put(
            "/api/students/students/1/",
            {
                "first_name": "Johan",
                "last_name": "Doe",
                "school": 3,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "Johan")
        self.assertEqual(response.data["last_name"], "Doe")
        self.assertEqual(response.data["school"]["id"], 3)

    def test_update_student_with_pk_4_is_404(self):
        response = self.client.put(
            "/api/students/students/4/",
            {
                "first_name": "Johan",
                "last_name": "Doe",
                "school": 3,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_student_with_pk_1_and_existing_identification_number_is_400(self):
        response = self.client.put(
            "/api/students/students/1/",
            {
                "identification_type": "TI",
                "identification_number": "200000000",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_student_with_pk_1_and_invalid_school_is_400(self):
        response = self.client.put(
            "/api/students/students/1/",
            {
                "school": 4,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_student_with_pk_1_and_invalid_relatives_is_400(self):
        response = self.client.put(
            "/api/students/students/1/",
            {
                "relatives": [10],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_student_with_pk_1_is_200(self):
        response = self.client.delete("/api/students/students/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_student_with_pk_4_is_404(self):
        response = self.client.delete("/api/students/students/4/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
