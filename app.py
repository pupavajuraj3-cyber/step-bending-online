from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    vysledok = None
    if request.method == 'POST':
        try:
            hrubka = float(request.form.get('hrubka', 0))
            polomer = float(request.form.get('polomer', 0))
            uhol = float(request.form.get('uhol', 0))
            vysledok = round((hrubka + polomer) * (uhol / 90), 2)
        except:
            vysledok = "Chyba: Zadaj správne čísla"
    return render_template('index.html', vysledok=vysledok)

if __name__ == '__main__':
    # Tato cast je klucova pre Render:
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
