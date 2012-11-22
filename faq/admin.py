from london.apps import admin
from london import forms
from london.apps.admin.modules import BaseModuleForm

from models import Question, Answer

class FormQuestion(BaseModuleForm):
    class Meta:
        model = Question

#    def initialize(self):
#        self.fields['tags'].widget = forms.ListByCommaInput()


class FormAnswer(BaseModuleForm):
    class Meta:
        model = Answer

class ModuleQuestion(admin.CrudModule):
    model = Question
    list_display = ('modified_date', 'author', 'text', 'status')
    form = FormQuestion

class ModuleAnswer(admin.CrudModule):
    model = Answer
    list_display = ('modified_date', 'author', 'text', 'question', 'parent_answer')
    form = FormAnswer

class AppFAQ(admin.AdminApplication):
    title = 'FAQ'
    modules = (ModuleQuestion, ModuleAnswer)
