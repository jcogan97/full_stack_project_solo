from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.gym_class import GymClass
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

@gym_classes_blueprint.route('/classes')
def gym_classes():
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/index.html", gym_classes=gym_classes)

@gym_classes_blueprint.route('/classes/<id>')
def show_gym_class(id):
    gym_class = gym_class_repository.select(id)
    members = member_repository.members(gym_class)
    return render_template("gym_classes/show.html", gym_class=gym_class, members=members)

@gym_classes_blueprint.route('/classes/new')
def new_class():
    return render_template('gym_classes/new.html')

@gym_classes_blueprint.route('/classes', methods=['POST'])
def register_class():
    description = request.form['description']
    duration = request.form['duration']
    available_slots = request.form['available_slots']
    type = request.form['type']
    new_class = GymClass(description, duration, available_slots, type)
    
    gym_class_repository.save(new_class)
    return redirect('/classes')

@gym_classes_blueprint.route('/classes/<id>/edit')
def edit_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template('gym_classes/edit.html', gym_class=gym_class)

@gym_classes_blueprint.route('/classes/<id>', methods=['POST'])
def update_class(id):
    description = request.form['description']
    duration = request.form['duration']
    available_slots = request.form['available_slots']
    type = request.form['type']
    sel_class = gym_class_repository.select(id)
    updated_class = GymClass(description, duration, available_slots, type, sel_class.id)
    
    gym_class_repository.update(updated_class)
    return redirect(f'/classes/{id}')