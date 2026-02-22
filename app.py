import os
import math
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    vysledok = None
    if request.method == 'POST':
        try:
            hrubka = float(request.form.get('hrubka', 0))
            polomer = float(request.form.get('polomer', 0))
            uhol = float(request.form.get('uhol', 0))
            pocet_krokov = int(request.form.get('pocet_krokov', 1))

            dlzka_obluka = (math.pi * (polomer + hrubka/2) * uhol) / 180
            posuv = dlzka_obluka / pocet_krokov
            
            vysledok = {
                'dlzka': round(dlzka_obluka, 2),
                'posuv': round(posuv, 2),
                'uhol_kroku': round(uhol / pocet_krokov, 2)
            }
        except Exception as e:
            vysledok = f"Chyba: {e}"
            
    return render_template('index.html', vysledok=vysledok)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
