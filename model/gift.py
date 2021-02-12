from database import db
from model import Base


class Gift(Base):
    recipient = db.Column(db.Text, nullable=False)
    event = db.Column(db.Text, nullable=False)

    def __init__(self, recipient: str, event: str):
        super().__init__()
        self.recipient = recipient
        self.event = event
