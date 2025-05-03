from user import User

class Student(User):
    def book_session(self, session):
        print(f"{self.name} booked session: {session}")

    def cancel_session(self, session_id):
        print(f"{self.name} cancelled session ID: {session_id}")

    def submit_feedback(self, feedback):
        print(f"{self.name} submitted feedback: {feedback}")