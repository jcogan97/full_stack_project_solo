import pdb

from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.booking import Booking
from models.member import Member
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
    
    if member.payment(gym_class.entry_fee) == False:
        
        return redirect('/bookings/payment_error')
    else:
        member.decrease_remaining_classes()
    
        new_booking = Booking(member, gym_class)
        booking_repository.save(new_booking)

        # print(gym_class.entry_fee)
        member_repository.update(member)
        # pdb.set_trace()
        return redirect('/bookings')

@bookings_blueprint.route('/bookings/payment_error')
def member_cannot_pay():
    return render_template('bookings/payment_error.html')

@bookings_blueprint.route('/bookings/<id>/delete', methods=['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect(url_for('.bookings'))