from london.apps import admin
from london import forms
from london.apps.admin.modules import BaseModuleForm

from models import Question, Answer

class FormQuestion(BaseModuleForm):
    class Meta:
        model = Question
        exclude = ('author',)

#    def initialize(self):
#        self.fields['tags'].widget = forms.ListByCommaInput()


class FormAnswer(BaseModuleForm):
    class Meta:
        model = Answer
        exclude = ('author',)

class ModuleQuestion(admin.CrudModule):
    model = Question
    list_display = ('modified_date', 'text', 'status')
    form = FormQuestion
    exclude = ('author',)

class ModuleAnswer(admin.CrudModule):
    model = Answer
    list_display = ('modified_date', 'text', 'question', 'parent_answer')
    form = FormAnswer
    exclude = ('author',)

class AppFAQ(admin.AdminApplication):
    title = 'FAQ'
    modules = (ModuleQuestion, ModuleAnswer)
