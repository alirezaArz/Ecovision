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

    function sendCommand(code, status = null, triggerElement = null, params = null) { // Added params argument
        const payload = { 'code': code };
        if (status !== null) {
            payload['status'] = status ? 'on' : 'off';
        }
        // Only include params if they exist
        if (params) {
            payload['params'] = params;
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
            alert(`failed to send request with the error of :${code}: ${error.message}`); // Keep error alerts for other types of errors
        });
    }

    // --- Event Listeners for Buttons ---

    // Toggle Switches (Global Snail and others)
    toggleSwitches.forEach(toggle => {
        toggle.addEventListener('change', function(event) {
            const dataCode = this.dataset.code;
            const isChecked = this.checked;
            let params = null;

            // If the toggle is being turned ON, get the parameters
            if (isChecked) {
                const numberInput = document.getElementById(`number-input-${dataCode}`);
                const unitSelect = document.getElementById(`time-unit-select-${dataCode}`);

                if (numberInput && unitSelect && numberInput.value && numberInput.value.trim() !== '') {
                    params = {
                        number: numberInput.value,
                        unit: unitSelect.value
                    };
                }
            }
            
            // Send command with status and potentially params
            sendCommand(dataCode, isChecked, this, params); 
        });
    });

    // Action Buttons (e.g., Instant Run)
    actionButtons.forEach(button => {
        button.addEventListener('click', function() {
            const dataCode = this.dataset.code;
            // No params needed for global instant run
            sendCommand(dataCode, null, this); 
        });
    });

    // Individual Run Buttons
    runButtons.forEach(button => {
        button.addEventListener('click', function() {
            const dataCode = this.dataset.code;
            // The run button no longer sends parameters. It just triggers the run.
            // The parameters are set when the toggle is activated.
            sendCommand(dataCode, null, this); 

            // Visual feedback: change color for a short period
            this.classList.add('active-feedback');
            setTimeout(() => {
                this.classList.remove('active-feedback');
            }, RUN_BUTTON_FEEDBACK_DURATION_MS);
        });
    });
});
