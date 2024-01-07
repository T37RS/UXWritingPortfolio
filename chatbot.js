const chatDisplay = document.getElementById('chatDisplay');
const userInputField = document.getElementById('userInput');

// Initial welcome message
displayMessage("Welcome to TruckingBot! How can I assist you today? You can ask about routes, safety, truck stops, or track a shipment.", 'bot');

// Function to process user input and generate bot responses
function processUserInput(userInput) {
    const lowercaseInput = userInput.toLowerCase();

    if (lowercaseInput.includes('help')) {
        return "👋 You can ask about routes, safety, truck stops, or track a shipment.";
    } else if (lowercaseInput.includes('route')) {
        return "📍 Sure thing! To get information about a specific route, please provide the starting and ending locations.";
    } else if (lowercaseInput.includes('track shipment')) {
        return "🚛 To track a shipment, please enter the tracking number or provide details about your shipment. For example, 'Track shipment ABC123'.";
    } else if (lowercaseInput.includes('safety')) {
        return "⚠️ Safety first! If you have questions about safety regulations, let me know what specific information you're looking for.";
    } else if (lowercaseInput.includes('truck stop')) {
        return "⛽ Need a pit stop? Please provide your location, and I'll help you find the nearest truck stop.";
    } else {
        return "🤖 I'm sorry if I didn't understand your query. Please type 'Help' for assistance or choose from the options mentioned.";
    }
}

// Function to display a message in the chat display
function displayMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.className = `${sender}-message`;
    messageElement.textContent = `${sender.charAt(0).toUpperCase() + sender.slice(1)}: ${message}`;
    chatDisplay.appendChild(messageElement);
    chatDisplay.scrollTop = chatDisplay.scrollHeight;
}

// Function to handle user input and display the conversation
function sendMessage() {
    const userInput = userInputField.value.trim();

    if (userInput === '') {
        return; // Don't process empty messages
    }

    // Display user message
    displayMessage(userInput, 'user');

    // Process user input and display bot response
    const botResponse = processUserInput(userInput);
    displayMessage(botResponse, 'bot');

    // Clear user input field
    userInputField.value = '';
}

// Function to handle Enter key press
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}