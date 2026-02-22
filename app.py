import os
from flask import Flask, render_template, request

# Povieme Flasku, kde presne hladat HTML subory
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    vysledok = None
    if request.method == 'POST':
        try:
            # Nacitame hodnoty z formulara
            hrubka = float(request.form.get('hrubka', 0))
            polomer = float(request.form.get('polomer', 0))
            uhol = float(request.form.get('uhol', 0))
            
            # Tvoj zakladny vypocet (upravime neskor podla tvojej praxe)
            vysledok = round((hrubka + polomer) * (uhol / 90), 2)
        except:
            vysledok = "Chyba: Zadaj správne čísla"
            
    return render_template('index.html', vysledok=vysledok)

if __name__ == '__main__':
    # Nastavenie portu, aby Render vedel aplikaciu spustit
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
