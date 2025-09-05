import utils.database as db

def search_media(name):
    media_db = db.PostgreSQLDatabase()
    media_db.connect()
    print(f"[DEBUG] search_media called with: name={name}")
    results = media_db.search_media(name)
    media_db.close()
    if results:
        return results
    else:
        return "No media found."