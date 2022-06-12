<template>
  <a-button type="secondary" @click="loadDevices">Refresh</a-button>
  <a-divider />
  <a-table
    v-if="!isLoading"
    bordered
    :dataSource="devices"
    :columns="devicesColumns"
  >
    <template #bodyCell="{ column, record }">
      <template v-if="column.dataIndex === 'actions'">
        <a-button
          v-for="action in actions"
          :key="action.actionName"
          type="primary"
          @click="onActionClick(record.deviceId, action.actionName)"
          >{{ action.title }}</a-button
        >
      </template>
    </template>
  </a-table>
  <a-spin size="large" v-else style="width: 100%; justify-content: center"/>
</template>

<script>
import deviceService from "../api/DeviceService";
export default {
  name: "DashboardView",
  components: {},
  data() {
    return {
      actions: [],
      devices: [],
      isLoading: false,
      devicesDataSource: [],
      devicesColumns: [
        { title: "Device ID", dataIndex: "deviceId", key: "deviceId" },
        { title: "Name", dataIndex: "name", key: "name" },
        { title: "Temperature", dataIndex: "temperature", key: "temperature" },
        { title: "Water", dataIndex: "water", key: "water" },
        { title: "Sun", dataIndex: "sun", key: "sun" },
        { title: "Actions", dataIndex: "actions" },
      ],
    };
  },
  methods: {
    onActionClick(deviceId, actionType) {
      deviceService.sendActionRequest(deviceId, actionType);
    },
    async loadDevices() {
      this.isLoading = true;
      [this.devices, this.actions] = await Promise.all([
        deviceService.getAllDevices(),
        deviceService.getPossibleActions(),
      ]);
      this.isLoading = false;
    },
  },
  async mounted() {
    await this.loadDevices();
  },
};
</script>

<style lang="scss" scoped></style>
