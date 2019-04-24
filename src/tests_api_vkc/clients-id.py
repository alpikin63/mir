from src.model.vkc import Vkc
import json
import jsonschema


def test_correct_code():
    print(Vkc().clients_by_id(672363).text)
