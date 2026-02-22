from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    vysledok = None
    if request.method == 'POST':
        try:
            # Tu sa spracujú hodnoty z tvojho formulára
            hrubka = float(request.form.get('hrubka', 0))
            polomer = float(request.form.get('polomer', 0))
            uhol = float(request.form.get('uhol', 0))
            
            # Tvoj vzorec (upravíme neskôr, ak bude treba)
            vysledok = (hrubka + polomer) * (uhol / 90)
            vysledok = round(vysledok, 2)
        except Exception as e:
            vysledok = "Chyba: Zadaj správne čísla"
    
    return render_template('index.html', vysledok=vysledok)

if __name__ == '__main__':
    app.run(debug=True)
