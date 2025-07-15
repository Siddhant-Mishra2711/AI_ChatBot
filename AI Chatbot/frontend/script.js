async function sendMessage() {
  const input = document.getElementById("user-input");
  const chatLog = document.getElementById("chat-log");
  const message = input.value;

  chatLog.innerHTML += "<div><b>You:</b> " + message + "</div>";
  input.value = "";

  const response = await fetch("http://localhost:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  const data = await response.json();
  chatLog.innerHTML += "<div><b>Bot:</b> " + data.response + "</div>";
  chatLog.scrollTop = chatLog.scrollHeight;
}