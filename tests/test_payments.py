from payment_api.models import User


def test_payment_flow(client, db_session):
	# create payer
	r = client.post("/users/", json={"name": "payer", "balance": 100.0})
	assert r.status_code == 200
	payer = db_session.query(User).filter_by(name="payer").first()
	# create payee
	r = client.post("/users/", json={"name": "payee", "balance": 20.0})
	assert r.status_code == 200
	payee = db_session.query(User).filter_by(name="payee").first()
	headers = {"X-API-Key": payer.api_key}
	# create payment
	r = client.post("/payments/", json={"payer_id": payer.id, "payee_id": payee.id, "amount": 50.0}, headers=headers)
	assert r.status_code == 200
	payment = r.json()
	assert payment["status"] == "pending"
	# complete payment
	r = client.post(f"/payments/{payment['id']}/complete", headers=headers)
	assert r.status_code == 200
	# balances should update
	payer_db = db_session.query(User).filter_by(name="payer").first()
	payee_db = db_session.query(User).filter_by(name="payee").first()
	assert payer_db.balance == 50.0
	assert payee_db.balance == 70.0
