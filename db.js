const { Pool } = require("pg");

const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "SmartCityLogistics",
  password: "password",
  port: 5460
});

module.exports = pool;