from care.facility.models.json_schema.common import DATETIME_REGEX

BLOOD_PRESSURE = {
    "$schema": f"http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {"systolic": {"type": "number"}, "diastolic": {"type": "number"}, "mean": {"type": "number"},},
    "additionalProperties": False,
}

INFUSIONS = {
    "$schema": f"http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {"name": {"type": "string"}, "quantity": {"type": "number"},},
            "additionalProperties": False,
            "required": ["name", "quantity"],
        }
    ],
}

IV_FLUID = {
    "$schema": f"http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {"name": {"type": "string"}, "quantity": {"type": "number"},},
            "additionalProperties": False,
            "required": ["name", "quantity"],
        }
    ],
}

FEED = {
    "$schema": f"http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {"name": {"type": "string"}, "quantity": {"type": "number"},},
            "additionalProperties": False,
            "required": ["name", "quantity"],
        }
    ],
}

OUTPUT = {
    "$schema": f"http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {"name": {"type": "string"}, "quantity": {"type": "number"},},
            "additionalProperties": False,
            "required": ["name", "quantity"],
        }
    ],
}

PRESSURE_SORE = {
    "$schema": f"http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {"region": {"type": "string"}, "scale": {"type": "number", "minimum": 1, "maximum": 5},},
            "additionalProperties": False,
            "required": ["region", "scale"],
        }
    ],
}


NURSING_PROCEDURE = {
    "$schema": f"http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {"procedure": {"type": "string"}, "description": {"type": "string"},},
            "additionalProperties": False,
            "required": ["procedure", "description"],
        }
    ],
}
