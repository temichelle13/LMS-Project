# app/services/analytics.py

from models.course import Course
from models.assignment import Assignment
from sqlalchemy import func
from database import SessionLocal

class AnalyticsService:
    def __init__(self):
        self.db_session = SessionLocal()
    
    def course_completion_rate(self, user_id):
        """Calculates the percentage of completed courses."""
        total_courses = self.db_session.query(Course).filter(Course.user_id == user_id).count()
        completed_courses = self.db_session.query(Course).filter(Course.user_id == user_id, Course.end_date < func.now()).count()
        return (completed_courses / total_courses) * 100 if total_courses > 0 else 0

    def assignment_completion_rate(self, user_id):
        """Calculates the percentage of assignments submitted."""
        total_assignments = self.db_session.query(Assignment).join(Course).filter(Course.user_id == user_id).count()
        submitted_assignments = self.db_session.query(Assignment).join(Course).filter(Course.user_id == user_id, Assignment.submitted == True).count()
        return (submitted_assignments / total_assignments) * 100 if total_assignments > 0 else 0

    def average_grade(self, user_id):
        """Calculates the average grade of submitted assignments."""
        # Placeholder: Implement based on your grading system
        pass

    def study_time_insights(self, user_id):
        """Generates insights on study time based on assignment completion and course duration."""
        # Placeholder: Implement logic to track and analyze study time
        pass
