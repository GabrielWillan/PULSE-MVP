#communicate with workout data + add csv file to database
import sqlite3 as sq

import pandas as pd

df = pd.read_csv("Updated_ExerciseDataset.csv")
Exercise_Name = df["Exercise_Name"].values
Exercise_Target = df["muscle_gp"].values
Exercise_Equipment = df["muscle_gp"].values


def load_dataset(name:Exercise_Name, target:Exercise_Target, equipment: Exercise_Equipment ):
    db = sq.connect("database/main/pulse.db")
    try:
        cursor = db.execute(
            """
            INSERT INTO exercises(name, target, equipment)
            VALUES(?, ?, ?)
            """,
            (name, target, equipment)
        )
        db.commit()
        cursor.lastrowid()
    finally:
        db.close()
