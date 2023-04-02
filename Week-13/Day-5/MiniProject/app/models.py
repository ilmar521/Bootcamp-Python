from app import flask_app, db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    details = db.Column(db.Text)
    completed = db.Column(db.Boolean)

    def save_task_to_db(self):
        with flask_app.app_context():
            db.session.add(self)
            db.session.commit()

    def set_task_as_complete(self):
        with flask_app.app_context():
            self.completed = not self.completed
            current_db_sessions = db.session.object_session(self)
            current_db_sessions.add(self)
            current_db_sessions.commit()

