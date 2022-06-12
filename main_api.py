from flask import Blueprint
from flask_restful import Api

from api_resources.devices import (
    DevicesListApi,
    DeviceActionsApi,
    DevicesActionsListApi,
)

# endpoint starts with /api
bp = Blueprint("main_api", __name__, url_prefix="/api")
api = Api(bp)

# GET /api/devices
api.add_resource(DevicesListApi, "/devices")
# GET /api/devices/actions
api.add_resource(DevicesActionsListApi, "/devices/actions")
# POST /api/device/<device_id>
api.add_resource(DeviceActionsApi, "/device/<device_id>")
