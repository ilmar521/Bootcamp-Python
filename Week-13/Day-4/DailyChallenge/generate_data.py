import faker
from app import flask_app, db
from app.models import Person, Phonenumber

fake = faker.Faker()

# def populate():
#     with flask_app.app_context():
#         filename = os.path.join(flask_app.static_folder, 'users.json')
#         with open(filename, 'r') as f:
#             data = json.load(f)
#             for user in data:
#                 user_inst = models.User(id=user['id'], name=user['name'], street=user['address']['street'], city=user['address']['city'], zipcode=user['address']['zipcode'])
#                 db.session.add(user_inst)
#                 db.session.commit()
#
#
# populate()