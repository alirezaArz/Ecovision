document.addEventListener('DOMContentLoaded', function() {
    // --- Configuration ---
    const CONTROL_ENDPOINT = '/admin/control/'; // Endpoint for sending toggle/run commands
    const RUN_BUTTON_FEEDBACK_DURATION_MS = 1000; // How long run button stays active (1 second)

    // --- DOM Elements ---
    const toggleSwitches = document.querySelectorAll('.toggle-switch input[type="checkbox"]');
    const actionButtons = document.querySelectorAll('.action-button'); // For Instant Run button
    const runButtons = document.querySelectorAll('.run-button'); // For individual run buttons

    // --- Utility Functions ---
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function sendCommand(code, status = null, triggerElement = null) { // Added triggerElement for context
        const payload = { 'code': code };
        if (status !== null) {
            payload['status'] = status ? 'on' : 'off';
        }

        fetch(CONTROL_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(payload)
        })
        .then(response => {
            if (!response.ok) {
                const contentType = response.headers.get("content-type");
                if (contentType && contentType.indexOf("application/json") !== -1) {
                    return response.json().then(errorData => {
                        throw new Error(`HTTP error! Status: ${response.status}, Message: ${errorData.message || 'Unknown error'}`);
                    });
                } else {
                    return response.text().then(text => {
                        throw new Error(`HTTP error! Status: ${response.status}, Raw Response: ${text.substring(0, 100)}...`);
                    });
                }
            }
            return response.json();
        })
        .then(data => {
            console.log('Command Success:', data);
            // No alert for success
        })
        .catch((error) => {
            console.error('Command Error:', error);
            // Revert toggle state if it was a toggle button and failed
            if (status !== null && triggerElement && triggerElement.type === 'checkbox') {
                triggerElement.checked = !status; // Revert the specific checkbox that triggered the event
            }
            alert(`خطا در ارسال درخواست با کد ${code}: ${error.message}`); // Keep error alerts for other types of errors
        });
    }

    // --- Event Listeners for Buttons ---

    // Toggle Switches (Global Snail and others)
    toggleSwitches.forEach(toggle => {
        toggle.addEventListener('change', function(event) {
            const dataCode = this.dataset.code;
            const isChecked = this.checked;
            sendCommand(dataCode, isChecked, this); // Pass 'this' as triggerElement
        });
    });

    // Action Buttons (e.g., Instant Run)
    actionButtons.forEach(button => {
        button.addEventListener('click', function() {
            const dataCode = this.dataset.code;
            sendCommand(dataCode, null, this); // Pass 'this' as triggerElement
        });
    });

    // Individual Run Buttons
    runButtons.forEach(button => {
        button.addEventListener('click', function() {
            const dataCode = this.dataset.code;
            sendCommand(dataCode, null, this); // Pass 'this' as triggerElement

            // Visual feedback: change color for a short period
            this.classList.add('active-feedback');
            setTimeout(() => {
                this.classList.remove('active-feedback');
            }, RUN_BUTTON_FEEDBACK_DURATION_MS);
        });
    });
});