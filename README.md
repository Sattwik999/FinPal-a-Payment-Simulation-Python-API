# FinPal - Payment Simulation Python API

A full-stack payment simulation project built with FastAPI (Python backend) and a simple HTML/CSS/JS frontend. This project allows users to register, log in with an API key, create payments, and view payment history. It is designed for learning, prototyping, and demonstration purposes.

## Features

- **User Registration:** Create users with a name and initial balance. Each user receives a unique API key.
- **Login:** Log in using your API key to access your dashboard.
- **Dashboard:** View your balance and payment history.
- **Create Payments:** Send payments to other registered users by specifying their name and amount.
- **Payment History:** See all payments you have made or received.
- **Background Tasks:** (Optional) Celery integration for sending payment receipts.
- **Docker Support:** Run the entire stack with Docker Compose.
- **Testing:** Pytest-based test suite for backend logic.

## Project Structure

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

## How to Run Locally

### 1. Clone the Repository
```sh
git clone https://github.com/Sattwik999/FinPal-a-Payment-Simulation-Python-API.git
cd FinPal-a-Payment-Simulation-Python-API
```

### 2. Set Up Environment Variables
- Copy `.env.example` to `.env` and fill in secrets as needed.
- For quick testing, use SQLite (default in `.env.example`).

### 3. Install Python Dependencies
```sh
pip install -r requirements.txt
```

### 4. Start the Backend
```sh
uvicorn payment_api.main:app --reload
```
- The API will be available at [http://localhost:8000](http://localhost:8000)
- Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)

### 5. Start the Frontend
- Open `frontend/index.html` directly in your browser.
- Use the UI to register, log in, create payments, and view history.

### 6. Run Tests
```sh
pip install -r dev-requirements.txt
pytest
```

### 7. Run with Docker (Optional)
```sh
docker-compose up --build
```
- This will start the backend, database, Redis, and Celery worker (if configured).

## API Endpoints

- `POST /users/` - Register a new user
- `GET /users` - List all users
- `GET /users/{user_id}` - Get user by ID
- `POST /payments/` - Create a payment
- `GET /payments/` - List payments for logged-in user

See [http://localhost:8000/docs](http://localhost:8000/docs) for full API documentation.

## Frontend Usage
- Register a user and copy your API key.
- Log in with your API key.
- Create payments by entering the recipient's name and amount.
- View your payment history in the dashboard.

## Collaboration & Contribution

1. **Fork the repository** and create your feature branch:
   ```sh
   git checkout -b feature/your-feature
   ```
2. **Commit your changes**:
   ```sh
   git commit -am "Add new feature"
   ```
3. **Push to your branch**:
   ```sh
   git push origin feature/your-feature
   ```
4. **Open a Pull Request** on GitHub.

### Guidelines
- Follow PEP8 for Python code.
- Keep frontend code clean and modular.
- Do not commit `.env` or database files.
- Add tests for new features.
- Document your changes in the README if needed.

## License

This project is for educational and demonstration purposes. See `LICENSE` for details.

---

For questions or issues, open an issue on GitHub or contact the maintainer.
