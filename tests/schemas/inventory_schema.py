INVENTORY_SCHEMA = {
    "type": "object",
    "required": [
        "approved"
    ],
    "properties": {
        "approved": {
            "type": "integer",
            "minimum": 0
        }
    },
    "additionalProperties": False
}