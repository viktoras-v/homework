from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Set up the database engine
engine = create_engine("sqlite:///mydatabase.db")
Base = declarative_base()


# Define a User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', age={self.age})>"


# Create table
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# -------------------------
# Add data
user1 = User(name="Alice", age=25)
user2 = User(name="Bob", age=30)

session.add(user1)
session.add(user2)

# Commit
session.commit()

# -------------------------
# Read data
print("All users in the database:")
users = session.query(User).all()
for user in users:
    print(user)

# -------------------------
# Modify data
alice = session.query(User).filter_by(name="Alice").first()
alice.age = 26
session.commit()

# -------------------------
# 9️⃣ Delete data
# Delete Bob
bob = session.query(User).filter_by(name="Bob").first()
if bob:
    session.delete(bob)
    session.commit()

# -------------------------
# 10️⃣ Retrieve data after changes
print("\nUsers after modifications:")
users = session.query(User).all()
for user in users:
    print(user)

# Close the session
session.close()
