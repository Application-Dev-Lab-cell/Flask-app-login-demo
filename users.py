# Simple user store (replace with DB later)
users = {
    "admin": "password123",
    "devops": "devops2026"
}

def check_login(username, password):
    return users.get(username) == password