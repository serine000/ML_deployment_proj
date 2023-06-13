"""
    This module is responsible for the web interface of the application using flask
"""
from flask import Flask, request, render_template

from src.pipeline.predict_pipeline import CustomDataObject, PredictPipeline

app = Flask(__name__)


# Homepage route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods = ['GET', 'POST'])
def predict_input_data():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomDataObject()
        data.gender = request.form['gender']
        data.race_ethnicity = request.form['ethnicity']
        data.parental_level_of_education = request.form['parental_level_of_education']
        data.lunch = request.form['lunch']
        data.test_preparation_course = request.form['test_preparation_course']
        data.reading_score = int(request.form['reading_score'])
        data.writing_score = int(request.form['writing_score'])

        prediction_pipeline = PredictPipeline(data)
        prediction_dataframe = prediction_pipeline.prepare_prediction_data()
        results = prediction_pipeline.predict(prediction_dataframe)
        return render_template('home.html', results = results[0])


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5005, debug = True)
