import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


class TestJSONPlaceholderAPI:

    # 1. GET /users/1 — fetch a known user and validate response structure
    def test_get_user_returns_200_and_required_fields(self):
        """
        Check that an existing user returns 200 and has id, name, and email.
        """
        response = requests.get(f"{BASE_URL}/users/1")

        # Status code must be 200 OK
        assert response.status_code == 200, (
            f"Expected 200, got {response.status_code}"
        )

        body = response.json()

        # Make sure required fields exist
        for field in ("id", "name", "email"):
            assert field in body, f"Missing required field: '{field}'"
            assert body[field] is not None, f"Field '{field}' must not be None"

        # Sanity-check the values returned for user 1
        assert body["id"] == 1
        assert "@" in body["email"], "email field should look like an email address"

    # 2. POST /posts — create a new post
    def test_post_creates_new_post_and_returns_201(self):
        """
        Check that creating a post returns 201 and echoes back the data.
        """
        payload = {
            "title":  "QA Assessment Post",
            "body":   "Testing POST endpoint for SS&C assignment.",
            "userId": 1,
        }

        response = requests.post(f"{BASE_URL}/posts", json=payload)

        # Should return created
        assert response.status_code == 201, (
            f"Expected 201, got {response.status_code}"
        )

        body = response.json()

        # Response should match what we sent
        assert body["title"]  == payload["title"],  "title mismatch"
        assert body["body"]   == payload["body"],   "body mismatch"
        assert body["userId"] == payload["userId"], "userId mismatch"

        # API should generate an id
        assert "id" in body, "Response must include an id for the new resource"
        assert isinstance(body["id"], int), "id must be an integer"

    #  3. GET /users/999 — user does not exist
    def test_get_nonexistent_user_returns_404(self):
        """
         Check that a missing user returns 404.
        """
        response = requests.get(f"{BASE_URL}/users/999")

        assert response.status_code == 404, (
            f"Expected 404, got {response.status_code}"
        )

        # Should return empty JSON object
        body = response.json()
        assert isinstance(body, dict), "Response body should be a JSON object"
