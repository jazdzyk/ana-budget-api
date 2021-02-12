from database import db
from model import Base


class Currency(Base):
    iso_name = db.Column(db.String(3), nullable=False, unique=True)
    symbol = db.Column(db.String(10))

    def __init__(self, iso_name: str, symbol: str = None):
        super().__init__()
        self.iso_name = iso_name
        self.symbol = symbol
