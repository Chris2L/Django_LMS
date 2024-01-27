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
        'lesson_location': course_progress.suspend_data or 0,
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
        course_progress.suspend_data = str(current_location)
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
        'suspend_data': course_progress.suspend_data
        }
    return render(request,'scorm_player_2004.html', context=context)


def save_scorm_2004(course, json_object):
    # ic(json_object["cmi"])
    # ic(json_object["cmi"]['learner_id'])
    # ic(json_object["cmi"]['completion_status']) # incomplete
    # ic(json_object["cmi"]['score']['min'])
    # ic(json_object["cmi"]['score']['max'])
    # ic(json_object["cmi"]['score']['raw'])
    # ic(json_object["cmi"]['score']['scaled'])

    # ic(json_object["cmi"]['suspend_data'])
    # ic(json_object["cmi"]['success_status']) # unknown / failed / passed

    # Use this data just not print for now
    # ic(json_object["cmi"]['suspend_data'])

    # try:
    #     ic(json_object["cmi"]['progress_measure'])
    # except:
    #     ic("No progress_measure")


    # try:
    #     for interaction in json_object["cmi"]['interactions']:
    #         try:
    #             ic(f"========== Interaction {interaction} ===============")
    #             ic(json_object["cmi"]['interactions'][interaction]["id"])
    #             ic(json_object["cmi"]['interactions'][interaction]["learner_response"])
    #             ic(json_object["cmi"]['interactions'][interaction]["latency"])
    #             ic(json_object["cmi"]['interactions'][interaction]["objectives"])
    #             ic(json_object["cmi"]['interactions'][interaction]["result"])
    #             ic(json_object["cmi"]['interactions'][interaction]["weighting"])

    #         except:
    #             ic(f"error for interactions[{interaction}]")
    # except:
    #     ic("no interaction")

    # try:
    #     for objective in json_object["cmi"]['objectives']:
    #         try:
    #             ic(f"========== Objective {objective} ===============")
    #             ic(json_object["cmi"]['objectives'][objective]["id"])
    #             ic(json_object["cmi"]['objectives'][objective]["completion_status"])
    #             ic(json_object["cmi"]['objectives'][objective]["progress_measure"])
    #             ic(json_object["cmi"]['objectives'][objective]["success_status"])
    #             ic(json_object["cmi"]['objectives'][objective]["success_status"])
    #             ic(json_object["cmi"]['objectives'][objective]['score']['min'])
    #             ic(json_object["cmi"]['objectives'][objective]['score']['max'])
    #             ic(json_object["cmi"]['objectives'][objective]['score']['raw'])
    #             ic(json_object["cmi"]['objectives'][objective]['score']['scaled'])

    #         except:
    #             ic("objective[id]")
    # except:
    #     ic("no objectives")




    
    try:
        user_id = int(json_object["cmi"]['learner_id'])
        ic(user_id)
        user = get_object_or_404(User, pk=user_id)
        course_progress = CourseUserProgress.objects.get(course=course, user=user)

        ic(course_progress)
    except Exception as e:
        ic(e)
        return HttpResponse(status=200, content="{}")

    try:
        current_location = json_object["cmi"]['suspend_data']
        course_progress.suspend_data = current_location
        ic(f"Setting lesson loc to {current_location}")
    except Exception as e:
        ic(e)

    try:
        lesson_status = json_object["cmi"]['success_status']
        course_progress.lesson_status = lesson_status
        ic(f"Setting lesson_status to {lesson_status}")
    except Exception as e:
        ic(e)

    try:
        exit = json_object["cmi"]["exit"]
        course_progress.exit_status = exit
        ic(f"Setting exit to {exit}")
    except Exception as e:
        ic(e)

    try:
        min = float(json_object["cmi"]["score"]["min"])
        course_progress.score.min = min
        ic(f"Setting course_progress.score.min to {min}")
    except Exception as e:
        course_progress.score.min = 0
        ic(e)

    try:
        max = float(json_object["cmi"]["score"]["max"])
        course_progress.score.max = max
        ic(f"Setting course_progress.score.max to {max}")
    except Exception as e:
        course_progress.score.max = 0
        ic(e)

    try:
        raw = float(json_object["cmi"]["score"]["raw"])
        course_progress.score.raw = raw
        ic(f"Setting course_progress.score.raw to {raw}")
    except Exception as e:
        course_progress.score.raw = 0
        ic(e)

    course_progress.score.save()

    course_progress.save()

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