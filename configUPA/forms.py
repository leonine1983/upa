from django import forms
from .models import Video_Backgroud_Painel

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video_Backgroud_Painel
        fields = ('title', 'video_file')