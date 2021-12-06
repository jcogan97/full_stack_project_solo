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
    return render_template('members/show.html', gym_classes=gym_classes, member=member)

@members_blueprint.route('/members/register')
def new_member():
    return render_template('members/new.html')

@members_blueprint.route('/members', methods=['POST'])
def register_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    new_member = Member(first_name, last_name, membership_1)
    
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
    membership = membership_repository.select(member.membership.id)
    # pdb.set_trace()
    edit_member = Member(first_name, last_name, membership, wallet, id)
    
    member_repository.update(edit_member)
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

