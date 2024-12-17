from supabase import create_client, Client
import config

def get_supabase_client() -> Client:
    url = config.SUPABASE_URL
    key = config.SUPABASE_KEY
    return create_client(url, key)

supabase = get_supabase_client()