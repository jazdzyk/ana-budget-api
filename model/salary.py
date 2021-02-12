from database import db
from model import Base


class Salary(Base):
    year = db.Column(db.SmallInteger, nullable=False)
    month = db.Column(db.SmallInteger, nullable=False)
    company = db.Column(db.Text, nullable=False)
    contract = db.Column(db.String(30), nullable=False)

    def __init__(self, year: int, month: int, company: str, contract: str):
        super().__init__()
        self.year = year
        self.month = month
        self.company = company
        self.contract = contract
