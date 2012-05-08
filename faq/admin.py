from london.apps import admin
from london import forms
from london.apps.admin.modules import BaseModuleForm

from models import Question

class FormQuestion(BaseModuleForm):
    class Meta:
        model = Question

    def initialize(self):
        self.fields['tags'].widget = forms.ListByCommaInput()

class ModuleQuestion(admin.CrudModule):
    model = Question
    list_display = ('title','answer','tags','is_published',)
    form = FormQuestion

class AppFAQ(admin.AdminApplication):
    title = 'FAQ'
    modules = (ModuleQuestion,)

