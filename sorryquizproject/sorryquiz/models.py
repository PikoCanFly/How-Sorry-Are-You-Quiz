from django.db import models
from django.contrib.auth.models import User
class Quiz(models.Model):
    title = models.CharField(max_length=225)
    is_ready_to_publish = models.BooleanField(default = False)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = "quizzes"

class Question(models.Model):
    text = models.CharField(max_length=225)
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.text


class Choice(models.Model):
    text = models.CharField(max_length=225)
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    
    def __str__(self) -> str:
        return self.text

class UserResponse(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
  
def __str__(self) -> str:
    return f"{self.user.username}'s response to {self.question.text} in {self.quiz.title} is {self.choice.text}"

def calculate_score(self):
    total_score = sum(choice.score for choice in self.question.choice.all())
    return total_score