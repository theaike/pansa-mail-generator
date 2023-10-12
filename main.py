from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def drone_flight_form():
    if request.method == 'POST':
        imie_nazwisko = request.form['imie_nazwisko']
        numer_telefonu = request.form['numer_telefonu']
        wspolrzedne = request.form['wspolrzedne']
        wysokosc_lotu = request.form['wysokosc_lotu']
        promien_okregu = request.form['promien_okregu']
        czas_rozpoczecia = request.form['czas_rozpoczecia']
        czas_zakonczenia = request.form['czas_zakonczenia']


        return f"Odbiorca: utm@pansa.pl <br> Temat: Zgłoszenie lotu BSP <br> Dane zgłoszenia: <br> Imię i nazwisko pilota: {imie_nazwisko} <br> Numer telefonu: {numer_telefonu} <br> Współrzędne WGS-84: {wspolrzedne} <br> Wysokość lotu: {wysokosc_lotu} metrów AGL <br> Promień okręgu: {promien_okregu} metrów <br> Czas rozpoczęcia: {czas_rozpoczecia} <br> Czas zakończenia: {czas_zakonczenia}"

    return render_template('flight_form.html')

if __name__ == '__main__':
    app.run(debug=True)
