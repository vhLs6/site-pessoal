from flask import Blueprint, render_template, request, redirect, url_for
from db import adicionar, atualizar, deletar, buscar_por_id, conectar_banco
from datetime import datetime

cartas_bp = Blueprint("cartas", __name__)

def get_cartas():
    conn, cursor = conectar_banco()
    cursor.execute("SELECT * FROM cartas ORDER BY id DESC")
    cartas = cursor.fetchall()
    conn.close()
    return cartas

@cartas_bp.route("/cartas")
def cartas():
    return render_template("cartas.html", cartas=get_cartas())

@cartas_bp.route("/nova_carta")
def nova_carta():
    return render_template("nova_carta.html", carta=None)  # Passa None pra criar nova

@cartas_bp.route("/salvar_carta", methods=["POST"])  # Mudei o nome da rota
def salvar_carta():
    texto = request.form["texto"]  # Mudei pra "texto" pra ficar igual desabafos
    agora = datetime.now()
    data_br = agora.strftime("%d/%m/%Y %H:%M")
    adicionar("cartas", (texto, data_br))
    return redirect(url_for("cartas.cartas"))

@cartas_bp.route("/editar_carta/<int:id>")
def editar_carta(id):
    carta = buscar_por_id("cartas", id)
    if not carta:
        return "Carta não encontrada", 404
    return render_template("nova_carta.html", carta=carta)

@cartas_bp.route("/atualizar_carta/<int:id>", methods=["POST"])  # Rota pra atualizar
def atualizar_carta(id):
    texto = request.form["texto"]
    atualizar("cartas", "texto", texto, id)
    return redirect(url_for("cartas.cartas"))

@cartas_bp.route("/deletar_carta/<int:id>")
def deletar_carta(id):
    deletar("cartas", id)
    return redirect(url_for("cartas.cartas"))