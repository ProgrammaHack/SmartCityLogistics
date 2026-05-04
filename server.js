const express = require("express");
const cors = require("cors");
const db = require("./db");

const app = express();

app.use(cors());
app.use(express.json());
app.use(express.static("public"));

/* ---------------- VEHICLES ---------------- */
app.get("/api/vehicles", async (req, res) => {
  const data = await db.query("SELECT * FROM Vehicle");
  res.json(data.rows);
});

/* ---------------- MISSIONS ---------------- */
app.get("/api/missions", async (req, res) => {
  const data = await db.query("SELECT * FROM Mission");
  res.json(data.rows);
});

/* ---------------- MAINTENANCE ---------------- */
app.get("/api/maintenance", async (req, res) => {
  const data = await db.query("SELECT * FROM Maintenance");
  res.json(data.rows);
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});