from models import member
from models import booking
from models.member      import Member
from models.gym_class   import GymClass
from models.booking     import Booking

import repositories.member_repository       as member_repository
import repositories.gym_class_repository    as gym_class_repository
import repositories.booking_repository      as booking_repository

member_repository.delete_all()
gym_class_repository.delete_all()
booking_repository.delete_all()

member_1 = Member("Henry", "Cavill", 20)
member_repository.save(member_1)

member_2 = Member("Jack", "Cogan", 1)
member_repository.save(member_2)

member_3 = Member("Tristan", "McDonald", 8)
member_repository.save(member_3)

class_1 = GymClass("Cycling", 30, 3, "Cardio")
gym_class_repository.save(class_1)

class_2 = GymClass("Yoga", 60, 2, "Body & Mind")
gym_class_repository.save(class_2)

class_3 = GymClass("Strength", 30, 5, "Functional")
gym_class_repository.save(class_3)

booking_1 = Booking(member_1, class_1)
booking_repository.save(booking_1)

booking_2 = Booking(member_1, class_3)
booking_repository.save(booking_2)

booking_3 = Booking(member_2, class_1)
booking_repository.save(booking_3)

booking_4 = Booking(member_3, class_2)
booking_repository.save(booking_4)