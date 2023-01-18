from turtle import title
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine(
    "mysql+mysqlconnector://root:24465336Kotiki@localhost:3306/to_do", echo=True)

Base = declarative_base()


class Topic(Base):
    __tablename__ = "topics"
    __table_args__ = {"schema": "to_do"}
    topic_id = Column(Integer, primary_key=True)
    title = Column(String(length=1000))
    description = Column(String(length=1000))

    def __repr__(self):
        return "<Topic(title'{0}', description ='{1}'>".format(self.title, self.description)


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {"schema": "to_do"}
    task_id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey('to_do.topic_id'))
    description = Column(String(length=1000))
    topic = relationship("Topic")

    def __repr__(self):
        return "<Task(description ='{0}'>".format(self.description)


Base.metadata.create_all(engine)
session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()
groceroes_topic = Topic(title="Groceries", description="buy vegetables")
session.add(groceroes_topic)
session.commit()
tasks = [Task(topic_id=groceroes_topic.topic_id,
              description="buy some basil & carrots")]
session.bulk_save_objects(tasks)
session.commit()

our_topic = session.query(Topic).filter_by(title="Groceries").first()
our_tasks = session.query(Task).all()
print(our_tasks)
