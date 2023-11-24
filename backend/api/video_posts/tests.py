from django.core.management import call_command
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from api.video_posts.models import VideoPost
from api.video_posts.serializers import VideoPostSerializer
import json


def authenticate(client):
    response = client.post(
        reverse("register"),
        {
            "first_name": "John",
            "last_name": "Doe",
            "username": "iamjohndoe",
            "password": "iamjohndoe",
        },
    )

    response = client.post(
        reverse("login"),
        {"username": "iamjohndoe", "password": "iamjohndoe"},
    )
    token = response.data["access_token"]
    client.credentials(HTTP_AUTHORIZATION="Bearer " + token)


class TestAddVideoPostAPI(APITestCase):
    def setUp(self):
        self.payload = {
            "title": "Sample Video",
            "description": "Sample Description",
            "video_url": "https://res.cloudinary.com/markuscloud/video/upload/v1700802932/nwva4le2xokznk9oyfxw.mp4",
            "thumbnail_url": "https://res.cloudinary.com/markuscloud/image/upload/v1700802423/brul1z7qluplzhebtonb.jpg",
        }
        super().setUp()

    def test_unauthenticated_request_to_post_video(self):
        response = self.client.post(reverse("post_video"), self.payload)
        json_response = response.data
        expected_status_code = 403
        expected_message = "Authentication credentials were not provided."
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_message, json_response["detail"])

    def test_authenticated_request_to_post_video(self):
        authenticate(self.client)
        response = self.client.post(reverse("post_video"), self.payload)
        json_response = response.data
        expected_status_code = 201
        expected_message = "Successfully posted video"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_message, json_response["message"])

    def test_missing_payload_upon_create(self):
        authenticate(self.client)
        self.payload = {}
        response = self.client.post(reverse("post_video"), self.payload)
        json_response = response.data
        expected_status_code = 400
        expected_message = "This field is required."

        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_message, str(json_response["title"][0]))
        self.assertEqual(expected_message, str(json_response["description"][0]))
        self.assertEqual(expected_message, str(json_response["video_url"][0]))
        self.assertEqual(expected_message, str(json_response["thumbnail_url"][0]))

    def test_blank_video_title_upon_create(self):
        authenticate(self.client)
        self.payload["title"] = ""
        response = self.client.post(reverse("post_video"), self.payload)
        json_response = response.data
        expected_status_code = 400
        expected_message = "This field may not be blank."

        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_message, str(json_response["title"][0]))

    def test_blank_video_description_upon_create(self):
        authenticate(self.client)
        self.payload["description"] = ""
        response = self.client.post(reverse("post_video"), self.payload)
        json_response = response.data
        expected_status_code = 400
        expected_message = "This field may not be blank."

        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_message, str(json_response["description"][0]))

    def test_blank_video_url_upon_create(self):
        authenticate(self.client)
        self.payload["video_url"] = ""
        response = self.client.post(reverse("post_video"), self.payload)
        json_response = response.data
        expected_status_code = 400
        expected_message = "This field may not be blank."

        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_message, str(json_response["video_url"][0]))

    def test_blank_thumbnail_url_upon_create(self):
        authenticate(self.client)
        self.payload["thumbnail_url"] = ""
        response = self.client.post(reverse("post_video"), self.payload)
        json_response = response.data
        expected_status_code = 400
        expected_message = "This field may not be blank."

        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_message, str(json_response["thumbnail_url"][0]))


class TestFetchSpecificVideoPostAPI(APITestCase):
    def setUp(self):
        self.payload = {
            "title": "Sample Video",
            "description": "Sample Description",
            "video_url": "https://res.cloudinary.com/markuscloud/video/upload/v1700802932/nwva4le2xokznk9oyfxw.mp4",
            "thumbnail_url": "https://res.cloudinary.com/markuscloud/image/upload/v1700802423/brul1z7qluplzhebtonb.jpg",
        }
        super().setUp()

    def test_unauthenticated_request_to_fetch_video_post(self):
        response = self.client.get(
            reverse("fetch_specific_video_by_id", kwargs={"id": 1})
        )
        json_response = response.data
        expected_status_code = 403
        expected_message = (
            expected_message
        ) = "Authentication credentials were not provided."
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_message, json_response["detail"])

    def test_authenticated_request_to_fetch_video_post(self):
        authenticate(self.client)

        # add video_post
        response = self.client.post(reverse("post_video"), self.payload)
        json_response = response.data["video"]

        # get video_post by id
        response = self.client.get(
            reverse("fetch_specific_video_by_id", kwargs={"id": json_response["id"]})
        )
        expected_status_code = 200
        response_video_post_data = response.data

        self.assertEqual(expected_status_code, response.status_code)

        # assert video_post data
        video_post = VideoPost.objects.get(pk=json_response["id"])
        serializer = VideoPostSerializer(video_post)

        expected_title = serializer.data["title"]
        expected_description = serializer.data["description"]
        expected_video_url = serializer.data["video_url"]
        expected_thumbnail_url = serializer.data["thumbnail_url"]

        self.assertEqual(expected_title, response_video_post_data["title"])
        self.assertEqual(
            expected_description,
            response_video_post_data["description"],
        )
        self.assertEqual(
            expected_video_url,
            response_video_post_data["video_url"],
        )
        self.assertEqual(
            expected_thumbnail_url,
            response_video_post_data["thumbnail_url"],
        )

    # add more tests here


class TestFetchAllVideoPostAPI(APITestCase):
    pass
    # add tests here


class TestUpdateVideoPostAPI(APITestCase):
    pass
    # add tests here


class TestDeleteVideoPostAPI(APITestCase):
    pass
    # add tests here
