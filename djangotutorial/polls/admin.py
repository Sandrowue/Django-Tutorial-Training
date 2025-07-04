from django.contrib import admin
from .models import Question, Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

    # Changing form fields order
    """ fields = ["pub_date", "question_text"] """

    # Using fieldsets
    fieldsets = [
        ("Define Question", {"fields": ["question_text"]}), 
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ] 
    inlines =[ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# Separate registration of Choice
""" admin.site.register(Choice) """
