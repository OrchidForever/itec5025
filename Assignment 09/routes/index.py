from .add_media import add_media
ROUTES = {
    "add_media": {
        "fn": add_media,
        "required": ["name", "owner", "location"],
    }
}