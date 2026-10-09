#communicate with workout data + add csv file to database
import sqlite3 as sq

import pandas as pd


def load_dataset():
    df=pd.read_csv("Updated_ExerciseDataset.csv")
    catalog=df[["Exercise_Name", "muscle_gp" ,"Equipment"]].copy()
    catalog = catalog.astype(object).where(pd.notna(catalog), None)
    rows = catalog.itertuples(index=False, name=None)

    db = sq.connect("database/main/pulse.db")
    try:
        db.executemany(
            """
            INSERT INTO exercises(name, target, equipment)
            VALUES(?, ?, ?)
            """,
            rows
        )
        db.commit()
    finally:
        db.close()

if __name__ == "main":
 load_dataset()
