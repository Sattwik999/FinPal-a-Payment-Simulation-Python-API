from payment_api.models import User

def test_create_user(client, db_session):
	res = client.post("/users/", json={"name": "alice", "balance": 100.0})
	assert res.status_code == 200
	data = res.json()
	assert data["name"] == "alice"
	assert data["balance"] == 100.0
	# check api_key exists in DB
	db_user = db_session.query(User).filter_by(name="alice").first()
	assert db_user.api_key is not None