import logging
from typing import List

from storage.fake_storage import FakeDeviceFactory
from storage.models import DeviceModel


def get_all_devices() -> List[DeviceModel]:
    # TODO: add the real source of devices here
    return FakeDeviceFactory.get_fake_devices()


class DeviceActionType:
    WATERING = "WATERING"

    class Meta:
        strict = True


def start_device_action(device_id: str, action_type: str) -> bool:
    if action_type == DeviceActionType.WATERING:
        # TODO: send this action to the broker
        # TODO: You can add more actions here
        logging.info(
            f"[Device({device_id})]Started action of type: {DeviceActionType.WATERING}"
        )
        return True

    logging.warning(f"[Device({device_id})]Unknown action type: {action_type}")
    return False
