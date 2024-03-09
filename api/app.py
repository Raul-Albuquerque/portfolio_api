from flask import Flask, jsonify

app = Flask(__name__)

from api.mock_data.about import about
from api.mock_data.contacts import contacts
from api.mock_data.courses import courses
from api.mock_data.projects import projects

@app.route('/about', methods=['GET'])
def get_about():
    return jsonify(about)

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
  import sys
  sys.setdefaultencoding('utf-8')
  app.run(debug=True)