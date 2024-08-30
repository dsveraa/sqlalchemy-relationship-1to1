from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = relationship("Address", back_populates="user", uselist=False) # 'uselist=False' means that this is a 1 to 1 relationship
    
class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="address")
    
Base.metadata.create_all(engine)
    
""" 
# adding new data with 1 to 1 relationship
new_user = User(name='David Vera')
new_address = Address(email='davidvera@gmail.com', user=new_user)
session.add(new_user)
session.add(new_address)
session.commit()

print(f'new_user.name = {new_user.name}')
print(f'new_address.email = {new_address.email}')
print(f'new_user.address.email = {new_user.address.email}')
print(f'new_address.user.name = {new_address.user.name}')
"""

# query to check if the relationship has done
user = session.query(User).filter_by(name='David Vera').first()
print(f'User: {user.name}, Address: {user.address.email}')