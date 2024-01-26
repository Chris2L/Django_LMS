from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json
from icecream import ic


from .models import CourseFormatChoices, Course, CourseUserProgress, Score

@login_required
def index_12(request, course_progress: CourseUserProgress):

    # scorm/1/123/media/courses/SCORM_12/golf/shared/launchpage.html
    # The problem here is that the first part should be from the base
    context = {
        'course_id': course_progress.course.pk,
        'course_path': course_progress.course.index,
        'lesson_location': course_progress.lesson_location,
        'total_time': '01:17:45.05',
        'student_id': course_progress.user.pk,
        'student_name': course_progress.user.username,
        'lesson_status': course_progress.lesson_status, # completed passed incomplete
        'score': json.dumps({
                  "raw": str(course_progress.score.raw),
                  "min": str(course_progress.score.min),
                  "max": str(course_progress.score.max)
                  }),
    }
    return render(request,'scorm_player_12.html', context=context)


def save_scorm_12(course, json_object):
    try:
        user_id = int(json_object["cmi"]["core"]["student_id"])
        ic(user_id)
        user = get_object_or_404(User, pk=user_id)
        course_progress = CourseUserProgress.objects.get(course=course, user=user)

        ic(course_progress)
    except Exception as e:
        ic(e)
        return HttpResponse(status=200, content="{}")

    try:
        current_location = int(json_object["cmi"]["core"]["lesson_location"])
        course_progress.lesson_location = current_location
        ic(f"Setting lesson loc to {current_location}")
    except Exception as e:
        ic(e)

    try:
        lesson_status = json_object["cmi"]["core"]["lesson_status"]
        course_progress.lesson_status = lesson_status
        ic(f"Setting lesson_status to {lesson_status}")
    except Exception as e:
        ic(e)

    try:
        exit = json_object["cmi"]["core"]["exit"]
        course_progress.exit_status = exit
        ic(f"Setting exit to {exit}")
    except Exception as e:
        ic(e)

    try:
        min = float(json_object["cmi"]["core"]["score"]["min"])
        course_progress.score.min = min
        ic(f"Setting course_progress.score.min to {min}")
    except Exception as e:
        course_progress.score.min = 0
        ic(e)

    try:
        max = float(json_object["cmi"]["core"]["score"]["max"])
        course_progress.score.max = max
        ic(f"Setting course_progress.score.max to {max}")
    except Exception as e:
        course_progress.score.max = 0
        ic(e)

    try:
        raw = float(json_object["cmi"]["core"]["score"]["raw"])
        course_progress.score.raw = raw
        ic(f"Setting course_progress.score.raw to {raw}")
    except Exception as e:
        course_progress.score.raw = 0
        ic(e)

    course_progress.score.save()

    course_progress.save()
    json_formatted_str = json.dumps(json_object, indent=2)

    print(json_formatted_str)

    return HttpResponse(status=200, content="{}")


@login_required
def index_2004(request, course_progress: CourseUserProgress):
    context = {
        'course_id': course_progress.course.pk,
        'course_path': course_progress.course.index,
        'lesson_location': 3,
        'student_id': course_progress.user.pk,
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
        # 'suspend_data': '23Ym6070u0v0w0x0y0z0A0B0C0~201$1001815T0101201112010150111501215013150141501515016150171501815~2o1d_3004000000001^1^1^1^1^1^1^1^1^1^101^10111^1^1^1^1^v_player.5lSe4axgifT.6RhxXG1cuH41^1^00000~2_U~218j3rA5210b101001a1a103e85~2F634003400g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000r78010141^h_default_Selectedg680101^8_defaultr78010141^h_default_Selected3400g620101^8_default3400g600101^8_default340034003400SR2WfL34003400340034003400q70020181^g_default_Visited0021200~2k8j3xB3210b101001a1a103vU2~2Z63400r78010141^h_default_Selectedr78010141^h_default_Selectedr78010141^h_default_Selected3400g620101^8_default34003400n70010107Correct7Correct55400030003440g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default340034003400TS3yw0L34003400340034003400q70020181^g_default_Visited00000~2M7l3WKl41112b101001a1a113dqd~2n6g680101^8_defaultr78010141^h_default_Selectedg680101^8_default3400g620101^8_default34003400n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default34403000300034003400TS38e1L34003400340034003400q70020181^g_default_Visited00000~218j3ZO5210b101001a1a103bl5~2H6r78010141^h_default_Selectedg680101^8_defaultr78010141^h_default_Selected3400g620101^8_default34003400n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default34403000300034003400SR2rgL34003400340034003400q70020181^g_default_Visited00000~2$7j3pI9210b101001a1a123x99~2F6r78010141^h_default_Selectedg680101^8_defaultg680101^8_default3400g620101^8_default34003400n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default34403000300034003400SR2OkL34003400340034003400q70020181^g_default_Visited00000~288j3_f6210b101001a1a123hG5~2O6r78010141^h_default_Selectedg680101^8_defaultg680101^8_default3400g620101^8_default34003400n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default34403000300034003400SR2_oL34003400340034003400q70020181^g_default_Visited00000~2h8j3tx3210b101001a1a1137W2~2X6g680101^8_defaultr78010141^h_default_Selectedg680101^8_default3400g620101^8_default34003400n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440n70010107Correct7Correct55400030003440g600101^8_default344030003000g600101^8_default344030003000g600101^8_default344030003000g600101^8_default34403000300034003400SR2upL34003400340034003400q70020181^g_default_Visited00000000002000',
    }
    return render(request,'scorm_player_2004.html', context=context)


def save_scorm_2004(course, json_object):
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





@login_required
def index(request, course_id):
    user = request.user
    ic(user)
    ic(user.id)
    course = get_object_or_404(Course, pk=course_id)

    try:
        course_progress = CourseUserProgress.objects.get(course=course, user=user)

        if course_progress.score is None:
            course_progress.score = Score()
            course_progress.score.save()

        course_progress.save()

        ic(course_progress.lesson_location)
    except CourseUserProgress.DoesNotExist:
        course_progress = CourseUserProgress(course=course, user=user)
        course_progress.score = Score()
        course_progress.score.save()
        course_progress.save()

    except Exception as e:
        ic(e)

    if course.format == CourseFormatChoices.SCORM_12:
        return index_12(request, course_progress)
    elif course.format == CourseFormatChoices.SCORM_2004:
        return index_2004(request, course_progress)
    

@login_required
def save_scorm(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    json_object = json.loads(request.body)

    if course.format == CourseFormatChoices.SCORM_12:
        return save_scorm_12(course, json_object)
    elif course.format == CourseFormatChoices.SCORM_2004:
        return save_scorm_2004(course, json_object)