import utils.database as db

def update_status(name, status):
    #Code to update media status in the database
    media_db = db.PostgreSQLDatabase()
    media_db.connect()
    success = media_db.update_media_status(name, status)
    print(f"[DEBUG] update_status called with: name={name}, status={status}")
    media_db.close()
    if success:
        return f"Media '{name}' status updated to '{status}'."
    else:
        return "Failed to update media status."