from db.run_sql import run_sql
from models.booking import Booking
from models.gym_class import GymClass
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, gym_classes_id) VALUES (%s, %s) RETURNING *"
    values = [booking.member.id, booking.gym_classes.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking