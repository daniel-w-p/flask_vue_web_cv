from .db_init import DB

db = DB.get()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username} ({self.email})>'

    def __init__(self, username, password, email):
        super().__init__(self)
        self.username = username
        self.password = password
        self.email = email
