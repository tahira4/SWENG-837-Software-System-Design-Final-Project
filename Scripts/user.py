class User:
    def __init__(self, user_id, name, email, role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role

    def login(self, password):
        print(f"{self.name} logged in.")

    def logout(self):
        print(f"{self.name} logged out.")