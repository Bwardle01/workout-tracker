from app.models import User
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


db = Session()

# insert users
db.add_all([
  User(username='Bronson', email='bronson@cbc.ca', password='bronson123'),
])

db.commit()

db.close()