import logging
from typing import List, Tuple

from storage.fake_storage import FakeDeviceFactory
from storage.models import DeviceModel


def get_all_devices() -> List[DeviceModel]:
    # TODO: add the real source of devices here
    return FakeDeviceFactory.get_fake_devices()


class DeviceActionType:
    WATERING = "WATERING"

    class Meta:
        strict = True


def start_device_action(device_id: str, action_type: str) -> Tuple[bool, str]:
    try:
        if action_type == DeviceActionType.WATERING:
            # TODO: send this action to the broker
            # TODO: You can add more actions here
            logging.info(
                f"[Device({device_id})]Started action of type: {DeviceActionType.WATERING}"
            )
            message = (
                f"Action [{action_type}] for device [{device_id}] executed successfully"
            )
            return True, message

    except Exception:
        # We can use exception message or whatever we need
        error = "Cannot complete an action"
        return False, error

    error = f"[Device({device_id})]Unknown action type: {action_type}"
    logging.warning(error)
    return False, error
