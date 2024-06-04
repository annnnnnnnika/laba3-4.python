import math
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    show_calc_button = False
    if request.method == 'POST':
        figure = request.form['figure']
        accuracy = int(request.form['accuracy'])
        if figure == 'cube':
            side = int(request.form['side'])
            volume = side ** 3
        elif figure == 'sphere':
            radius = int(request.form['radius'])
            volume = (4 / 3) * math.pi * radius ** 3
        elif figure == 'cone':
            radius = int(request.form['radius'])
            height = int(request.form['height'])
            volume = (1 / 3) * math.pi * radius ** 2 * height
        elif figure == 'cylinder':
            radius = int(request.form['radius'])
            height = int(request.form['height'])
            volume = math.pi * radius ** 2 * height
        else:
            return render_template('index.html',figure='Неверный тип фигуры')
        if 'accuracy' not in request.form:
            volume = volume
        else:
            volume = round(volume, accuracy)
        return render_template('result.html', volume=volume)
    else:
        return render_template('index.html', figure=None, side=None, show_calc_button=show_calc_button)


if __name__ == '__main__':
    app.run()

app.run(debug=True)
def cube_volume_calc(side, accuracy):
    alert = "error"
    if (type(side)!=int or type(accuracy)!=int or side==None or accuracy == None ):
        return alert
    volume = side ** 3
    return round(volume, accuracy)
def sphere_volume_calc( radius, accuracy):
    alert = "error"
    if (type(radius)!=int or type(accuracy)!=int or radius==None or accuracy == None ):
        return alert
    volume = (4 / 3) * math.pi * radius ** 3
    return round(volume, accuracy)
def cone_cylinder_volume_calc(figure, radius, height, accuracy):
    alert = "error"
    volume = None
    if (type(radius) != int or type(accuracy) != int or type(height) != int or radius == None or accuracy == None or figure==None or height == None):
        return alert
    if figure == 'cone':
        volume = (1 / 3) * math.pi * radius ** 2 * height
    if figure == 'cylinder':
        volume = math.pi * radius ** 2 * height
    return round(volume, accuracy)

