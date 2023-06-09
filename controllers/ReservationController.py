from ..models import Reservation, Seat, Screening
from .. import db


### FUNCTIONS THAT INTERACT WITH OUR RESERVATION MODEL IN THE DATABASE ###

def create(user_id, screening_id, seat_id):
    reservation = Reservation(user_id, seat_id, screening_id)
    db.session.add(reservation)
    db.session.commit()
    return True


def delete(id):
    reservation = Reservation.query.get(id)
    db.session.delete(reservation)
    db.session.commit()
    return True


def update(id, user_id, seat_id, screening_id):
    reservation = Reservation.query.get(id)
    reservation.user_id = user_id
    reservation.seat_id = seat_id
    reservation.screening_id = screening_id
    db.session.commit()
    return True


def get(id):
    reservation = Reservation.query.get(id)
    return reservation


def get_all():
    return Reservation.query.all()


#  Useful when loading the user reservations page
def get_user_reservations(user_id):
    reservations = Reservation.query.filter_by(user_id=user_id)
    return reservations


def filter(day, month, year):
    data = {"normal_sold":0, "normal_value":0, "vip_sold":0, "vip_value":0}

    for r in Reservation.query.all():
        screening_date = Screening.query.get(r.screening_id).datetime

        if check_date(screening_date, day, month, year):
            seat = Seat.query.get(r.seat_id)
            if seat.vip:
                data["vip_sold"] += 1
                data["vip_value"] += seat.price
                continue 
            data["normal_sold"] += 1
            data["normal_value"] += seat.price

    return data


def check_date(d1, day, month, year):
    if year != 0:
        if not d1.year == year:
            return False
    if month != 0:
        if not d1.month == month:
            return False
    if day != 0:
        if not d1.day == day:
            return False
    return True
    ######################################################
'''def print(id, user_id, seat_id, screening_id):
    reservation = Reservation.query.get(id)
    reservation.user_id = user_id
    reservation.seat_id = seat_id
    reservation.screening_id = screening_id
    db.session.commit()
    return True'''