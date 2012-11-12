from london.apps import admin
from london import forms
from london.apps.admin.modules import BaseModuleForm

from models import Question, Comment

class FormQuestion(BaseModuleForm):
    class Meta:
        model = Question

#    def initialize(self):
#        self.fields['tags'].widget = forms.ListByCommaInput()


class FormComment(BaseModuleForm):
    class Meta:
        model = Comment

class ModuleQuestion(admin.CrudModule):
    model = Question
    list_display = ('modified_date', 'owner', 'text', 'is_published', 'status')
    form = FormQuestion

class ModuleComment(admin.CrudModule):
    model = Comment
    list_display = ('modified_date', 'owner', 'text', 'parent_comment', 'question')
    form = FormComment

class AppFAQ(admin.AdminApplication):
    title = 'FAQ'
    modules = (ModuleQuestion, ModuleComment)
