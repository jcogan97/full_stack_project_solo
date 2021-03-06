import pdb
from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from controllers.gym_class_controller import gym_classes
from models.member import Member
from console import membership_1
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.membership_repository as membership_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route('/members')
def members():
    members = member_repository.select_all()
    return render_template("/members/index.html", members=members)

@members_blueprint.route('/members/<id>')
def show_classes(id):
    member = member_repository.select(id)
    gym_classes = gym_class_repository.gym_classes(member)
    return render_template('members/show.html', gym_classes=gym_classes, member=member, membership=member.membership)

@members_blueprint.route('/members/register')
def new_member():
    return render_template('members/new.html')

@members_blueprint.route('/members', methods=['POST'])
def register_member():
    # pdb.set_trace()
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership_id = request.form['membership']
    membership = membership_repository.select(membership_id)
    new_member = Member(first_name, last_name, membership)
    member_repository.save(new_member)
    return redirect(url_for(".members"))

@members_blueprint.route('/members/<id>/edit')
def edit_member(id):
    member = member_repository.select(id)
    memberships = membership_repository.select_all()
    return render_template('members/edit.html', member=member, memberships=memberships)

@members_blueprint.route('/members/<id>', methods=['POST'])
def update_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    wallet = request.form['wallet']
    # print(membership)
    
    member = member_repository.select(id)
    
    # pdb.set_trace()
    member.first_name = first_name
    member.last_name = last_name
    member.wallet = wallet
    
    member_repository.update(member)
    return redirect(url_for('.members'))

@members_blueprint.route('/members/<id>/delete', methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect(url_for(".members"))

@members_blueprint.route('/members/<id>/upgrade')
def upgrade_member_membership(id):
    member = member_repository.select(id)
    memberships = membership_repository.select_all()
    return render_template('/members/upgrade.html', member=member, memberships=memberships)

@members_blueprint.route('/members/<id>/upgrade', methods=['POST'])
def user_selected_membership(id):
    membership_id = request.form['membership_id']
    membership = membership_repository.select(membership_id)
    member = member_repository.select(id)
    if member.sufficient_funds(membership.cost) == False:
        return redirect('/bookings/payment_error')
    else:
        member.payment(membership.cost)
        member.set_membership(membership)
        # edited_member = Member(member.first_name, member.last_name, membership, member.wallet, member.id)
        member_repository.update(member)
        return redirect(f'/members/{id}')