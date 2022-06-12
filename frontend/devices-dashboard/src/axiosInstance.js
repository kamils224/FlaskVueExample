import axios from "axios";

const baseUrl = "http://127.0.0.1:5000/api";

export default axios.create({
  baseURL: baseUrl,
  timeout: 100000,
  headers: {
    "Content-Type": "application/json",
  },
});
