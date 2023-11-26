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
        'suspend_data': '23Ym6070u0v0w0x0y0z0A0B0C0~201$1001815T0101201112010150111501215013150141501515016150171501815~2o1d_3004000000001^1^1^1^1^1^1^1^1^1^101^10111^1^1^1^1^v_player.5lSe4axgifT.6RhxXG1cuH41^1^00000~2_U~218j3rA5210b101001a1a103e85~2F634003400g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000r78010141^h_default_Selectedg680101^8_defaultr78010141^h_default_Selected3400g620101^8_default3400g600101^8_default340034003400SR2WfL34003400340034003400q70020181^g_default_Visited0021200~2k8j3xB3210b101001a1a103vU2~2Z63400r78010141^h_default_Selectedr78010141^h_default_Selectedr78010141^h_default_Selected3400g620101^8_default34003400n70010107Correct7Correct55400030003440g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default340034003400TS3yw0L34003400340034003400q70020181^g_default_Visited00000~2M7l3WKl41112b101001a1a113dqd~2n6g680101^8_defaultr78010141^h_default_Selectedg680101^8_default3400g620101^8_default34003400n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default34403000300034003400TS38e1L34003400340034003400q70020181^g_default_Visited00000~218j3ZO5210b101001a1a103bl5~2H6r78010141^h_default_Selectedg680101^8_defaultr78010141^h_default_Selected3400g620101^8_default34003400n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default34403000300034003400SR2rgL34003400340034003400q70020181^g_default_Visited00000~2$7j3pI9210b101001a1a123x99~2F6r78010141^h_default_Selectedg680101^8_defaultg680101^8_default3400g620101^8_default34003400n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default34403000300034003400SR2OkL34003400340034003400q70020181^g_default_Visited00000~288j3_f6210b101001a1a123hG5~2O6r78010141^h_default_Selectedg680101^8_defaultg680101^8_default3400g620101^8_default34003400n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default34403000300034003400SR2_oL34003400340034003400q70020181^g_default_Visited00000~2h8j3tx3210b101001a1a1137W2~2X6g680101^8_defaultr78010141^h_default_Selectedg680101^8_default3400g620101^8_default34003400n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default34403000300034003400SR2upL34003400340034003400q70020181^g_default_Visited00000000002000',
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