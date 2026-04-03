from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Subscription(Base):

    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    price = Column(Integer)

    video_limit = Column(Integer)

    platforms = Column(Integer)
