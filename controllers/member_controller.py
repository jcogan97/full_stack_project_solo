from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from controllers.gym_class_controller import gym_classes
from models.member import Member
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

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
    new_member = Member(first_name, last_name)
    
    member_repository.save(new_member)
    return redirect(url_for(".members"))