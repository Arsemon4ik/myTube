from django.contrib import admin

from .models import Comment, Subscribe, Video, Author

# Register your models here.
admin.site.register(Comment)
admin.site.register(Subscribe)
admin.site.register(Video)
admin.site.register(Author)
