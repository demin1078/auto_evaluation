from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    car_description = "Краткое описание автомобиля. Это отличный выбор для городских поездок."
    full_description = "Развернутое описание автомобиля. Этот автомобиль обладает высокой экономичностью и комфортом."
    return render_template('index.html', 
                           car_description=car_description, 
                           full_description=full_description)

if __name__ == '__main__':
    app.run(debug=True)
