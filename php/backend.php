<?php
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $requestData = json_decode(file_get_contents('php://input'), true);

    if ($requestData && isset($requestData['action']) && $requestData['action'] === 'stop_program') {
        // Insérez ici le code pour arrêter le programme sur votre machine.
        // Exemple : shell_exec('killall program_name');
        // Réponse de confirmation
        echo json_encode(['success' => true,'message' => $_SERVER['HTTP_ORIGIN']]);
        exit;
    }
}

// Réponse d'erreur par défaut
echo json_encode(['error' => 'Invalid request']);
