from supabase import create_client
from uuid import uuid4

# Configuración
SUPABASE_URL = 'https://ywfxblbdenirocfwexpz.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl3ZnhibGJkZW5pcm9jZndleHB6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDMzNjA0MTMsImV4cCI6MjA1ODkzNjQxM30.Vtd1VLKoOS7l_cIdtm7Rdhg-to7gA4jzZjk-TZNdaIA'  # Tu clave

# Inicializar cliente
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Registro de ejemplo
try:
    # 1. Registrar usuario en Auth (opcional, si necesitas el auth_id real)
    auth_response = supabase.auth.sign_up({
        "email": "jaider55@gmail.com",
        "password": "123456j"
    })
    
    # 2. Insertar en 'persona' con UUID válido
    data, count = supabase.table('persona').insert({
        "nombre": "jaide",
        "dni": "12345678",
        "telefono": "30012354567",
        "correo_electr": "jaider55@gmail.com",
        "auth_id": auth_response.user.id  # UUID real
        # O usa str(uuid4()) para pruebas sin Auth
    }).execute()

    print("✅ Datos insertados:", data)
except Exception as e:
    print("❌ Error:", e)