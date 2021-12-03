from db.run_sql import run_sql
from models.gym_class import GymClass
from models.member import Member

def save(member):
    sql = "INSERT INTO members (full_name, wallet) VALUES (%s, %s) RETURNING id"
    values = [member.full_name]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select_all():
    
    members = []
    
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    
    for row in results:
        member = Member(row['full_name'], row['wallet'], row['id'])
        members.append(member)
    return members

def select(id):

    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        member = Member(result['full_name'], result['wallet'], result['id'])
    return member

def delete_all():
    sql = "DELETE  FROM members"
    run_sql(sql)