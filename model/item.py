from datetime import datetime

from database import db
from model import Base, Type, Currency, Gift, Salary, Service, Category


class Item(Base):
    type_id = db.Column(db.Integer, db.ForeignKey("type.id"), nullable=False)
    type = db.relationship("Type", backref=db.backref("items", lazy="dynamic"))

    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)

    currency_id = db.Column(db.Integer, db.ForeignKey("currency.id"), nullable=False)
    currency = db.relationship("Currency", backref=db.backref("items", lazy="dynamic"))

    description = db.Column(db.Text)

    gift_info_id = db.Column(db.Integer, db.ForeignKey("gift.id"))
    gift_info = db.relationship("Gift", backref=db.backref("items", lazy="dynamic"))

    salary_info_id = db.Column(db.Integer, db.ForeignKey("salary.id"))
    salary_info = db.relationship("Salary", backref=db.backref("items", lazy="dynamic"))

    service_info_id = db.Column(db.Integer, db.ForeignKey("service.id"))
    service_info = db.relationship("Service", backref=db.backref("items", lazy="dynamic"))

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category = db.relationship("Category", backref=db.backref("items", lazy="dynamic"))

    def __init__(self, type: Type, date: datetime, amount: float, currency: Currency,
                 description: str = None, gift_info: Gift = None, salary_info: Salary = None,
                 service_info: Service = None, category: Category = None):
        super().__init__()
        self.type = type
        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.gift_info = gift_info
        self.salary_info = salary_info
        self.service_info = service_info
        self.category = category
