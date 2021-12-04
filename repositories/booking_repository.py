from db.run_sql import run_sql
from models.booking import Booking
from models.gym_class import GymClass
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

def save(booking):
    
    sql = "INSERT INTO bookings (member_id, gym_classes_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.gym_class.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

def select_all():
    
    bookings = []
    
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    
    for row in results:
        member = member_repository.select(row['member_id'])
        gym_class = gym_class_repository.select(row['gym_classes_id'])
        booking = Booking(member, gym_class, row['id'])
        bookings.append(booking)
    return bookings

def select(id):
    
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = (sql, values)[0]
    
    if result is not None:
        booking = Booking(result['member_id'], result['gym_class_id'], result['id'])
    return booking

def delete_all():
    sql = "DELETE  FROM bookings"
    run_sql(sql)