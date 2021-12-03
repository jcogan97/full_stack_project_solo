from db.run_sql import run_sql
from models.gym_class import GymClass
from models.member import Member

def save(member):
    sql = "INSERT INTO members (full_name, wallet) VALUES (%s, %s) RETURNING id"
    values = [member.full_name]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

