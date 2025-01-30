from flask import Flask
from flask_cors import CORS
from routes.data_routes import data_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(data_bp, url_prefix='/data')

@app.route ("/")
def home():
    return {"message": "Servidor Flask funcionando perra"}



if __name__ == "__main__":
    app.run(debug = True)