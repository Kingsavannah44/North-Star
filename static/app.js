// app.js — owned by the frontend developer
 
        const chatMessages = document.getElementById('chatMessages');
        const messageInput = document.getElementById('messageInput');
        const suggestions = document.getElementById('suggestions');

        async function sendMessage(text = null) {
            const message = text || messageInput.value.trim();
            if (!message) return;

            // Clear input
            messageInput.value = '';

            // Remove empty state if present
            const emptyState = chatMessages.querySelector('.empty-state');
            if (emptyState) {
                emptyState.remove();
            }

            // Hide suggestions
            if (suggestions) {
                suggestions.style.display = 'none';
            }

            // Add user message
            addMessage(message, 'user');

            // Show typing indicator
            showTypingIndicator();

            try {
                // Call API
                const response = await fetch('http://localhost:8000/api/support/query', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message: message })
                });

                if (!response.ok) {
                    throw new Error(`API error: ${response.status}`);
                }

                const data = await response.json();
                removeTypingIndicator();

                if (data.success && data.data) {
                    const botResponse = data.data;
                    addMessage(botResponse.answer, 'bot', botResponse);
                } else {
                    addMessage('Sorry, I could not process your request. Please try again.', 'bot', { 
                        error: true 
                    });
                }
            } catch (error) {
                removeTypingIndicator();
                console.error('Error:', error);
                addMessage(
                    'Connection error. Make sure the backend server is running on http://localhost:8000',
                    'bot',
                    { error: true }
                );
            }

            messageInput.focus();
        }

        function addMessage(text, sender, metadata = {}) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${sender}`;

            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            contentDiv.textContent = text;

            messageDiv.appendChild(contentDiv);

            if (metadata && metadata.category) {
                const infoDiv = document.createElement('div');
                infoDiv.className = 'bot-info' + (metadata.error ? ' error-message' : '');
                
                let categoryLabel = metadata.category.replace(/_/g, ' ').toUpperCase();
                let categoryEmoji = {
                    'ORDER_STATUS': '📦',
                    'STOCK_AVAILABILITY': '📊',
                    'UNKNOWN': '❓'
                }[metadata.category] || '💬';
                
                infoDiv.textContent = `${categoryEmoji} ${categoryLabel}`;
                messageDiv.insertBefore(infoDiv, contentDiv);
            }

            const timeDiv = document.createElement('div');
            timeDiv.className = 'message-time';
            const now = new Date();
            timeDiv.textContent = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
            messageDiv.appendChild(timeDiv);

            chatMessages.appendChild(messageDiv);
            scrollToBottom();
        }

        function showTypingIndicator() {
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message bot';
            messageDiv.id = 'typing-indicator';

            const typingDiv = document.createElement('div');
            typingDiv.className = 'typing-indicator';
            for (let i = 0; i < 3; i++) {
                const dot = document.createElement('div');
                dot.className = 'typing-dot';
                typingDiv.appendChild(dot);
            }

            messageDiv.appendChild(typingDiv);
            chatMessages.appendChild(messageDiv);
            scrollToBottom();
        }

        function removeTypingIndicator() {
            const indicator = document.getElementById('typing-indicator');
            if (indicator) {
                indicator.remove();
            }
        }

        function scrollToBottom() {
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
