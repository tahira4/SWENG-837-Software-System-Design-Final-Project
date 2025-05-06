# classes_and_methods.py

from abc import ABC, abstractmethod

# Base User class with inheritance
class User(ABC):
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    @abstractmethod
    def get_role(self):
        pass


class Student(User):
    def get_role(self):
        return "Student"

    def request_session(self, tutor_id, subject):
        # pseudocode: logic to request a new session
        pass


class Tutor(User):
    def get_role(self):
        return "Tutor"

    def accept_session(self, session_id):
        # pseudocode: logic to accept a session
        pass


class Faculty(User):
    def get_role(self):
        return "Faculty"

    def review_feedback(self):
        # pseudocode: logic for faculty to view feedback reports
        pass


class Session:
    def __init__(self, session_id, student, tutor, time, status):
        self.session_id = session_id
        self.student = student
        self.tutor = tutor
        self.time = time
        self.status = status  # scheduled, in_progress, completed, canceled

    def start_session(self):
        # pseudocode to mark session as in progress
        pass

    def complete_session(self):
        # pseudocode to mark session as completed
        pass


class Feedback:
    def __init__(self, feedback_id, session, rating, comment):
        self.feedback_id = feedback_id
        self.session = session
        self.rating = rating
        self.comment = comment

    def submit_feedback(self):
        # pseudocode to store feedback
        pass


# Factory Pattern for user creation
class UserFactory:
    @staticmethod
    def create_user(user_type, user_id, name, email):
        if user_type == "Student":
            return Student(user_id, name, email)
        elif user_type == "Tutor":
            return Tutor(user_id, name, email)
        elif user_type == "Faculty":
            return Faculty(user_id, name, email)
        else:
            raise ValueError("Invalid user type")


# Singleton for session scheduler
class SessionScheduler:
    _instance = None

    def __init__(self):
        if SessionScheduler._instance is not None:
            raise Exception("This class is a singleton!")
        SessionScheduler._instance = self
        self.sessions = []

    @staticmethod
    def get_instance():
        if SessionScheduler._instance is None:
            SessionScheduler()
        return SessionScheduler._instance

    def schedule_session(self, student, tutor, time):
        # pseudocode to schedule a session
        pass


# Observer pattern for notifications
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class NotificationService:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def notify_all(self, message):
        for observer in self.observers:
            observer.update(message)
