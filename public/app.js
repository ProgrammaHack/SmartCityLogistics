async function loadVehicles() {
  const res = await fetch("/api/vehicles");
  const data = await res.json();
  document.getElementById("output").innerText =
    JSON.stringify(data, null, 2);
}

async function loadMissions() {
  const res = await fetch("/api/missions");
  const data = await res.json();
  document.getElementById("output").innerText =
    JSON.stringify(data, null, 2);
}

async function loadMaintenance() {
  const res = await fetch("/api/maintenance");
  const data = await res.json();
  document.getElementById("output").innerText =
    JSON.stringify(data, null, 2);
}