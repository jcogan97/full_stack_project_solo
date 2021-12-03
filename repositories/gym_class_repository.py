from db.run_sql import run_sql
from models.gym_class import GymClass
from models.member import Member

def save(gym_class):
    sql = "INSERT INTO gym_classes (description, duration, available_slots, type) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [gym_class.description, gym_class.duration, gym_class.available_slots, gym_class.type]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class