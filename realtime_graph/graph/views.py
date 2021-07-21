from django.shortcuts import render
from django.contrib import messages
import pickle
import numpy as np

model =pickle.load(open("EEG.sav",'rb'))

# Create your views here.
def index(request):
    return render(request,'base.html',context={'text':'HElloworld'})

def ml_model(request):
    if request.method =="POST":
        channel1 = request.POST['one']
        channel2 = request.POST['two']
        channel3 = request.POST['three']
        channel4 = request.POST['four']
        features = [float(i) for i in (channel1,channel2,channel3,channel4)]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        return render(request,'machine.html',prediction_text=prediction)
        
        # messages.success(request , "Your messages has been sent!!")



    return render(request,'machine.html')