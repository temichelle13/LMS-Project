# app/utilities/notification_service.py

from datetime import datetime, timedelta
from models.assignment import Assignment
from database import SessionLocal

class NotificationService:
    def __init__(self):
        self.db_session = SessionLocal()

    def get_upcoming_due_dates(self, days_ahead=7):
        """Retrieves assignments due within the specified number of days ahead."""
        target_date = datetime.now() + timedelta(days=days_ahead)
        return self.db_session.query(Assignment).filter(Assignment.due_date <= target_date, Assignment.submitted == False).all()

    def send_due_date_notifications(self):
        """Sends notifications for assignments due within the next week."""
        upcoming_assignments = self.get_upcoming_due_dates()
        for assignment in upcoming_assignments:
            # Placeholder for sending the notification
            # This could be an email, SMS, or push notification
            print(f"Reminder: '{assignment.title}' is due by {assignment.due_date}.")
