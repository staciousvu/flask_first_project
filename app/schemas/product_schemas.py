from flask_marshmallow import Schema
from marshmallow import fields

class ProductSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    description = fields.Str(required=False)
    category_id = fields.Int(required=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
    