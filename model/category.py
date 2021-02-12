from database import db
from model import Base, CategoryType


class Category(Base):
    name = db.Column(db.Text, nullable=False, unique=True)

    type_id = db.Column(db.Integer, db.ForeignKey("categorytype.id"))
    type = db.relationship("CategoryType", backref=db.backref("categories", lazy="dynamic"))

    def __init__(self, name: str, type: CategoryType = None):
        super().__init__()
        self.name = name
        self.type = type
