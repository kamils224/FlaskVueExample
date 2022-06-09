from dataclasses import asdict

from flask import request
from marshmallow import Schema, fields

import services.devices as device_service
from api_resources.base_resource import BaseResource


class DevicesListApi(BaseResource):
    def get(self):
        """
        A list of connected devices.
        """
        devices_list = device_service.get_all_devices()
        return self.success_response([asdict(device) for device in devices_list])


class DeviceActionsSerializer(Schema):
    action_type = fields.String(required=True)


class DeviceActionsApi(BaseResource):
    def post(self, device_id: str):
        validated = DeviceActionsSerializer().load(request.json)
        action_type = validated["action_type"]
        success = device_service.start_device_action(device_id, action_type)

        if success:
            return self.success_response(f"Action [{action_type}] executed successfully")
        return self.error_not_found()
