from flask import Flask, render_template, request, redirect, url_for
from learning_dashboard.models import init_db, Course

app = Flask(__name__)

@app.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

# Additional routes for adding courses, assignments, etc. will go here

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
from flask import request
from learning_dashboard.models import db, Course

# Route for handling the form submission
@app.route('/add_course', methods=['POST'])
def add_course():
    title = request.form['title']
    description = request.form['description']
    # Handle additional fields here
    
    new_course = Course(title=title, description=description)
    db.session.add(new_course)
    db.session.commit()
    
    return redirect(url_for('index'))
from learning_dashboard.models import Assignment
# Assuming Assignment model exists in models.py

@app.route('/add_assignment', methods=['POST'])
def add_assignment():
    course_id = request.form['course_id']
    title = request.form['title']
    due_date = request.form['due_date']
    # Handle additional fields here
    
    new_assignment = Assignment(course_id=course_id, title=title, due_date=due_date)
    db.session.add(new_assignment)
    db.session.commit()
    
    return redirect(url_for('index'))
@app.route('/course/<int:course_id>')
def course_details(course_id):
    course = Course.query.get_or_404(course_id)
    # Assuming you have a relationship set up to fetch assignments for the course
    return render_template('course_details.html', course=course)
@app.route('/delete_course/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for('index'))
@app.route('/analytics')
def show_analytics():
    # Example: Fetch and calculate analytics data
    average_study_time = calculate_average_study_time()
    courses_completed = count_courses_completed()
    average_grade = calculate_average_grade()
    
    return render_template('analytics.html', average_study_time=average_study_time, courses_completed=courses_completed, average_grade=average_grade)
@app.route('/notifications')
def show_notifications():
    notifications = fetch_unread_notifications()
    return render_template('notifications.html', notifications=notifications)
