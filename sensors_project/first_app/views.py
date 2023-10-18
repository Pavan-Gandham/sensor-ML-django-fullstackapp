from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import pickle

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


@csrf_exempt
def sensors_pre(request):
    template = loader.get_template('index.html')
    maxtemp = request.POST.get("tmax")
    mintemp = request.POST.get("tmin")
    rhi = request.POST.get("rhi")
    rf = request.POST.get("rf")
    rhii = request.POST.get("rhii")
    ssh = request.POST.get("ssh")

    sensors_data = [
        [maxtemp, mintemp, rhi, rf, rhii, ssh]]
    sensors_model = pickle.load(open('ranfor.pkl', 'rb'))
    prediction = sensors_model.predict(
        [[maxtemp, mintemp, rhi, rf, rhii, ssh]])



    return HttpResponse(template.render({'result':prediction}))
