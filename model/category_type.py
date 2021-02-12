from database import db
from model import Base


class CategoryType(Base):
    name = db.Column(db.Text, nullable=False, unique=True)

    def __init__(self, name: str):
        super().__init__()
        self.name = name
