from supabase import create_client
from datetime import datetime
import os

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

def upload_product_image(file, seller_id):
    bucket_name = "product-images"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = file.filename
    path = f"seller_{seller_id}/{timestamp}_{filename}"

    res = supabase.storage.from_(bucket_name).upload(
        path=path,
        file=file.read(),
        file_options={"content-type": file.content_type, "x-upsert": "true"}
    )
    print(res)

    if isinstance(res, dict) and res.get("error"):
        raise Exception(f"Erro no upload: {res['error']}")

    public_url = f"{url}/storage/v1/object/public/{bucket_name}/{path}"
    return public_url