# app/models/assignment.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.sql import func

class Assignment(Base):
    __tablename__ = 'assignments'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    due_date = Column(DateTime)
    submitted = Column(Boolean, default=False)
    grade = Column(String, nullable=True)  # Optional: For tracking grades on assignments
    course_id = Column(Integer, ForeignKey('courses.id'))
    
    course = relationship("Course", back_populates="assignments")
    
    # Additional fields might include file attachments, submission links, feedback, etc.
