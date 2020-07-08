from django.db import models

class Poll(models.Model):
    name = models.CharField(max_length=127) 
    start_date = models.DateField(editable=False)
    finish_date = models.DateField()
    description = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.name

class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def get_type(self):
        try:
            self.questiontext
            return 'question-text'
        except QuestionText.DoesNotExist:
            pass

        try:
            self.questiosinglechoice
            return 'question-single-choice'
        except QuestionSingleChoice.DoesNotExist:
            pass

        try:
            self.questionmultichoice
            return 'question-multi-choice'
        except QuestionMultiChoice.DoesNotExist:
            pass

        return 'generic'

class QuestionText(Question):
    question_text = models.CharField(max_length=200)

class QuestionSingleChoice(Question):
    question_choice = models.CharField(max_length=200)

class QuestionMultiChoice(Question):
    question_choice = models.CharField(max_length=200)



