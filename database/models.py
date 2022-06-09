import random
from dataclasses import dataclass
from itertools import count


@dataclass
class DeviceModel:
    device_id: str
    name: str
    temperature: int
    water: int
    sun: int


class FakeDeviceFactory:
    # number of instances created by this factory
    __created_instances = count(0)

    @staticmethod
    def create_random_fake_device() -> DeviceModel:
        unique_id = next(FakeDeviceFactory.__created_instances)
        return DeviceModel(
            device_id=f"device{unique_id}",
            name=f"device_name_{unique_id}",
            temperature=random.randint(0, 50),
            water=random.randint(0, 100),
            sun=random.randint(0, 100),
        )
