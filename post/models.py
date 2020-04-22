from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    class Meta:
        db_table = 'post'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    title = models.CharField(_('title'), max_length=250)
    text = models.TextField(_('text'))

    def __str__(self):
        return '%s %s' % (self.pk, self.title)


class PostLike(models.Model):
    class Meta:
        db_table = 'post_like'

    post = models.ForeignKey(Post, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='post_likes')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.pk, self.post.title)
