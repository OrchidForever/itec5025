import utils.database as db

def search_media(name):
    # media_db = db.PostgreSQLDatabase()
    # media_db.connect()
    # results = media_db.search_media(name)
    # media_db.close()
    # if results:
    #     return results
    # else:
    #     return "No media found."
    print(f"[DEBUG] search_media called with: name={name}")
    return f"Search results for media '{name}': [Sample Media 1, Sample Media 2]"
