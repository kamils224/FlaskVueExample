import random
from itertools import count
from typing import List

from storage.models import DeviceModel


class FakeDeviceFactory:
    @staticmethod
    def create_random_fake_devices(num_of_items: int) -> List[DeviceModel]:
        start = random.randint(0, 999999)
        return [
            DeviceModel(
                device_id=f"device{i}",
                name=f"device_name_{i}",
                temperature=random.randint(0, 50),
                water=random.randint(0, 100),
                sun=random.randint(0, 100),
            )
            for i in range(start, start + num_of_items)
        ]

    @staticmethod
    def get_fake_devices() -> List[DeviceModel]:
        num_of_items = 35
        return FakeDeviceFactory.create_random_fake_devices(num_of_items)
