from flask import Flask, jsonify, request 

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Os segredos da mente milionária',
        'autor': 'T. Harv Eker'
    },
    {
        'id': 2,
        'titulo': 'As 48 leis do poder',
        'autor': 'Robert Greene'
    },
    {
        'id': 3,
        'titulo': 'Destravar da Inteligência Emocional',
        'autor': 'Pablo Marçal'
    },
]

@app.route('/livros')
def getBooks():
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)