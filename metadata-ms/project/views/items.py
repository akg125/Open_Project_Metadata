# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals
from typing import Tuple

import connexion
from flask import jsonify

from project.models.init_db import db
from project.models.models import  Item
from project.serializers.serializers import ItemSchema


def get(id: int) -> Tuple[dict, int]:

    item = Item.query.get(id)

    schema = ItemSchema()
    result = schema.dump(item)

    if not len(result):
        result = { "message": "Item does not exist" }
        return jsonify(result), 404

    return jsonify(result), 200


def search() -> Tuple[dict, int]:
    return get()


def post() -> dict:
    if connexion.request.is_json:
        data = connexion.request.get_json()
        item = Item(receipe=data["receipe"], extra_info=data['extra_info'])
        db.session.add(item)
        db.session.commit()

        return jsonify(ItemSchema().dump(item))
    return jsonify({})

def put(id: int) -> dict:


    if connexion.request.is_json:
        data = connexion.request.get_json()

        item = Item.query.get(id)

        if("receipe" in data.keys()):
            item.receipe = data.get("receipe")
        if("extra_info" in data.keys()):    
            item.extra_info = data["extra_info"]

        db.session.commit()

        return jsonify(ItemSchema().dump(item))
    return jsonify({})