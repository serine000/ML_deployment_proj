# End to End Machine Learning Project

This project is about building a full ML project with its entire pipeline from development to deployment. 

## Steps to launch the pipeline

1. Start by creating a virtual python environment. To do so, run the following instructions:
```
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

Note: You can exit from this environment later by running `deactivate` in your terminal.

2. Launch the setup.py file by running the instruction below to download all necessary requirements and dependencies into your virtual environment. This also build the entire project and turns it into a package.
```
pip3 install .
```

3. At any moment of you update the README library and need to download the new packages, run the 
    below instruction when inside your virtual environment terminal:
```
pip3 install -r requirements.txt
```

4. To run the local training pipeline and have the model and preprocessor artifacts saved,
run the following command in your terminal:
```
python3 main.py
```
This will trigger training your data and save the artifacts.

5. To run the flask web app to use our model there run:
```angular2html
python3 app.py
```
and open `localhost:5005` in your browser, this will give you the landing page of the application.
Go to `localhost:5005/predictdata` to perform a data prediction and view your results in the web browser.