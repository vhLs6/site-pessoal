from flask import session, redirect, url_for, request

PUBLIC_PAGES = ["home", "verificar", "static"]

def proteger_rotas(app):
    @app.before_request
    def proteger():
        if request.endpoint not in PUBLIC_PAGES and not session.get("logado"):
            return redirect(url_for("home"))