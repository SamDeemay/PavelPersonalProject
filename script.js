async function generateMessage() {
    const userInput = document.getElementById('userInput').value;
    if (userInput.trim() === '') return;

    const chatMessages = document.getElementById('chatMessages');

    // Create user message
    const userMessage = document.createElement('p');
    userMessage.className = 'message user';
    userMessage.textContent = userInput;
    chatMessages.appendChild(userMessage);

    // Clear input field
    document.getElementById('userInput').value = '';

    // Scroll to the bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Create bot message container
    const botMessage = document.createElement('p');
    botMessage.className = 'message pavel';
    chatMessages.appendChild(botMessage);

    // Fetch bot response from backend
    const response = await fetch('http://localhost:1234/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            prompt: userInput
        })
    });

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        const chunk = decoder.decode(value);
        const lines = chunk.split('\n\n');
        for (const line of lines) {
            if (line.startsWith('data: ')) {
                const data = line.slice(6);
                botMessage.textContent += data;
                // Scroll to the bottom as new data is added
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }
        }
    }
}