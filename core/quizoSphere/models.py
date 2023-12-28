from django.db import models

class quiz(models.Model):
    quiz_name=models.CharField(max_length=100,unique=True)
    quiz_subject=models.CharField(max_length=100)
    no_of_quiz=models.IntegerField() 
    quiz_type=models.CharField(max_length=100)
    quiz_start_date=models.DateTimeField()
    quiz_end_date=models.DateTimeField()
    quiz_post_date=models.DateTimeField() 
    admin_name=models.CharField(max_length=100,default='admin')   

class Question(models.Model):
    quiz_id=models.ForeignKey(quiz, on_delete=models.CASCADE)
    value=models.TextField()

class Options(models.Model):
    Question_id=models.ForeignKey(Question,on_delete=models.CASCADE)
    bool_option=models.BooleanField()
    text_option=models.TextField()
    isanswer=models.BooleanField(default= False)
    score = models.IntegerField(default=0)
