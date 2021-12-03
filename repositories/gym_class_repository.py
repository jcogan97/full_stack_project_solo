from db.run_sql import run_sql
from models.gym_class import GymClass
from models.member import Member

def save(gym_class):
    
    sql = "INSERT INTO gym_classes (description, duration, available_slots, type) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [gym_class.description, gym_class.duration, gym_class.available_slots, gym_class.type]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

def select_all():
    
    gym_classes = []
    
    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)
    
    for row in results:
        gym_class = GymClass(row['description'], row['duration'], row['available_slots'], row['type'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def select(id):
    
    gym_class = None
    
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        gym_class = GymClass(result['description'], result['duration'], result['available_slots'], result['type'], result['id'])
    return gym_class

def delete_all():
    sql = "DELETE  FROM gym_classes"
    run_sql(sql)