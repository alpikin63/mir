from src.model.vkc import Vkc
import json
import jsonschema
from jsonschema import validate

schema = {
    "type": "object",
    "required": ["id", "status", "name", "phone", "email", "sex", "birthday", "cards", "clientDataChangeHistory",
                 "comment", "registrationMethod", "registrationDate"]
}
validate(instance=Vkc().clients_by_id(2).json(), schema=schema)

