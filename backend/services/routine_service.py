#create a routine & days 
import sqlite3 as sq


class RoutineCreate:
    DAY_NAMES = (
        "Day1", "Day2", "Day3", "Day4",
        "Day5", "Day6", "Day7",
    )

    def __init__(self, dayname = DAY_NAMES):
        self._database = sq.connect("../database/main/pulse.db")
        self._daynames = dayname
        self.CreateRoutine = self.create_routine(name="STR",days="SR")
    def create_routine(self, name: str, days: str):
        db = self._database
        cursor = db.execute(
            """
            INSERT INTO routinebase(name, days)
            VALUES(?, ?)
            """,
            (name, days)
        )
        routine_id = cursor.lastrowid

        for day in self._daynames:
            db.execute(
                """
                INSERT INTO routinedays(routine_id, day_name)
                VALUES(?, ?)
                """,
                (routine_id, day)
            )
    






