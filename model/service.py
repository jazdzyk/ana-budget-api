from datetime import datetime

from database import db
from model import Base


class Service(Base):
    order_date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    actual_time = db.Column(db.Numeric(10, 2))
    delivery_date = db.Column(db.Date)

    def __init__(self, order_date: datetime, price: float, actual_time: float = None, delivery_date: datetime = None):
        super().__init__()
        self.order_date = order_date
        self.price = price
        self.actual_time = actual_time
        self.delivery_date = delivery_date
