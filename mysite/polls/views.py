import os
from django.shortcuts import render
import json

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

import tensorflow as tf

def index(request):
    return render(request, 'index.html', {})


def get_all_music(request):
    file_name_list = os.listdir('polls/resources')
    print(file_name_list)
    file_list_as_json = json.dumps(file_name_list)
    return HttpResponse(file_list_as_json, content_type="application/json")

def music(request):
    file_name = request.path.split('/')[-1]
    print("received request for music file " + file_name)
    data = None
    file_name = 'polls/resources/' + file_name
    with open(file_name, 'rb') as f:
        data = f.read()
    return HttpResponse(data)



