from flask import Flask
import random

app = Flask(__name__)

datos=["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
       'Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.',
       'El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna',
       'Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo',
       'Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo',
       'Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos',
       'Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas']


@app.route("/")
def hello_world():
    return '<h1>Hola silvana</h1>' '<a href="/factou">¡Aqui hay datos aleatorios de las dependencias a la tecnologia</a>'
@app.route("/factou")
def datitos():
    return f'<p>{random.choice(datos)}</p>' '<a href="/coin">Aqui puedes lanzar una moneda</a>'
@app.route("/coin")
def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
    
app.run(debug=True)
