<!DOCTYPE html>
<html lang="sk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kalkulačka Ohýbania</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f9; display: flex; justify-content: center; padding: 50px; }
        .box { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); width: 320px; text-align: center; }
        input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
        .vysledok { margin-top: 20px; padding: 15px; background: #e2f3e5; color: #2e7d32; font-weight: bold; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Step Bending</h2>
        <form method="POST">
            <input type="number" step="any" name="hrubka" placeholder="Hrúbka plechu (mm)" required>
            <input type="number" step="any" name="polomer" placeholder="Polomer (R)" required>
            <input type="number" step="any" name="uhol" placeholder="Uhol ohybu (°)" required>
            <button type="submit">VYPOČÍTAŤ</button>
        </form>

        {% if vysledok %}
            <div class="vysledok">
                Výsledok: {{ vysledok }} mm
            </div>
        {% endif %}
    </div>
</body>
</html>
