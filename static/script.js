function sendMessage(event) {
  event.preventDefault();
  const userInput = document.getElementById("userInput");
  const chatbox = document.getElementById("chatbox");

  // Ajouter le message utilisateur
  const userMessage = document.createElement("div");
  userMessage.className = "user-message";
  userMessage.innerText = userInput.value;
  chatbox.appendChild(userMessage);

  // Envoyer la question via Fetch API
  fetch("/ask", {
    method: "POST",
    body: new URLSearchParams({ question: userInput.value }),
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
  })
    .then((response) => response.json())
    .then((data) => {
      const botMessage = document.createElement("div");
      botMessage.className = "bot-message";
      botMessage.innerText = data.answer;
      chatbox.appendChild(botMessage);
      chatbox.scrollTop = chatbox.scrollHeight;
    });

  userInput.value = "";
  return false;
}
