from dataclasses import dataclass


@dataclass
class DeviceModel:
    device_id: str
    name: str
    temperature: int
    water: int
    sun: int
