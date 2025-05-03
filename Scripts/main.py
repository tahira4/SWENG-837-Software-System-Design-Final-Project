from student import Student
from tutor import Tutor
from session import Session

# Sample usage
student = Student("S1", "Alice", "alice@example.com", "Student")
tutor = Tutor("T1", "Bob", "bob@example.com", "Tutor")
session = Session("SESS101", student, tutor, "2025-05-02 10:00")

student.book_session(session.session_id)
session.join()
student.submit_feedback("Great session!")