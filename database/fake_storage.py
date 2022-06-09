from typing import List

from database.models import FakeDeviceFactory, DeviceModel


def get_fake_devices() -> List[DeviceModel]:
    number_of_items = 15
    return [
        FakeDeviceFactory.create_random_fake_device() for _ in range(number_of_items)
    ]
