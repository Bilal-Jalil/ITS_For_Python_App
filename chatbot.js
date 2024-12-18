function askChatbot() {
    const query = document.getElementById('chat-query').value;
    fetch('/chatbot', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: 'query=' + encodeURIComponent(query)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('chat-response').innerText = data.response;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
