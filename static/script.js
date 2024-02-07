function sendMessage() {
    var userMessage = document.getElementById("user-message").value;

    if (userMessage.trim() === "") {
        return;
    }

    document.getElementById("chat-box").innerHTML += "<p>User: " + userMessage + "</p>";

    // Send the user message to the server
    fetch("/ask", {
        method: "POST",
        body: new URLSearchParams({
            "user_message": userMessage
        }),
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    })
    .then(response => response.json())
    .then(data => {
        var botResponse = data.bot_response;
        document.getElementById("chat-box").innerHTML += "<p>Bot: " + botResponse + "</p>";
    });

    // Clear the input field
    document.getElementById("user-message").value = "";
}
