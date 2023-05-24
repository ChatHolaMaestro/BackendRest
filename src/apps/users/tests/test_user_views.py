from rest_framework import status
from rest_framework.test import APITestCase


class UserViewSetTestCase(APITestCase):
    fixtures = ["users.json"]

    def setUp(self):
        self.user = self.client.login(
            email="john@example.com", password="Complexpass123"
        )
        self.user_count = 9

    def test_list_users_is_200_and_has_users(self):
        response = self.client.get("/api/users/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.user_count)

    def test_retrieve_user_with_pk_1_is_200_and_has_user(self):
        response = self.client.get("/api/users/users/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_retrieve_user_with_pk_10_is_404(self):
        response = self.client.get("/api/users/users/10/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_admin_user_with_valid_data_is_201_and_has_user(self):
        response = self.client.post(
            "/api/users/users/",
            {
                "email": "newuser@example.com",
                "password": "Complexpass123",
                "first_name": "New",
                "last_name": "User",
                "identification_type": "CC",
                "identification_number": "123456789",
                "phone_number": "123456789",
                "role": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["email"], "newuser@example.com")

    def test_create_user_with_no_role_is_201_and_user_is_admin(self):
        response = self.client.post(
            "/api/users/users/",
            {
                "email": "newuser@example.com",
                "password": "Complexpass123",
                "first_name": "New",
                "last_name": "User",
                "identification_type": "CC",
                "identification_number": "123456789",
                "phone_number": "123456789",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["role"], 1)

    def test_create_user_with_existing_email_is_400(self):
        response = self.client.post(
            "/api/users/users/",
            {
                "email": "john@example.com",
                "password": "Complexpass123",
                "first_name": "New",
                "last_name": "User",
                "identification_type": "CC",
                "identification_number": "123456789",
                "phone_number": "123456789",
                "role": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_existing_identification_number_is_400(self):
        response = self.client.post(
            "/api/users/users/",
            {
                "email": "newuser@example.com",
                "password": "Complexpass123",
                "first_name": "New",
                "last_name": "User",
                "identification_type": "CC",
                "identification_number": "111111111",
                "phone_number": "123456789",
                "role": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_invalid_email_address_is_400(self):
        response = self.client.post(
            "/api/users/users/",
            {
                "email": "newuser",
                "password": "Complexpass123",
                "first_name": "New",
                "last_name": "User",
                "identification_type": "CC",
                "identification_number": "123456789",
                "phone_number": "123456789",
                "role": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_user_with_pk_1_is_200_and_has_updated_user(self):
        response = self.client.put(
            "/api/users/users/1/",
            {
                "email": "newemail@example.com",
                "first_name": "Newer",
                "last_name": "User",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "newemail@example.com")
        self.assertEqual(response.data["first_name"], "Newer")
        self.assertEqual(response.data["last_name"], "User")

    def test_update_user_with_pk_10_is_404(self):
        response = self.client.put(
            "/api/users/users/10/",
            {
                "email": "newemail@example.com",
                "first_name": "Newer",
                "last_name": "User",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_user_with_pk_1_and_existing_email_is_400(self):
        response = self.client.put("/api/users/users/1/", {"email": "jane@example.com"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_user_with_pk_1_and_existing_identification_number_is_400(self):
        response = self.client.put(
            "/api/users/users/1/", {"identification_number": "222222222"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_user_with_pk_1_and_invalid_email_address_is_400(self):
        response = self.client.put("/api/users/users/1/", {"email": "newemail"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_user_with_pk_1_is_200(self):
        response = self.client.delete("/api/users/users/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user_with_pk_10_is_404(self):
        response = self.client.delete("/api/users/users/10/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
