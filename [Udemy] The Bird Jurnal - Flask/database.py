from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import create_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "postgresql://postgres:24465336Kotiki@localhost:5432/birds")

Base = declarative_base()


class Bird(Base):
    __tablename__ = 'birds'
    bird_id = Column(Integer, primary_key=True)
    name = Column(String(length=255))

    def __repr__(self) -> str:
        return "<Bird(bird_id='{0}', name='{1}')>".format(self.bird_id, self.name)


class Feature(Base):
    __tablename__ = 'features'

    feature_id = Column(Integer, primary_key=True)
    bird_id = Column(Integer, ForeignKey('birds.bird_id'))
    feature = Column(String(length=400))

    bird = relationship('Bird')

    def __repr__(self):
        return "<Feature(feature='{0}'))>".format(self.feature)


Base.metadata.create_all(engine)


def create_session():
    session = sessionmaker(bind=engine)
    return session()


if __name__ == "__main__":
    session = create_session()

    first_bird = Bird(name="Owl")
    feature = Feature(
        feature="it has big eyes and a small tail. It hunts at night and sleep during a day", bird_id=first_bird.bird_id)
    session.add(first_bird, feature)
    session.commit()
