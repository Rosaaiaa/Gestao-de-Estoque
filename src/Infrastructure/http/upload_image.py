from supabase import create_client
import os

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

def upload_product_image(file):
    
    bucket_name = "product-images"
    filename = file.filename

    # Faz upload no bucket (sobrescreve se já existir)
    res = supabase.storage.from_(bucket_name).upload(filename, file.read(), {"upsert": True})

    # Retorna a URL pública
    public_url = f"{url}/storage/v1/object/public/{bucket_name}/{filename}"
    return public_url