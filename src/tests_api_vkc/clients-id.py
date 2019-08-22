from src.model.vkc import Vkc
import json
import jsonschema
import pprint


def test_correct_code():
  pprint.pprint(Vkc().partners_by_id('916').json())
  sheme={
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "id",
    "name",
    "shortDescription",
    "description",
    "partnerLegalEntities",
    "url"
  ],
  "properties": {
    "id": {
      "$id": "#/properties/id",
      "type": "integer",
      "title": "The Id Schema",
      "default": 0,
      "examples": [
        0
      ]
    },
    "name": {
      "$id": "#/properties/name",
      "type": "string",
      "title": "The Name Schema",
      "default": "",
      "examples": [
        "string"
      ],
      "pattern": "^(.*)$"
    },
    "shortDescription": {
      "$id": "#/properties/shortDescription",
      "type": "string",
      "title": "The Shortdescription Schema",
      "default": "",
      "examples": [
        "string"
      ],
      "pattern": "^(.*)$"
    },
    "description": {
      "$id": "#/properties/description",
      "type": "string",
      "title": "The Description Schema",
      "default": "",
      "examples": [
        "string"
      ],
      "pattern": "^(.*)$"
    },
    "partnerLegalEntities": {
      "$id": "#/properties/partnerLegalEntities",
      "type": "array",
      "title": "The Partnerlegalentities Schema",
      "items": {
        "$id": "#/properties/partnerLegalEntities/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "legalId",
          "legalName",
          "legalAddress",
          "requisites"
        ],
        "properties": {
          "legalId": {
            "$id": "#/properties/partnerLegalEntities/items/properties/legalId",
            "type": "integer",
            "title": "The Legalid Schema",
            "default": 0,
            "examples": [
              0
            ]
          },
          "legalName": {
            "$id": "#/properties/partnerLegalEntities/items/properties/legalName",
            "type": "string",
            "title": "The Legalname Schema",
            "default": "",
            "examples": [
              "string"
            ],
            "pattern": "^(.*)$"
          },
          "legalAddress": {
            "$id": "#/properties/partnerLegalEntities/items/properties/legalAddress",
            "type": "string",
            "title": "The Legaladdress Schema",
            "default": "",
            "examples": [
              "string"
            ],
            "pattern": "^(.*)$"
          },
          "requisites": {
            "$id": "#/properties/partnerLegalEntities/items/properties/requisites",
            "type": "string",
            "title": "The Requisites Schema",
            "default": "",
            "examples": [
              "string"
            ],
            "pattern": "^(.*)$"
          }
        }
      }
    },
    "url": {
      "$id": "#/properties/url",
      "type": "string",
      "title": "The Url Schema",
      "default": "",
      "examples": [
        "string"
      ],
      "pattern": "^(.*)$"
    }
  }
}
  jsonschema.validate(instance=Vkc().partners_by_id('916').json(), schema=sheme)