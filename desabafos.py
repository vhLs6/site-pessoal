from flask import Blueprint, render_template, request, redirect, url_for
from db import adicionar, atualizar, deletar, buscar_por_id, conectar_banco
from datetime import datetime

desabafos_bp = Blueprint("desabafos", __name__)

def get_desabafos():
    conn, cursor = conectar_banco()
    cursor.execute("SELECT * FROM desabafos ORDER BY id DESC")
    desabafos = cursor.fetchall()
    conn.close()
    return desabafos

@desabafos_bp.route("/desabafos")
def desabafos():
    return render_template("desabafos.html", desabafos=get_desabafos())

@desabafos_bp.route("/novo_desabafo")
def novo_desabafo():
    return render_template("novo_desabafo.html")

@desabafos_bp.route("/salvar_desabafo", methods=["POST"])
def salvar_desabafo():
    texto = request.form["texto"]
    agora = datetime.now()
    data_br = agora.strftime("%d/%m/%Y %H:%M")
    adicionar("desabafos", (texto, data_br))
    return redirect(url_for("desabafos.desabafos"))

@desabafos_bp.route("/editar_desabafo/<int:id>")
def editar_desabafo(id):
    desabafo = buscar_por_id("desabafos", id)
    return render_template("editar_desabafo.html", desabafo=desabafo)

@desabafos_bp.route("/atualizar_desabafo/<int:id>", methods=["POST"])
def atualizar_desabafo(id):
    texto = request.form["texto"]
    atualizar("desabafos", "texto", texto, id)
    return redirect(url_for("desabafos.desabafos"))

@desabafos_bp.route("/deletar_desabafo/<int:id>")
def deletar_desabafo(id):
    deletar("desabafos", id)
    return redirect(url_for("desabafos.desabafos"))