from datetime import datetime

from database import db


class Base(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    created = db.Column(db.DateTime, nullable=False)
    last_modified = db.Column(db.DateTime, nullable=False)
    modified_count = db.Column(db.Integer, nullable=False)
    modified_note = db.Column(db.Text, nullable=False)

    def __init__(self):
        now = datetime.now()
        self.created = now
        self.last_modified = now
        self.modified_count = 0
        self.modified_note = ""

    def __repr__(self):
        return f"<{type(self).__name__} {self._format_attribute_names()}>"

    def on_modify(self, note: str):
        self.last_modified = datetime.now()
        self.modified_count += 1
        self.modified_note += f"{note};"

    def _format_attribute_names(self):
        attributes = [f"{attr}={getattr(self, attr)}" for attr in dir(self) if not attr.startswith("__")]
        return " ".join(attributes)
