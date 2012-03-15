from london.db import models

class QuestionQuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)

class Question(models.Model):
    class Meta:
        query = 'faq.models.QuestionQuerySet'

    title = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False, db_index=True)
    answer = models.TextField(blank=True)
    tags = models.ListField(blank=True, null=True)

    def __unicode__(self):
        return self['title']

