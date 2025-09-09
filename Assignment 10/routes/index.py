from .add_media import add_media
from .search_media import search_media
from .update_status import update_status

ROUTES = {
    "add_media": {
        "fn": add_media,
        "required": ["name", "owner", "location", "format"],
    },
    "search_media": {
        "fn": search_media,
        "required": ["name"],
    },
    "update_media_status": {
        "fn": update_status,  # Placeholder for update_media_status function
        "required": ["name", "status"],
    },
    "chitchat": {
        "fn": lambda: "Let's chat! How can I assist you today with your media management?",
        "required": [],
    },
}