from flask import Flask, jsonify

from mock_data.about import about
from mock_data.contacts import contacts
from mock_data.courses import courses
from mock_data.projects import projects

app = Flask(__name__)

@app.route('/about')
def get_about():
  return jsonify(about)

@app.route('/contacts')
def get_contacts():
  return jsonify(contacts)

@app.route('/courses')
def get_courses():
  return jsonify(courses)

@app.route('/projects')
def get_projects():
  return jsonify(projects)

if __name__ == '__main__':
  app.run(debug=True)