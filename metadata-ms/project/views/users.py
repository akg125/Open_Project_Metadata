# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals
from typing import Tuple

import connexion
from flask import jsonify

from project.models.init_db import db
from project.models.models import  UserProfile
from project.serializers.serializers import UserSchema


def get(id: int) -> Tuple[dict, int]:

    user = UserProfile.query.get(id)

    schema = UserSchema()
    result = schema.dump(user)

    if not len(result):
        result = { "message": "User does not exist" }
        return jsonify(result), 404

    return jsonify(result), 200


def search() -> Tuple[dict, int]:
    return get()


def post() -> dict:
    if connexion.request.is_json:
        data = connexion.request.get_json()
        user = UserProfile(contact_number=data["contact_number"], address = data["address"], wallet_points=data["wallet_points"])
        db.session.add(user)
        db.session.commit()

        return jsonify(UserSchema().dump(user))
    return jsonify({})

def put(id: int) -> dict:


    if connexion.request.is_json:
        data = connexion.request.get_json()

        user = UserProfile.query.get(id)

        if("address" in data.keys()):
            user.address = data.get("address")
        if("wallet_points" in data.keys()):    
            user.wallet_points = data["wallet_points"]
        if("contact_number" in data.keys()):
            user.contact_number = data["contact_number"]

        db.session.commit()

        return jsonify(UserSchema().dump(user))
    return jsonify({})