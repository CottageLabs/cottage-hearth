import textwrap

from django.db import models
from django import forms
from django.forms import Textarea
from django.utils.safestring import mark_safe


class CreatorsWidget(Textarea):
    class Media:
        js = ('journal/fields/creators.js',)

    def render(self, name, value, attrs=None, renderer=None):
        return mark_safe(textwrap.dedent(f"""
            <div class="creators-field">
                {super().render(name, value, attrs, renderer)}
            </div>
        """.strip('\n')))


class CreatorsFormField(forms.JSONField):
    widget = CreatorsWidget


class CreatorsField(models.JSONField):
    def formfield(self, **kwargs):
        kwargs.setdefault('form_class', CreatorsFormField)
        return super().formfield(**kwargs)
