from flask import Flask, jsonify, request
from flask_cors import CORS
from supabase_client import supabase

app = Flask(__name__)

CORS(app)

@app.route ("/")
def home():
    return jsonify({"message": "Servidor Flask funcionando a todo motor!!"})

@app.route("/getMotores", methods = ["GET"])
def getData():
    response = supabase.table ("Motores").select("*").execute()
    return jsonify(response.data), 200

@app.route("/addMotores", methods=["POST"])
def addMotores():
    data = request.json
    response = supabase.table("Motores").insert(data).execute()
    return jsonify({"message": "Motor subibdo a la base de datos campeon", "data": response.data}), 201

if __name__ == "__main__":
    app.run(debug = True)