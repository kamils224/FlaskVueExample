<template>
  <a-table bordered :dataSource="devices" :columns="devicesColumns">
    <template #bodyCell="{ column, record }">
      <template v-if="column.dataIndex === 'actions'">
        <a-button
          type="primary"
          @click="onActionClick(record.deviceId, actionTypes.watering)"
          >Watering</a-button
        >
      </template>
    </template>
  </a-table>
</template>

<script>
import deviceService from "../api/DeviceService";
export default {
  name: "DashboardView",
  components: {},
  data() {
    return {
      actionTypes: {
        watering: "WATERING",
      },
      devices: null,
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
      console.log(deviceId);
      console.log(actionType);
    },
  },
  mounted() {
    this.devices = deviceService.getAllDevices();
  },
};
</script>

<style lang="scss" scoped></style>
