from db.run_sql import run_sql
from models.gym_class import GymClass
from models.membership import Membership

def save(membership):
    sql = "INSERT INTO memberships (type, cost, free_classes) VALUES (%s, %s, %s) RETURNING id"
    values = [membership.type, membership.cost, membership.free_classes]
    results = run_sql(sql, values)
    membership.id = results[0]['id']
    return membership

def select_all():
    
    memberships = []
    
    sql = "SELECT * FROM memberships"
    results = run_sql(sql)
    
    for row in results:
        membership = Membership(row['type'], row['cost'], row['free_classes'], row['id'])
        memberships.append(membership)
    return memberships

def select(id):

    membership = None
    sql = "SELECT * FROM memberships WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        membership = Membership(result['type'], result['cost'], result['free_classes'], result['id'])
    return membership

def delete_all():
    sql = "DELETE  FROM memberships"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE  FROM memberships WHERE id = %s"
    values = [id]
    run_sql(sql, values)