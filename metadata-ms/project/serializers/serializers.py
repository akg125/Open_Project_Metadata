from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema

from project.models.models import  Item, UserProfile

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = UserProfile
        fields = ('user_id', 'contact_number', 'address', 'wallet_points')

class ItemSchema(SQLAlchemySchema):
    class Meta:
        model = Item
        fields = ('item_id', 'receipe', 'extra_info')