const API_BASE = "http://localhost:8000";
let apiKey = "";
let userId = null;

function registerUser() {
    const name = document.getElementById('register-name').value;
    const balance = document.getElementById('register-balance').value;
    fetch(`${API_BASE}/users/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, balance: Number(balance) })
    })
    .then(res => res.json())
    .then(data => {
        if (data.api_key && data.id) {
            document.getElementById('register-result').innerText = `Registered! Your API Key: ${data.api_key} | User ID: ${data.id}`;
            userId = data.id;
            apiKey = data.api_key;
        } else {
            document.getElementById('register-result').innerText = data.detail || 'Registration failed.';
        }
    })
    .catch(() => {
        document.getElementById('register-result').innerText = 'Error registering user.';
    });
}

function loginUser() {
    apiKey = document.getElementById('api-key').value;
    userId = null;
    if (!apiKey) {
        document.getElementById('login-result').innerText = 'Please enter your API key.';
        return;
    }
    // Try to find user by API key (fetch all users and match)
    fetch(`${API_BASE}/users`, { headers: { 'Accept': 'application/json' } })
    .then(res => res.json())
    .then(users => {
        const user = users.find(u => u.api_key === apiKey);
        if (user) {
            userId = user.id;
            document.getElementById('login-section').style.display = 'none';
            document.getElementById('register-section').style.display = 'none';
            document.getElementById('dashboard-section').style.display = 'block';
            document.getElementById('user-info').innerText = `Hello, ${user.name}! Balance: $${user.balance}`;
            loadPaymentHistory();
        } else {
            document.getElementById('login-result').innerText = 'Invalid API key.';
        }
    })
    .catch(() => {
        document.getElementById('login-result').innerText = 'Error logging in.';
    });
}

function logoutUser() {
    apiKey = "";
    userId = null;
    document.getElementById('dashboard-section').style.display = 'none';
    document.getElementById('login-section').style.display = 'block';
    document.getElementById('register-section').style.display = 'block';
    document.getElementById('api-key').value = "";
    document.getElementById('login-result').innerText = "";
}

function createPayment() {
    const amount = document.getElementById('payment-amount').value;
    const recipientName = document.getElementById('payment-recipient').value;
    if (!userId || !apiKey) {
        document.getElementById('payment-result').innerText = 'Please login first.';
        return;
    }
    // Lookup recipient user ID by name
    fetch(`${API_BASE}/users`, { headers: { 'Accept': 'application/json' } })
    .then(res => res.json())
    .then(users => {
        const recipient = users.find(u => u.name === recipientName);
        if (!recipient) {
            document.getElementById('payment-result').innerText = 'Recipient not found.';
            return;
        }
        const payeeId = recipient.id;
        fetch(`${API_BASE}/payments/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-API-Key': apiKey
            },
            body: JSON.stringify({ payer_id: userId, payee_id: payeeId, amount: Number(amount), currency: 'USD' })
        })
        .then(res => res.json())
        .then(data => {
            if (data.id) {
                document.getElementById('payment-result').innerText = 'Payment created!';
                loadPaymentHistory();
            } else {
                document.getElementById('payment-result').innerText = data.detail || 'Payment failed.';
            }
        })
        .catch(() => {
            document.getElementById('payment-result').innerText = 'Error creating payment.';
        });
    })
    .catch(() => {
        document.getElementById('payment-result').innerText = 'Error finding recipient.';
    });
}

function loadPaymentHistory() {
    fetch(`${API_BASE}/payments/`, {
        headers: { 'X-API-Key': apiKey }
    })
    .then(res => res.json())
    .then(data => {
        if (Array.isArray(data)) {
            let html = '<ul>';
            data.forEach(p => {
                html += `<li>ID: ${p.id}, Amount: $${p.amount}, Payee ID: ${p.payee_id}, Status: ${p.status}</li>`;
            });
            html += '</ul>';
            document.getElementById('payment-history').innerHTML = html;
        } else {
            document.getElementById('payment-history').innerText = 'No payments found.';
        }
    })
    .catch(() => {
        document.getElementById('payment-history').innerText = 'Error loading payments.';
    });
}
