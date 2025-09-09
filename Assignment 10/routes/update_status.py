import utils.database as db

def update_status(name, status, format=None):
    ''' Code to update media status in the database with validation '''
    # Verify if values are not empty
    if not name or not status:
        return "Failed to update media status. Please provide both name and status."
    media_db = db.PostgreSQLDatabase()
    media_db.connect()
    # Verify if media exists
    existing_media = media_db.search_media_by_name(name)
    if not existing_media:
        media_db.close()
        return f"Media '{name}' not found."
    # Verify that more than one media is not found
    if len(existing_media) > 1 and format is None:
        media_db.close()
        return f"Multiple entries found for media '{name}'. Please specify further."
    if format is None:
        success = media_db.update_media_status(name, status)
    else:
        success = media_db.update_media_status_by_name_and_format(name, format, status)
    media_db.close()
    if success:
        return f"Media '{name}' status updated to '{status}'."
    else:
        return "Failed to update media status."