# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:49:44 2022

@author: anusuyababy
"""

from flask import Flask, render_template, request
from strsimpy.cosine import Cosine
import pickle
import numpy as np
import pandas as pd
import time

app = Flask(__name__)



@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    time.sleep(6)
    return render_template('table.html')
    


if __name__=="__main__":
    app.run(debug=True)
