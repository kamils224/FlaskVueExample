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
        return self.success_response(
            {"devices": [asdict(device) for device in devices_list]}
        )


class DevicesActionsListApi(BaseResource):
    def get(self):
        """
        A list of possible actions
        """
        possible_actions = [
            {
                "title": "Watering",
                "action_name": device_service.DeviceActionType.WATERING,
            }
        ]
        return self.success_response({"actions": possible_actions})


class DeviceActionsSerializer(Schema):
    action_name = fields.String(required=True)


class DeviceActionsApi(BaseResource):
    def post(self, device_id: str):
        validated = DeviceActionsSerializer().load(request.json)
        action_type = validated["action_name"]
        success = device_service.start_device_action(device_id, action_type)

        if success:
            return self.success_response(
                {"message": f"Action [{action_type}] executed successfully"}
            )
        return self.error_not_found()
