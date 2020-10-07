from flask import render_template, redirect, url_for, flash
from ..models.course import Course
from .forms import AddCourse
from .. import db
from flask_login import current_user


def addCourse():
    if not current_user.is_authenticated:
        flash("You must be logged in to add course", 'danger')
        return redirect(url_for('courses_route'))
    form = AddCourse()
    if form.validate_on_submit():
        course = Course(name=form.name.data)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('courses_route'))
    return render_template('addcourse.html', form=form)


def showCourses():
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)


def showCoursePage(id):
    course = Course.query.filter_by(id=id).first()
    name = course.name
    resources = course.resources
    courseId = id
    return render_template('course.html', name=name, resources=resources, id=courseId)
