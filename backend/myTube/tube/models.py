from django.db import models
from django.conf import settings


class Author(models.Model):
    authorName = models.OneToOneField(settings.AUTH_USER_MODEL, max_length=64, on_delete=models.CASCADE, related_name='author')
    authorBlocked = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.authorName}'


class Video(models.Model):
    videoSource = models.FileField(upload_to='videos', null=True)
    videoHeader = models.CharField(max_length=64, default='')
    videoTitle = models.CharField(max_length=64, default='')
    videoAuthor = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    videoLikes = models.IntegerField(default=0)
    videoDisLikes = models.IntegerField(default=0)
    videoViews = models.IntegerField(default=0)
    videoThumb = models.ImageField(upload_to='thumbnail', null=True)
    videoUsersLiked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='UsersLiked')
    videoUsersDisLiked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='UsersDisliked')

    videoDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.videoTitle}'

    def view(self):
        self.videoViews += 1
        self.save()

    def like(self):
        self.videoLikes += 1
        self.save()

    def dislike(self):
        self.videoDisLikes += 1
        self.save()


class Comment(models.Model):
    commentVideo = models.ForeignKey(Video, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    commentText = models.CharField(max_length=64)
    commentDateTime = models.DateTimeField(auto_now_add=True)
    commentRating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.commentUser} - {self.commentText}'

    def like(self):
        self.commentRating += 1
        self.save()


class Subscribe(models.Model):
    subscribeUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscribeChannel = models.ForeignKey(Author, on_delete=models.CASCADE)
