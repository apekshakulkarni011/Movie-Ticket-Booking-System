from ..settings import db
from ..models import Seat

def generate_seats():
    a = {"K": 14, "J": 14, "I": 14, "H": 14, "G": 14, "F": 8,"E": 14, "D": 14, "C": 14, "B": 14,"A": 8}
    for letter, num in a.items():
        for i in range(1, num+1):
            position = letter + str(i)
            vip = False
            price = 110.0
            if letter in ["F", "A"] and i in [3, 4, 5, 6]:
                vip = True
                price = 160.0
            seat = Seat(position, vip, price)
            db.session.add(seat)
    db.session.commit()


def get_all():
    return Seat.query.all()


def get(id):
    return Seat.query.get(id)


def get_by_position(pos):
    seat = Seat.query.filter_by(position=pos).first()
    if seat:
        return seat
    return None