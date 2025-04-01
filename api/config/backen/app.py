from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# Especifica la ruta ABSOLUTA al .env
load_dotenv(r'C:\conectacomunidad\ConectaComunidad\api\config\backen\.env')

# Verifica que carga las variables (opcional)
print("URL cargada:", os.getenv('SUPABASE_URL'))  # Corregido aquí el nombre de la variable

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route('/registro', methods=['POST'])
def registrar():
    try:
        data = request.json  # Recibe los datos del frontend
        
        # Simulación de registro exitoso (aquí puedes agregar la lógica con Supabase)
        return jsonify({"success": True, "message": "Registro exitoso"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
