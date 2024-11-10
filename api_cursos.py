from flask import Flask, request, jsonify
import db 
import banco

app = Flask(__name__)

@app.route("/cursos", methods=["GET"])
def recupera_todos_cursos():
    return jsonify(db.cursos), 200

@app.route("/cursos/oracle", methods=["GET"])
def recupera_todos_oracle():
    dados = banco.consulta_todos()
    if len(dados) > 0:
        return jsonify(dados), 200
    else:
        return jsonify({"title": "Nenhum curso na base", "status": 404}), 404

@app.route("/cursos/<int:id>", methods=["GET"])
def recupera_curso_id(id):
    for curso in db.cursos:
        if curso['id'] == id:
            return jsonify(curso), 200
    return jsonify({"msg": "Curso não encontrado", "status": 404}), 404

@app.route("/cursos/oracle", methods=["POST"])
def insere_oracle():
    curso = request.json
    banco.insere(curso)
    return jsonify(curso), 200

@app.route("/cursos", methods=["POST"])
def insere():
    curso = request.json
    
    for c in db.cursos:
        if c['id'] == curso['id'] or c['titulo'] == curso['titulo']:
            return jsonify({"msg": "Curso já cadastrado", "status": 406}), 406
    
    db.cursos.append(curso)
    return jsonify(curso), 201

@app.route("/cursos", methods=["PUT"])
def altera():
    curso = request.json
    for i in range(len(db.cursos)):
        info = db.cursos[i]
        if info['id'] == curso['id']:
            db.cursos[i] = curso
            return jsonify(curso), 200
    
    return jsonify({'msg': 'Curso não encontrado', 'status': 404}), 404

@app.route("/cursos/<int:id>", methods=["DELETE"])
def exclui(id):
    for i in range(len(db.cursos)):
        if db.cursos[i]['id'] == id:
            del db.cursos[i]
            return jsonify({"msg": "Curso excluído com sucesso"}), 200
    
    return jsonify({"msg": "Curso não encontrado", "status": 404}), 404

if __name__ == "__main__":
    app.run(debug=True)
