from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': [ 'pub_date' ], 'classes': ['collapse']}),
    ]
    # Compacter layout for choices
    inlines = [ChoiceInline]
    # Table view of the Question selection
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Add a filter field
    list_filter = ['pub_date']
    # Add searching question strings
    search_fields = ['question_text']
    
admin.site.register(Question, QuestionAdmin)
