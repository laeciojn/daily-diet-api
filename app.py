from flask import Flask, request, jsonify
from database import db
from model.refeicao import Refeicao
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") #chave
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL") #caminho do banco

db.init_app(app)
@app.route("/refeicao", methods=["POST"])
def criar_refeicao():
    data = request.json

    nome = data.get("nome")
    descricao = data.get("descricao")
    dentroDaDieta = data.get("dentroDaDieta")

    if nome and descricao and dentroDaDieta is not None:
            ref = Refeicao(nome=nome, descricao=descricao, dentroDaDieta=dentroDaDieta)
            db.session.add(ref)
            db.session.commit()
            return jsonify({"message": "Refeição criada com sucesso!"})

    return jsonify({"message": "Dados inválidos!"}), 400

@app.route("/refeicao/<int:id_refeicao>", methods=["PUT"])
def atualizar_refeicao(id_refeicao):
    data = request.json
    nome = data.get("nome")
    descricao = data.get("descricao")
    dentroDaDieta = data.get("dentroDaDieta")

    refeicao = Refeicao.query.get(id_refeicao)
    if refeicao:
        refeicao.nome = nome
        refeicao.descricao = descricao
        refeicao.dentroDaDieta = dentroDaDieta
        db.session.commit()
        return jsonify({"message": "Refeição atualizada com sucesso!"})

    return jsonify({"message": "Refeição não encontrada!"}), 404

@app.route("/refeicao/<int:id_refeicao>", methods=["DELETE"])
def deletar_refeicao(id_refeicao):
    refeicao = Refeicao.query.get(id_refeicao)
    if refeicao:
        db.session.delete(refeicao)
        db.session.commit()
        return jsonify({"message": f"Refeição {refeicao.nome} removida com sucesso!"}), 200

    return jsonify({"message": "Refeição não encontrada!"}), 404

@app.route("/refeicao", methods=["GET"])
def buscar_todas_refs():
    refeicoes = Refeicao.query.all()

    if refeicoes:
        return jsonify(
            [refeicao.to_dict() for refeicao in refeicoes]
        ), 200

    return jsonify({"message": "Nenhuma refeição encontrada!"}), 200

@app.route("/refeicao/<int:id_refeicao>", methods=["GET"])
def buscar_refeicao(id_refeicao):
    refeicao = Refeicao.query.get(id_refeicao)

    if refeicao:
        return jsonify(refeicao.to_dict())

    return jsonify({"message": "Refeição não encontrada!"}), 200


if __name__ == "__main__":
    app.run(debug=True)