from database import db
from model import Base


class Type(Base):
    name = db.Column(db.String(15), nullable=False, unique=True)

    def __init__(self, name: str):
        super().__init__()
        self.name = name
