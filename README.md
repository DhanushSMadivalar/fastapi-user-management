__<ins>FastAPI User Management API</ins>__

This is a simple User Management API built with FastAPI, supporting CRUD operations for user data.

__<ins>Installation :</ins>__



***Clone the repository:**

git clone https://github.com/yourusername/fastapi-user-management.git

cd fastapi-user-management


***Create a virtual environment:**

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows


***Install dependencies:**

pip install -r requirements.txt
Run the API:

uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000/.


**<ins>Testing</ins>**

Open http://127.0.0.1:8000/docs to test the API using FastAPI’s interactive Swagger UI.

Use Postman or curl to send requests.
