from flask import Blueprint, render_template, request, redirect, url_for
from db import adicionar, atualizar, deletar, buscar_por_id, conectar_banco

metas_bp = Blueprint("metas", __name__)

def get_metas():
    conn, cursor = conectar_banco()
    cursor.execute("SELECT * FROM metas")
    metas = cursor.fetchall()
    conn.close()
    return metas

@metas_bp.route("/metas")
def metas():
    return render_template("metas.html", metas=get_metas())

@metas_bp.route("/adicionar_meta", methods=["POST"])
def adicionar_meta():
    meta = request.form["meta"]
    adicionar("metas", (meta,))
    return redirect(url_for("metas.metas"))

@metas_bp.route("/deletar_meta/<int:id>")
def deletar_meta(id):
    deletar("metas", id)
    return redirect(url_for("metas.metas"))

@metas_bp.route("/editar_meta/<int:id>")
def editar_meta(id):
    meta = buscar_por_id("metas", id)
    return render_template("metas.html", metas=get_metas(), meta_edit=meta)

@metas_bp.route("/atualizar_meta/<int:id>", methods=["POST"])
def atualizar_meta(id):
    nova_meta = request.form["meta"]
    atualizar("metas", "meta", nova_meta, id)
    return redirect(url_for("metas.metas"))