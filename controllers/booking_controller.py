from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route('/bookings')
def bookings():
    
    members = member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    bookings = booking_repository.select_all()
    
    return render_template("bookings/index.html", bookings=bookings, members=members, gym_classes=gym_classes)

@bookings_blueprint.route('/bookings', methods=['POST'])
def new_booking():
    
    member_id = request.form['member_id']
    gym_class_id = request.form['gym_class_id']
    
    member = member_repository.select(member_id)
    gym_class = gym_class_repository.select(gym_class_id)
    
    new_booking = Booking(member, gym_class)
    
    booking_repository.save(new_booking)
    
    return redirect('/bookings')