from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    #pub_date = models.DateTimeField('date published') # Part of the tutorial but not necessarily needed

class Cards_Drawn(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    cards_drawn_text = models.CharField(max_length = 200)
    #votes = models.IntegerField(default = 0) # Will we need this? Likely not

    # If using Field.choices??? Idk
    #CARD_ONE = '1'
    #CARD_TWO = '2'
    #CARD_THREE = '3'
    #CARD_FOUR = '4'
