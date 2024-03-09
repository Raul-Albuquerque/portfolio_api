from flask import Flask, jsonify

app = Flask(__name__)

from api.mock_data.about import about

@app.route('/about', methods=['GET'])
def get_about():
    return jsonify(about)


if __name__ == '__main__':
  app.run(debug=True)