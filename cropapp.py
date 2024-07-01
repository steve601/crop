from flask import Flask,render_template,request
from source.main_project.pipeline.predict_pipeline import UserData,PredicPipeline
import numpy as np

app = Flask(__name__)
label_to_int = {'rice': 0,
               'maize': 1,
          'pigeonpeas': 2,
           'mothbeans': 3,
            'mungbean': 4,
           'blackgram': 5,
              'lentil': 6,
         'pomegranate': 7,
              'banana': 8,
               'mango': 9,
         'watermelon': 10,
          'muskmelon': 11,
             'orange': 12,
             'papaya': 13,
            'coconut': 14,
             'cotton': 15,
               'jute': 16,
             'coffee': 17}

def find_key_by_value(d, value):
    for k, v in d.items():
        if v == value:
            return k
    return None 
@app.route('/')
def homepage():
    return render_template('crop.html')

@app.route('/recommend',methods=['POST'])
def do_prediction():
    data = UserData(
        N=request.form.get('N'),
        P=request.form.get('P'),
        K=request.form.get('K'),
        humidity=request.form.get('hum'),
        ph=request.form.get('ph'),
        rainfall=request.form.get('rain')
    )
    data = data.get_data_as_df()
    
    predict_pipe = PredicPipeline()
    result = predict_pipe.predict(data)
    key = find_key_by_value(label_to_int, result)
    msg = f'Recommended crop is; {key}'
    
    return render_template('crop.html',text=msg)

if __name__ == "__main__":
    app.run(debug=True)
    