class Availability:
    def __init__(self, slot_id, tutor_id, date, start_time, end_time, is_booked=False):
        self.slot_id = slot_id
        self.tutor_id = tutor_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.is_booked = is_booked