from flask import Flask, render_template, request, redirect, url_for, session
from db import criar_tabelas
from auth import proteger_rotas
from desabafos import desabafos_bp
from metas import metas_bp
from cartas import cartas_bp

app = Flask(__name__)
app.secret_key = "segredo_super_secreto"

criar_tabelas()
proteger_rotas(app)

# rotas públicas
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/verificar", methods=["POST"])
def verificar():
    nome = request.form["nome"]
    senha = request.form["senha"]
    if nome == "Victor" and senha == "1029384756":
        session["logado"] = True
        return redirect(url_for("painel"))
    else:
        return "Nome ou senha incorretos"

@app.route("/painel")
def painel():
    return render_template("painel.html")

@app.route("/logout")
def logout():
    session.pop("logado", None)
    return redirect(url_for("home"))

# registrar blueprints
app.register_blueprint(desabafos_bp)
app.register_blueprint(metas_bp)
app.register_blueprint(cartas_bp)

if __name__ == "__main__":
    app.run(debug=True)