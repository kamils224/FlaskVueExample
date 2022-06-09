import logging
from enum import Enum, auto
from typing import List, Any

from database.fake_storage import get_fake_devices
from database.models import DeviceModel


def get_all_devices() -> List[DeviceModel]:
    # todo: add the real source of devices here
    return get_fake_devices()


class AutoName(Enum):
    def _generate_next_value_(
        self: str, start: int, count: int, last_values: list[Any]
    ) -> Any:
        return self


class DeviceActionType(AutoName):
    WATERING = auto()


def start_device_action(device_id: str, action_type: str) -> bool:
    if action_type == DeviceActionType.WATERING:
        logging.info(f"[Device({device_id})]Started action of type: {DeviceActionType.WATERING}")
        return True

    logging.warning(f"[Device({device_id})]Unknown action type: {action_type}")
    return False
