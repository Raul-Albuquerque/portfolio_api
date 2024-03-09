from flask import Flask, jsonify

app = Flask(__name__)

livros = [
  {
    'id': 1,
    'titulo': 'O Senhor dos Aneis -  A Sociedade do Anel',
    'autor': 'J.R.R. Tolkien'
  },
  {
    'id': 2,
    'titulo': 'Harry Potter e a Pedra Filosofal',
    'autor': 'J.K. Howling'
  },
  {
    'id': 3,
    'titulo': 'Habitos Atomicos',
    'autor': 'James Clear'
  },
]

# Consultar(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

if __name__ == '__main__':
  app.run(debug=True)