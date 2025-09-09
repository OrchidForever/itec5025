import utils.database as db

def search_media(name):
    ''' Code to search media in the database by name '''
    # Verify if name is not empty
    if not name:
        return "Please provide a media name to search."
    media_db = db.PostgreSQLDatabase()
    media_db.connect()
    results = media_db.search_media_by_name(name)
    media_db.close()
    if results:
        # Check if multiple results and format accordingly
        if len(results) > 1:
            returnValue = "Found multiple media entries:\n"
            for item in results:
                returnValue += f"Found {item[2]} {item[1]} located at {item[4]} owned by {item[3]} with status {item[5]}\n"
            return returnValue.strip()
        else:
            return f"Found one record: {results[0][2]} {results[0][1]} located at {results[0][4]} owned by {results[0][3]} with status {results[0][5]}"
    else:
        return "No media found."