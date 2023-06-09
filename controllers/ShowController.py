from ..models import Show, Screening
from .. controllers.ReservationController import delete as delete_reservation
from .. import db



def create(name, genre, duration, description, img):
    shw = Show(name, genre, duration, description, img)
    db.session.add(shw)
    db.session.commit()
    return True


def delete(id):
    show = Show.query.get(id)

    #  Delete all the screenings of the show
    for s in show.screenings:
        delete_screening(s.id)

    db.session.delete(show)
    db.session.commit()
    return True


def update(id, name, genre, duration, description,img):
    show = Show.query.get(id)
    show.name = name
    show.genre = genre
    show.duration = duration
    show.description = description
    show.img = img
    db.session.commit()
    return True


def get(id):
    # get show id as a parameter, find the show using query and return the show 
    shw = Show.query.get(id)
    Show.query.get(id)
    return shw


def get_all():
    return Show.query.all()


def get_reservations(id):
    shw = Show.query.get(id)
    return shw.reservations


def get_first(num):
    # get first "num" shows from the database and return them as a list
    shws = Show.query.order_by(Show.id).all()
    first_num = shws[:num]
    return first_num


def search(search_word):
    # search all the shows with names starting with "search"
    return Show.query.filter(Show.name.startswith(search_word)).all()


#screenings
def add_screening(show_id, datetime):
    screening = Screening(show_id, datetime)
    db.session.add(screening)
    db.session.commit()
    return True


def get_screening(screening_id):
    screening = Screening.query.get(screening_id)
    return screening


def get_all_screenings():
    return Screening.query.all()


def delete_screening(screening_id):
    screening = get_screening(screening_id)

    #  Delete all the reservations for the screening
    for r in screening.reservations:
        delete_reservation(r.id)

    db.session.delete(screening)
    db.session.commit()
    return True


def get_screenings(show_id):
    show = get(show_id)
    return show.screenings


def get_reserved_seats_ids(screening_id):
    screening = get_screening(screening_id)
    seat_ids = [res.seat_id for res in screening.reservations]
    return seat_ids