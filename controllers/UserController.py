from ..models import User
from .. import db
from .. import logged_in_user



def create(name, email):
    user = User(name, email)
    db.session.add(user)
    db.session.commit()
    return True


def email_exists(email):
    email = User.query.filter_by(email=email).first()
    if email:
        return True
    return False


def name_exists(name):
    name = User.query.filter_by(name=name).first()
    if name:
        return True
    return False


def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return True


def update(new_name, new_email, id):
    user = User.query.get(id)
    user.name = new_name
    user.email = new_email
    db.session.commit()
    return True


def get(id):
    user =  User.query.get(id)
    return user


def get_all():
    user = User.query.all()
    return user


def login(name, email):
    user = User.query.filter_by(name=name, email=email).first()
    if user:
        global logged_in_user 
        logged_in_user = user
        return True
    return False


def logout():
    global logged_in_user 
    logged_in_user = None


def get_logged_in_user():
    return logged_in_user