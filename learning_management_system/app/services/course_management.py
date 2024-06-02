# app/services/course_management.py

from models.course import Course
from database import SessionLocal

class CourseManagementService:
    def __init__(self):
        self.db_session = SessionLocal()
    
    def add_course(self, title, description, platform, start_date, end_date, user_id):
        """Adds a new course."""
        course = Course(
            title=title,
            description=description,
            platform=platform,
            start_date=start_date,
            end_date=end_date,
            user_id=user_id
        )
        self.db_session.add(course)
        self.db_session.commit()
        return course
    
    def update_course(self, course_id, **kwargs):
        """Updates course details."""
        self.db_session.query(Course).filter(Course.id == course_id).update(kwargs)
        self.db_session.commit()
    
    def get_user_courses(self, user_id):
        """Retrieves all courses for a user."""
        return self.db_session.query(Course).filter(Course.user_id == user_id).all()
