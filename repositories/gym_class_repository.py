from db.run_sql import run_sql
from models.gym_class import GymClass
from models.member import Member

def save(gym_class):
    
    sql = "INSERT INTO gym_classes (description, duration, available_slots, type, entry_fee) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [gym_class.description, gym_class.duration, gym_class.available_slots, gym_class.type, gym_class.entry_fee]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

def select_all():
    
    gym_classes = []
    
    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)
    
    for row in results:
        gym_class = GymClass(row['description'], row['duration'], row['available_slots'], row['type'], row['entry_fee'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def select(id):
    
    gym_class = None
    
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        gym_class = GymClass(result['description'], result['duration'], result['available_slots'], result['type'], result['entry_fee'], result['id'])
    return gym_class

def delete_all():
    sql = "DELETE  FROM gym_classes"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE  FROM gym_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def update(gym_class):
    sql = "UPDATE gym_classes SET (description, duration, available_slots, type) = (%s, %s, %s, %s) WHERE id = %s"
    values = [gym_class.description, gym_class.duration, gym_class.available_slots, gym_class.type, gym_class.entry_fee, gym_class.id]
    run_sql(sql, values)
    
def gym_classes(member):
    
    gym_classes = []
    
    sql = "SELECT gym_classes.* FROM gym_classes INNER JOIN bookings ON bookings.gym_classes_id = gym_classes.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)
    
    for row in results:
        gym_class = GymClass(row['description'], row['duration'], row['available_slots'], row['type'], row['entry_fee'], row['id'])
        gym_classes.append(gym_class)
        
    return gym_classes