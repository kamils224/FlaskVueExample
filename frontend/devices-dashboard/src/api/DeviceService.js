import axios from "../axiosInstance";

export class DeviceModel {
  constructor(deviceId, name, temperature, water, sun) {
    this.deviceId = deviceId;
    this.name = name;
    this.temperature = temperature;
    this.water = water;
    this.sun = sun;
  }

  static fromJson(json) {
    return new DeviceModel(
      json.device_id,
      json.name,
      json.temperature,
      json.water,
      json.sun
    );
  }
}

class ActionModel {
  constructor(title, actionName) {
    this.title = title;
    this.actionName = actionName;
  }

  static fromJson(json) {
    return new ActionModel(json.title, json.action_name);
  }
}

class DeviceService {
  async getAllDevices() {
    const response = await axios.get("/devices");

    return response.data.devices.map((item) => DeviceModel.fromJson(item));
  }

  async getPossibleActions() {
    const response = await axios.get("/devices/actions");
    return response.data.actions.map((item) => ActionModel.fromJson(item));
  }

  async sendActionRequest(deviceId, actionName) {
    const response = await axios.post(`/device/${deviceId}`, {
      action_name: actionName,
    });
    return response.data.message;
  }
}

export default new DeviceService();
