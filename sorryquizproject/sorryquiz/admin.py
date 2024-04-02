from django.contrib import admin
from .models import *
from django.db.models import Sum


class ChoiceInline(admin.TabularInline):
    model=Choice
    extra = 1
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_filter = ("quiz",)

class UserResponseAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "selected_choice", "score", "quiz_title", "quiz_total_score")
    search_fields = ("user__username",)
    list_filter = ("user", "quiz")

    def quiz_title(self, obj):
        return obj.quiz.title
    
    def score(self, obj):
        return obj.selected_choice.score if obj.selected_choice else 0
    
    def quiz_total_score(self, obj):
        user_responses = UserResponse.objects.filter(user=obj.user, quiz=obj.quiz)
        total = user_responses.aggregate(total_score= Sum('selected_choice__score'))["total_score"]
        return total if total is not None else 0

admin.site.register(UserResponse, UserResponseAdmin)
admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

