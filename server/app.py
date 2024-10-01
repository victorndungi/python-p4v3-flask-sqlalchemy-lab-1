# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)


# View to get earthquake by id
@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake(id):
    # Query the earthquake using db.session inside the request context
    earthquake = db.session.get(Earthquake, id)

    if earthquake:
        # If found, return the earthquake's attributes in JSON format
        return make_response(jsonify({
            'id': earthquake.id,
            'magnitude': earthquake.magnitude,
            'location': earthquake.location,
            'year': earthquake.year
        }), 200)
    else:
        # If not found, return a 404 error with a message
        return make_response(jsonify({'message': f'Earthquake {id} not found.'}), 404)




@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    earthquakes = db.session.query(Earthquake).filter(Earthquake.magnitude >= magnitude).all()

    earthquake_data=[
        {
            'id': eq.id,
            'magnitude': eq.magnitude,
            'location':eq.location,
            'year':eq.year
            
        }for eq in earthquakes
    ]

    response = {
        'count': len(earthquake_data),
        'quakes': earthquake_data
    }

    return make_response(jsonify(response),200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)