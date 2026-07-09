from flask import Blueprint, render_template, request, redirect, flash
from models import db, User

users_bp = Blueprint('users_bp', __name__)


@users_bp.route('/form')
def form():
    return render_template('form.html')


@users_bp.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    skill = request.form['skill']
    new_user = User(username=username, skill=skill)
    db.session.add(new_user)
    db.session.commit()
    flash(f"{username}'s details saved successfully!")
    return redirect('/users')


@users_bp.route('/users')
def show_users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)


@users_bp.route('/edit/<int:user_id>')
def edit_user(user_id):
    selected_user = User.query.get(user_id)
    return render_template('edit.html', user=selected_user)


@users_bp.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    selected_user = User.query.get(user_id)
    selected_user.username = request.form['username']
    selected_user.skill = request.form['skill']
    db.session.commit()
    flash(f"{selected_user.username}'s details updated successfully!")
    return redirect('/users')


@users_bp.route('/delete/<int:user_id>')
def delete_user(user_id):
    selected_user = User.query.get(user_id)
    db.session.delete(selected_user)
    db.session.commit()
    flash(f"{selected_user.username}'s entry deleted successfully!")
    return redirect('/users')