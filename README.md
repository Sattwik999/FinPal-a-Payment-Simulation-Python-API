![FinPal Banner](banner.png)


# FinPal - Payment Simulation Python API

Hi! I'm Sattwik Sarkar, and this is my personal project: a full-stack payment simulation app built with FastAPI (Python backend) and a simple HTML/CSS/JS frontend. I created this project to learn, experiment, and demonstrate how a modern payment API works from scratch.

---

## Why I Built This
I wanted to understand how payment systems work under the hood, practice building REST APIs, and get hands-on with Docker, testing, and frontend integration. This project helped me learn about authentication, database transactions, and background processing.

---

## Tech Stack
- **Backend:** FastAPI, SQLAlchemy, Pydantic
- **Database:** SQLite (default), PostgreSQL (optional)
- **Task Queue:** Celery (optional)
- **Frontend:** HTML, CSS, JavaScript
- **Testing:** Pytest
- **Containerization:** Docker, Docker Compose

---

## Key Features
- User registration with API key authentication
- Payment creation, completion, and cancellation
- Payment history dashboard
- Background email receipts (Celery)
- RESTful API with OpenAPI docs
- Dockerized setup for easy deployment
- Pytest-based test suite

---

## Example API Request
```bash
# Register a user
curl -X POST http://localhost:8000/users/ -H "Content-Type: application/json" -d '{"name": "Alice", "balance": 100}'

# Create a payment
curl -X POST http://localhost:8000/payments/ -H "Content-Type: application/json" -H "x-api-key: <your_api_key>" -d '{"payer_id": 1, "payee_id": 2, "amount": 10, "currency": "USD"}'
```

---

## Future Improvements / Roadmap
- Add OAuth2 authentication
- Integrate Stripe or Razorpay for real payments
- Add user profile pictures
- Improve frontend UI/UX
- Add admin dashboard
- Deploy to cloud (Azure, Heroku, etc.)

---

## Links
- [LinkedIn](https://www.linkedin.com/in/sattwik-sarkar999)
- [Portfolio](http://www.sattwiksarkar.me/)
- [More Projects](https://github.com/Sattwik999)

---

## About the Project

This app lets you:
- Register as a user (with a name and starting balance)
- Get a unique API key for authentication
- Log in using your API key
- View your dashboard (balance and payment history)
- Send payments to other users
- See all payments you've made or received
- (Optionally) Send payment receipts via background tasks (Celery)

Everything is designed for easy local setup, quick prototyping, and clear code structure. You can run it with Docker or just Python, and the frontend is pure HTML/CSS/JS for simplicity.

---

## How I Built & Set Up the Python Backend

### 1. Project Structure

```
├── payment_api/         # FastAPI backend
│   ├── main.py          # App entrypoint
│   ├── models.py        # SQLAlchemy models
│   ├── routes/          # API routes (users, payments)
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # DB setup
│   ├── config.py        # Settings
│   ├── tasks.py         # Celery tasks (optional)
│   └── ...
├── frontend/            # HTML/CSS/JS frontend
│   ├── index.html       # Main UI
│   ├── style.css        # Styles
│   └── app.js           # JS logic
├── tests/               # Pytest tests
├── requirements.txt     # Python dependencies
├── dev-requirements.txt # Dev/test dependencies
├── Dockerfile           # Backend Dockerfile
├── docker-compose.yml   # Multi-service orchestration
├── .env.example         # Example environment config
├── .gitignore           # Ignore secrets, DB, etc.
└── README.md            # Project documentation
```

### 2. Setting Up Locally (Step-by-Step)

### 1. Clone the Repository
```sh
git clone https://github.com/Sattwik999/FinPal-a-Payment-Simulation-Python-API.git
cd FinPal-a-Payment-Simulation-Python-API
```

#### Configure Environment Variables
- Copy `.env.example` to `.env`:
  ```sh
  cp .env.example .env
  ```
- Edit `.env` as needed. For quick testing, SQLite is the default.

### 3. Install Python Dependencies
```sh
pip install -r requirements.txt
```

#### Start the Backend
```sh
uvicorn payment_api.main:app --reload
```
- The API runs at [http://localhost:8000](http://localhost:8000)
- Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)

#### Start the Frontend
- Open `frontend/index.html` in your browser.
- Use the UI to register, log in, create payments, and view history.

#### Run Tests
```sh
pip install -r dev-requirements.txt
pytest
```

#### Run Everything with Docker (Optional)
```sh
docker-compose up --build
```
- This starts backend, database, Redis, and Celery worker (if configured).

---

## API Endpoints

- `POST /users/` - Register a new user
- `GET /users` - List all users
- `GET /users/{user_id}` - Get user by ID
- `POST /payments/` - Create a payment
- `GET /payments/` - List payments for logged-in user

See [http://localhost:8000/docs](http://localhost:8000/docs) for full API documentation.

---

## Frontend Usage
- Register a user and copy your API key.
- Log in with your API key.
- Create payments by entering the recipient's name and amount.
- View your payment history in the dashboard.

---

## Collaboration & Contribution

If you want to contribute:
1. Fork the repo and create your feature branch:
   ```sh
   git checkout -b feature/your-feature
   ```
2. Commit your changes:
   ```sh
   git commit -am "Add new feature"
   ```
3. Push to your branch:
   ```sh
   git push origin feature/your-feature
   ```
4. Open a Pull Request on GitHub.



---

## Author
**Sattwik Sarkar**

---

## License
This project is for educational and demonstration purposes. See `LICENSE` for details.

---

For questions or issues, open an issue on GitHub or contact me directly.
