from django import forms
from captcha.fields import CaptchaField
from django.utils.translation import ugettext_lazy as _
from .models import picture, comment


class AddForm(forms.ModelForm):
    class Meta:
        model = picture
        fields = ('pic_image', 'pic_title', 'pic_text',)
    captcha = CaptchaField()


class AddComment(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('comment_text',)
    captcha = CaptchaField()