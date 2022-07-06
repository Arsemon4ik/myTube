from django_filters import FilterSet
from .models import Video


class VideoFilter(FilterSet):
    class Meta:
        model = Video
        fields = {
            'videoHeader': ['icontains'],
        }
