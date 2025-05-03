class Session:
    def __init__(self, session_id, student, tutor, datetime, status='Scheduled'):
        self.session_id = session_id
        self.student = student
        self.tutor = tutor
        self.datetime = datetime
        self.status = status

    def join(self):
        print(f"Session {self.session_id} started.")

    def cancel(self):
        self.status = 'Cancelled'
        print(f"Session {self.session_id} cancelled.")