STORE_SCHEMA = {
    "type": "object",
    "required": [
        "id",
        "petId",
        "quantity",
        "status",
        "complete"
    ],
    "properties": {
        "id": {
            "type": "integer",
            "minimum": 1
        },
        "petId": {
            "type": "integer",
            "minimum": 1
        },
        "quantity": {
            "type": "integer",
            "minimum": 0
        },
        "status": {
            "type": "string",
            "enum": ["placed", "approved", "delivered"]
        },
        "complete": {
            "type": "boolean"
        }
    },
    "additionalProperties": False
}
