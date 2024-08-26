document.getElementById('generateUsernameBtn').addEventListener('click', function() {
    fetch('/generate_username')
        .then(response => response.json())
        .then(data => document.getElementById('username').value = data.username);
});
