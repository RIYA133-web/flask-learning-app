# from flask import Flask
# app=Flask(__name__)
# @app.route('/')
# def home():
#     return "hilo riggy!flask chl ryo hai"


# @app.route('/about')
# def about():
#      return "this is riggy flask journey"

# @app.route('/contact')
# def contact():
#      return "contact me at riyaRai@gmail.com"

# @app.route('/greet/<name>')
# def greet(name):
#      return f"Nameste,{name}!"
# @app.route('/square/<int:number>')
# def square(number):
#      return f"Square of {number} is {number*number}"

# if __name__=='__main__':
#       app.run(debug=True)
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/greet/<name>')
# def greet(name):
#     return render_template('index.html', name=name)
# @app.route('/skills')
# def skills():
#     skill_list = ['Python', 'Pandas', 'NumPy', 'Flask', 'SQL', 'Machine Learning']
#     return render_template('skills.html', skills=skill_list)

# if __name__ == '__main__':
#        app.run(debug=True)
# from flask import Flask, render_template, request
# app=Flask(__name__)
# @app.route('/form')
# def form():
#     return render_template('form.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     username = request.form['username']
#     skill = request.form['skill']
#     return f"Hi {username}! Nice to know you like {skill}."
# if __name__=='__main__':
#        app.run(debug=True)

# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), nullable=False)
#     skill = db.Column(db.String(100), nullable=False)

#     def __repr__(self):
#         return f"<User {self.username}>"


# @app.route('/form')
# def form():
#     return render_template('form.html')


# @app.route('/submit', methods=['POST'])
# def submit():
#     username = request.form['username']
#     skill = request.form['skill']

#     new_user = User(username=username, skill=skill)
#     db.session.add(new_user)
#     db.session.commit()

#     return f"Hi {username}! Your skill '{skill}' has been saved to the database."


# @app.route('/users')
# def show_users():
#     all_users = User.query.all()
#     return render_template('users.html', users=all_users)
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'riiggy123secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    skill = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    skill = request.form['skill']

    new_user = User(username=username, skill=skill)
    db.session.add(new_user)
    db.session.commit()

    flash(f"{username}'s details saved successfully!")
    return redirect('/users')


@app.route('/users')
def show_users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)


@app.route('/edit/<int:user_id>')
def edit_user(user_id):
    selected_user = User.query.get(user_id)
    return render_template('edit.html', user=selected_user)


@app.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    selected_user = User.query.get(user_id)
    selected_user.username = request.form['username']
    selected_user.skill = request.form['skill']
    db.session.commit()
    return redirect('/users')


@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    selected_user = User.query.get(user_id)
    db.session.delete(selected_user)
    db.session.commit()
    flash(f"{selected_user.username}'s entry deleted successfully!")
    return redirect('/users')


if __name__ == '__main__':
    app.run(debug=True)