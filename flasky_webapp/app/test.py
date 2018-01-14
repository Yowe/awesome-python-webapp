from .models import User
from . import db


u = User(email='john@example.com',username='john',password='cat')
db.session.add(u)
db.session.commit()