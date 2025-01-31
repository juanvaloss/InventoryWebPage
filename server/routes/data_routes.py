from flask import Blueprint, jsonify, request
from supabase_client import supabase

data_bp = Blueprint("data", __name__)

@data_bp.route("/inventario", methods = ["GET"])
def get_data():
    response = supabase.table("catalogoMotores").select("*"). execute()
    return jsonify(response.data), 200

@data_bp.route("/inventario", methods=["POST"])
def addMotores():
    data = request.json
    response = supabase.table("catalogoMotores").insert(data).execute()
    return jsonify({"message": "Motor subido a la base de datos", "data": response.data}), 201