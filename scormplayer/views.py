from django.shortcuts import render
from django.http import HttpResponse
import json
from icecream import ic


# Create your views here.
def index(request):
     context = {
          'lesson_location': 3,
          'total_time': '01:17:45.05',
          'student_id': "user1",
          'student_name': "John Doe",
          'lesson_status': 'incomplete', # completed passed incomplete
          'score': json.dumps({
                    "raw": '70',
                    "min": '0',
                    "max": '100'
                    }),
     }
     return render(request,'scorm_player_12.html', context=context)


def save_scorm(request):
    json_object = json.loads(request.body)

    ic(json_object["cmi"]["core"]["student_id"])

    json_formatted_str = json.dumps(json_object, indent=2)

    print(json_formatted_str)

    return HttpResponse(status=200, content="{}")


def index_2004(request):
     context = {
          'lesson_location': 3,
          'student_id': "user1",
          'student_name': "John Doe",
          'lesson_status': 'incomplete', # completed passed incomplete
          'scaled_passing_score': 0.5,
          'score': json.dumps({
                    "raw": '70',
                    "min": '0',
                    "max": '100',
                    "scaled": '0.7'
                    }),
     }
     return render(request,'scorm_player_2004.html', context=context)


def save_scorm_2004(request):
    json_object = json.loads(request.body)

    ic(json_object["cmi"])
    ic(json_object["cmi"]['learner_id'])
    ic(json_object["cmi"]['completion_status']) # incomplete
    ic(json_object["cmi"]['score']['min'])
    ic(json_object["cmi"]['score']['max'])
    ic(json_object["cmi"]['score']['raw'])
    ic(json_object["cmi"]['score']['scaled'])

    ic(json_object["cmi"]['success_status']) # unknown / failed / passed

#     json_formatted_str = json.dumps(json_object, indent=2)

#     print(json_formatted_str)

    return HttpResponse(status=200, content="{}")