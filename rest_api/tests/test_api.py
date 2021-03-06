from rest_framework import status
from .base_test_api import BaseAPITestCase


class CreateError(BaseAPITestCase):
    def setUp(self):
        super().setUp()

    def test_create_errors_with_valid_params(self):
        response = self.client.post(self.url_error, self.valid_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_errors_with_invalid_params(self):
        response = self.client.post(self.url_error, self.invalid_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ListingError(BaseAPITestCase):
    def setUp(self):
        super().setUp()

    def test_listing_errors(self):
        response = self.client.get(self.url_error)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listing_errors_by_id(self):
        response = self.client.get(self.url_error, kwargs={'id': self.error.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdatingError(BaseAPITestCase):
    def setUp(self):
        super().setUp()

    def test_updating_errors_with_valid_params(self):
        response = self.client.put(f"{self.url_error}{self.error.id}/", self.valid_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_updating_errors_with_invalid_params(self):
        response = self.client.put(f"{self.url_error}{self.error.id}/", self.invalid_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class Deletion(BaseAPITestCase):
    def setUp(self):
        super().setUp()

    def test_deletion_errors(self):
        response = self.client.delete(f"{self.url_error}{self.error.id}/", format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
