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
        # 'course_path': '/media/courses/PlayTheGame_2004/RuntimeBasicCalls_SCORM20043rdEdition/shared/launchpage.html',
        # 'course_path': '/media/courses/PlayTheGame_2004/RunTimeAdvancedCalls_SCORM20043rdEdition/shared/launchpage.html',
        'course_path': '/media/courses/PlayTheGame_2004/aca_2022_scorm2004_passed-incomplete_en-us/index_lms.html',
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
        #  'objectives': json.dumps({
        #        '0': {'id': 'obj_etiquette',},
        #        '1': {'id': 'obj_handicapping',},
        #        '2': {'id': 'obj_havingfun',},
        #        '3': {'id': 'obj_playing',},
        #  })
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

    # Use this data just not print for now
    # ic(json_object["cmi"]['suspend_data'])

    try:
        ic(json_object["cmi"]['progress_measure'])
    except:
        ic("No progress_measure")


    try:
        for interaction in json_object["cmi"]['interactions']:
            try:
                ic(f"========== Interaction {interaction} ===============")
                ic(json_object["cmi"]['interactions'][interaction]["id"])
                ic(json_object["cmi"]['interactions'][interaction]["learner_response"])
                ic(json_object["cmi"]['interactions'][interaction]["latency"])
                ic(json_object["cmi"]['interactions'][interaction]["objectives"])
                ic(json_object["cmi"]['interactions'][interaction]["result"])
                ic(json_object["cmi"]['interactions'][interaction]["weighting"])

            except:
                ic(f"error for interactions[{interaction}]")
    except:
        ic("no interaction")

    try:
        for objective in json_object["cmi"]['objectives']:
            try:
                ic(f"========== Objective {objective} ===============")
                ic(json_object["cmi"]['objectives'][objective]["id"])
                ic(json_object["cmi"]['objectives'][objective]["completion_status"])
                ic(json_object["cmi"]['objectives'][objective]["progress_measure"])
                ic(json_object["cmi"]['objectives'][objective]["success_status"])
                ic(json_object["cmi"]['objectives'][objective]["success_status"])
                ic(json_object["cmi"]['objectives'][objective]['score']['min'])
                ic(json_object["cmi"]['objectives'][objective]['score']['max'])
                ic(json_object["cmi"]['objectives'][objective]['score']['raw'])
                ic(json_object["cmi"]['objectives'][objective]['score']['scaled'])

            except:
                ic("objective[id]")
    except:
        ic("no objectives")

#     json_formatted_str = json.dumps(json_object, indent=2)

#     print(json_formatted_str)

    return HttpResponse(status=200, content="{}")