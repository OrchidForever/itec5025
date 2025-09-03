from .add_media import add_media
ROUTES = {
    "add_media": {
        "fn": add_media,
        "required": ["name", "owner", "location", "format"],
    },
    "search_media": {
        "fn": None,  # Placeholder for search_media function
        "optional": ["name", "owner", "location", "format"],
    },
    "update_media_status": {
        "fn": None,  # Placeholder for update_media_status function
        "required": ["name", "status"],
    },
    "chitchat": {
        "fn": lambda: "Let's chat! How can I assist you today with your media management?",
        "required": [],
    },
}