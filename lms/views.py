from django.shortcuts import render
from django.http import QueryDict, HttpResponseRedirect, HttpResponse
import json


def index(request):
    return render(request, "index.html")


def save_scorm(request):
    json_object = json.loads(request.body)

    json_formatted_str = json.dumps(json_object, indent=2)

    print(json_formatted_str)

    return HttpResponse(status=200, content="{}")