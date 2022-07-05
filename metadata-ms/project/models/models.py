# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

from sqlalchemy import Integer, String

from project.models.init_db import db


class UserProfile(db.Model):
    __tablename__ = "users"

    user_id = db.Column(Integer, primary_key=True, autoincrement=True)
    address = db.Column(String)
    contact_number = db.Column(String, unique=True)
    wallet_points = db.Column(Integer)
    
class Item(db.Model):
    __tablename__ = "items"

    item_id = db.Column(Integer, primary_key=True, autoincrement=True)
    receipe = db.Column(String)
    extra_info = db.Column(String)
    