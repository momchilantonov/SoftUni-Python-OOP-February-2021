class ExercisePlan:
    id = 0

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        duration_in_minutes = hours * 60
        return cls(trainer_id, equipment_id, duration_in_minutes)

    @staticmethod
    def get_next_id():
        ExercisePlan.id += 1
        return ExercisePlan.id
