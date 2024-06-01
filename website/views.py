from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from .models import Notes
from . import db
import json
views = Blueprint('views', __name__)

@views.route("/home")
@login_required
def home():
	_notes = Notes.query.filter_by(user_id=current_user.id).all()
	return render_template("home.html", user=current_user, _notes=_notes)

@views.route("/save_note", methods=['POST'])
@login_required
def save_note():
	note = request.form.get("note")
	new_note = Notes(note=note, user_id=current_user.__dict__.get('id'))
	db.session.add(new_note)
	db.session.commit()
	flash("Note Saved")
	return redirect(url_for("views.home"))

@views.route("/delete_note", methods=['POST'])
@login_required
def delete_note():
	note = json.loads(request.data)
	note_id = note.get('note_id')
	_note = Notes.query.get(note_id)
	if _note:
		if _note.user_id == current_user.id:
			db.session.delete(_note)
			db.session.commit()
	return "Deleted"