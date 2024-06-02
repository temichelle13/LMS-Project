# app/models/course.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.sql import func

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    platform = Column(String)  # Platform where the course is taken (e.g., Coursera, edX)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="courses")
    
    # You can add more fields as necessary, such as progress, grades, etc.
