<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Eingabewerte bereinigen
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

    // Hier kannst du die Daten speichern, z.B. in eine Datenbank oder per E-Mail versenden
    echo "Name: $name, Email: $email, Nachricht: $message";

    // Optional: Rückmeldung an den Benutzer geben
    // z.B. echo json_encode(["status" => "success", "message" => "Formular erfolgreich gesendet!"]);
}
?>
