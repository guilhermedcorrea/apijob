from app import create_app
"""Estarta aplicação"""
app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, port=8900, debug=True)