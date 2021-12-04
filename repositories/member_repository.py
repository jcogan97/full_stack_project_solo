from db.run_sql import run_sql
from models.gym_class import GymClass
from models.member import Member

def save(member):
    sql = "INSERT INTO members (first_name, last_name, wallet) VALUES (%s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.wallet]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select_all():
    
    members = []
    
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['wallet'], row['id'])
        members.append(member)
    return members

def select(id):

    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['wallet'], result['id'])
    return member

def delete_all():
    sql = "DELETE  FROM members"
    run_sql(sql)
    
def update(member):
    sql = "UPDATE members SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.id]
    run_sql(sql, values)
    
def members(gym_class):
    
    members = []
    
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE gym_classes_id = %s"
    values = [gym_class.id]
    results = run_sql(sql, values)
    
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['wallet'], row['id'])
        members.append(member)
        
    return members