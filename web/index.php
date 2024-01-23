<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Control Panel</title>
</head>
<body>
    <h1>Control Panel</h1>
    <button onclick="stopProgram()">Stop Program</button>

    <script>
        function stopProgram() {
            // Faites une requête Ajax vers votre backend (PHP)
            // Exemple avec fetch :
            fetch('http://localhost:5000/backend.php', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ action: 'stop_program' }),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Réponse du serveur:', data);
            })
            .catch(error => {
                console.error('Erreur lors de la requête:', error);
            });
        }
    </script>
</body>
</html>
