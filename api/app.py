import json
from flask import Flask, jsonify, Response

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

from api.mock_data.about import about
from api.mock_data.contacts import contacts
from api.mock_data.courses import courses
from api.mock_data.projects import projects

@app.route('/about', methods=['GET'])
def get_about():
    response_data = json.dumps(about, ensure_ascii=False).encode('utf8')
    return Response(response=response_data, status=200, mimetype='application/json')

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)

@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(projects)


if __name__ == '__main__':
    app.run(debug=True)