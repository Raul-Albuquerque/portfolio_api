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
    response_data = json.dumps(contacts, ensure_ascii=False).encode('utf8')
    return Response(response=response_data, status=200, mimetype='application/json')

@app.route('/courses', methods=['GET'])
def get_courses():
    response_data = json.dumps(courses, ensure_ascii=False).encode('utf8')
    return Response(response=response_data, status=200, mimetype='application/json')

@app.route('/projects', methods=['GET'])
def get_projects():
    response_data = json.dumps(projects, ensure_ascii=False).encode('utf8')
    return Response(response=response_data, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)