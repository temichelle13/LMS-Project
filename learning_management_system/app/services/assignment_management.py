# app/services/assignment_management.py

from models.assignment import Assignment
from database import SessionLocal

class AssignmentManagementService:
    def __init__(self):
        self.db_session = SessionLocal()
    
    def add_assignment(self, title, description, due_date, course_id):
        """Adds a new assignment."""
        assignment = Assignment(
            title=title,
            description=description,
            due_date=due_date,
            course_id=course_id
        )
        self.db_session.add(assignment)
        self.db_session.commit()
        return assignment
    
    def mark_as_submitted(self, assignment_id):
        """Marks an assignment as submitted."""
        self.db_session.query(Assignment).filter(Assignment.id == assignment_id).update({"submitted": True})
        self.db_session.commit()
    
    def update_assignment(self, assignment_id, **kwargs):
        """Updates assignment details."""
        self.db_session.query(Assignment).filter(Assignment.id == assignment_id).update(kwargs)
        self.db_session.commit()
    
    def get_course_assignments(self, course_id):
        """Retrieves all assignments for a course."""
        return self.db_session.query(Assignment).filter(Assignment.course_id == course_id).all()
