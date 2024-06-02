from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///interactions.db')
Session = sessionmaker(bind=engine)
session = Session()

class Interaction(Base):
    __tablename__ = 'interactions'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)

Base.metadata.create_all(engine)

def save_interaction(question, answer):
    interaction = Interaction(question=question, answer=answer)
    session.add(interaction)
    session.commit()
