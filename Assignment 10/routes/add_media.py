import utils.database as db

def add_media(name, format, owner, location):
    ''' Code to add media to the database with validation and duplication check '''
    # First verify if values are not empty
    if not all([name, format, owner, location]):
        return "Failed to add media. Please provide all required fields."
    media_db = db.PostgreSQLDatabase()
    media_db.connect()
    # Verify if media already exists
    existing_media = media_db.search_media_by_name(name)
    if existing_media:
        return f"The {format} '{name}' already exists."
    success = media_db.add_media(name, format, owner, location)
    media_db.close()
    if success:
        return f"The {format} '{name}' was added successfully."
    else:
        return "Failed to add media. Please try again."