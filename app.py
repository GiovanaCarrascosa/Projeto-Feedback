from flask import Flask

app = Flask (__name__)

# A partir daqui será as rotas.

@app.route ("/principal")

def pagina_principal():

    return "calcinha de onça";


app.run(debug=True)