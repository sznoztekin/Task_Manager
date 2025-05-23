from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_required, current_user
from app import db
from models import Task
from forms import TaskForm
import json

task_bp = Blueprint("task", __name__, url_prefix="/tasks")

@task_bp.route("/")
@login_required
def task_list():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template("tasks.html", tasks=tasks)

@task_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            user_id=current_user.id,
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data
        )
        db.session.add(task)
        db.session.commit()
        flash("Görev eklendi.")
        return redirect(url_for("task.task_list"))
    return render_template("add_task.html", form=form)

@task_bp.route("/update/<int:task_id>", methods=["GET", "POST"])
@login_required
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        return "Yetkisiz erişim", 403

    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.due_date = form.due_date.data
        db.session.commit()
        flash("Görev güncellendi.")
        return redirect(url_for("task.task_list"))
    return render_template("update_task.html", form=form)

@task_bp.route("/delete/<int:task_id>")
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        return "Yetkisiz erişim", 403
    db.session.delete(task)
    db.session.commit()
    flash("Görev silindi.")
    return redirect(url_for("task.task_list"))

@task_bp.route("/api")
@login_required
def tasks_api():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    task_list = [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "due_date": task.due_date.isoformat() if task.due_date else None,
            "status": task.status,
        }
        for task in tasks
    ]
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(task_list, f, ensure_ascii=False, indent=4)
    return jsonify(task_list)
