
Flask Notes App
This is a simple notes app built using Flask, a micro web framework for Python. The app allows users to create, view, and delete notes.

Features
Home Page
The home page displays a list of notes created by the current user. The notes are retrieved from the database using the Notes model.

Creating Notes
Users can create new notes by submitting a form on the home page. The note is saved to the database using the save_note function.

Deleting Notes
Users can delete notes by sending a POST request to the delete_note endpoint with the note ID. The note is deleted from the database if it belongs to the current user.

Code Overview
views.py
This file contains the Flask views for the app.

home function
Retrieves a list of notes for the current user using the Notes model.
Renders the home.html template with the notes and current user.
save_note function
Retrieves the note text from the form submission.
Creates a new Notes object with the note text and current user ID.
Saves the note to the database using db.session.add and db.session.commit.
Flashes a success message and redirects to the home page.
delete_note function
Retrieves the note ID from the JSON data in the request.
Retrieves the note object from the database using Notes.query.get.
Checks if the note belongs to the current user.
Deletes the note from the database using db.session.delete and db.session.commit.
Returns a success message.
models.py
This file contains the Notes model, which represents a note in the database.

templates/home.html
This file contains the HTML template for the home page, which displays a list of notes and a form to create new notes.

app.py
This file contains the Flask app instance and configuration.

Requirements
Flask
Flask-Login
Flask-SQLAlchemy
Setup
Install the required packages using pip install -r requirements.txt.
Create a database and update the SQLALCHEMY_DATABASE_URI configuration in app.py.
Run the app using python app.py.
Access the app at http://localhost:5000/home.# first_flask_app
