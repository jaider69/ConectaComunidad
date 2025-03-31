from dotenv import load_dotenv
import os

# Especifica la ruta ABSOLUTA al .env
load_dotenv(r'C:\conectacomunidad\ConectaComunidad\api\config\backen\.env')

# Verifica que carga las variables (opcional)
print("URL cargada:", os.getenv('SUPABASE_URL'))