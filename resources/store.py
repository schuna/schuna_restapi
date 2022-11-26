import uuid
from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView

from db import items, stores
from schemas import StoreSchema

blp = Blueprint("Stores", __name__, description="Operations on stores")


# noinspection PyMethodMayBeStatic
@blp.route("/store/<string:store_id>")
class Stores(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Sore deleted."}
        except KeyError:
            abort(404, message="Store not found")


# noinspection PyMethodMayBeStatic
@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return {"stores": list(stores.values())}

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message="Store already exists")
        store_id = uuid.uuid4().hex
        store = {**store_data, "store_id": store_id}
        stores[store_id] = store
        return store
