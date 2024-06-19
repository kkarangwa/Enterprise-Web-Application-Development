from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm, ScheduleCollectionForm
from app.models import User, WasteCollection

@app.route('/')
def index():
    return render_template('index.html')

# ... other routes for login, registration, scheduling, tracking, admin dashboard, etc.

@app.route('/schedule', methods=['GET', 'POST'])
@login_required
def schedule():
    form = ScheduleCollectionForm()
    if form.validate_on_submit():
        collection = WasteCollection(user_id=current_user.id, scheduled_date=form.scheduled_date.data, status='Pending')
        db.session.add(collection)
        db.session.commit()
        flash('Waste collection scheduled successfully!')
        return redirect(url_for('schedule'))
    return render_template('schedule.html', form=form)
