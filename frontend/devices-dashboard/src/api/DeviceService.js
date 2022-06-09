export class DeviceModel {
  constructor(deviceId, name, temperature, water, sun) {
    this.deviceId = deviceId;
    this.name = name;
    this.temperature = temperature;
    this.water = water;
    this.sun = sun;
  }
}

const fakeDevices = [
  new DeviceModel("device1", "deviceName1", 15, 50, 5),
  new DeviceModel("device2", "deviceName2", 30, 10, 80),
  new DeviceModel("device3", "deviceName3", 45, 30, 64),
  new DeviceModel("device4", "deviceName4", 18, 70, 32),
  new DeviceModel("device5", "deviceName5", 25, 44, 57),
];

class DeviceService {
  getAllDevices() {
    return fakeDevices;
  }
}

export default new DeviceService();
