from sqlalchemy import Column, Integer, String, ForeignKey

from app.core.database import Base


class Video(Base):

    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    filepath = Column(String)

    duration = Column(Integer)

  user_id = Column(Integer, ForeignKey("users.id"))
