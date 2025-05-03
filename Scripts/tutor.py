from user import User

class Tutor(User):
    def set_availability(self, slot):
        print(f"{self.name} set availability: {slot}")

    def view_feedback(self):
        print(f"{self.name} viewed feedback.")