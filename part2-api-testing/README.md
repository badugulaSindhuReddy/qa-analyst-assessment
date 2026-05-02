# Part 2 — API Testing (JSONPlaceholder)

## Approach
I used pytest along with the `requests` library to test REST API endpoints from JSONPlaceholder.
The tests verify basic API behavior like status codes, response structure, and data correctness.
## Tests Covered
1. GET /users/1
   - Checks status code is 200
   - Verifies required fields (id, name, email)

2. POST /posts
   - Checks status code is 201
   - Confirms response matches the payload sent
   - Ensures a new id is generated

3. GET /users/999
   - Checks status code is 404 for a non-existent user
   - Confirms response is a valid JSON object

## Tools Used
- pytest (for writing and running tests)
- requests (for making HTTP calls)

## How to Run
Install dependencies:
  pip install pytest requests
Running the code:
  pytest test_api.py -v
