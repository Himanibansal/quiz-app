from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import JsonResponse

# Create your views here.
def get_quiz(request):
    queryset=quiz.objects.all()
    return render(request,"quiz.html",{'queryset':queryset})

# def question(request,id):
#     queryset=Question.objects.filter(quiz_id=id)
#     queryset2=Options.objects.filter(Question_id=Question__quiz_id)
#     return render(request,"questions.html",{'queryset':queryset, 'queryset2': queryset2})

def question(request, quiz_id):
    # Get the quiz instance or return a 404 error if not found
    quiz_instance = get_object_or_404(quiz, id=quiz_id)

    # Get questions associated with the quiz
    questions = Question.objects.filter(quiz_id=quiz_instance)

    # Get options for each question
    options_dict = {}
    for question in questions:
        options_dict[question.id] = Options.objects.filter(Question_id=question)

    return render(request, "questions.html", {'quiz': quiz_instance, 'questions': questions, 'options_dict': options_dict})

def calculate_score(request, question_id):
    selected_option_id = request.POST.get('selected_option')
    selected_option = Options.objects.get(id=selected_option_id)

    is_correct = selected_option.isanswer
    score = 1 if is_correct else 0

    # Update the score for the question
    question = get_object_or_404(Question, id=question_id)
    question.score += score
    question.save()

    # Return the calculated score to update the front end
    return JsonResponse({'score': score})