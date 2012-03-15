from london.apps import admin
from london import forms

from models import Question

class ListByCommaInput(forms.TextInput):
    def value_from_datadict(self, data, files, name):
        value = super(ListByCommaInput, self).value_from_datadict(data, files, name)
        return [i.strip() for i in value.split(',')]

    def _format_value(self, value):
        value = value or []
        return ', '.join(value)

class FormQuestion(forms.ModelForm):
    class Meta:
        model = Question

    def initialize(self):
        self.fields['tags'].widget = ListByCommaInput()

class ModuleQuestion(admin.CrudModule):
    model = Question
    list_display = ('title','answer','tags','is_published',)
    form = FormQuestion

class AppFAQ(admin.AdminApplication):
    title = 'FAQ'
    modules = (ModuleQuestion,)

