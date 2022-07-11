from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget

from .models import Video


class PostForm(ModelForm):
    '''Форма создание статей для пользователей (которые вошли в систему)'''

    class Meta:
        model = Video
        fields = ['videoHeader', 'videoTitle', 'videoAuthor', 'videoSource', 'videoThumb']
        widgets = {
            'videoThumb': SummernoteWidget(),
        }
