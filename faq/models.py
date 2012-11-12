import datetime

from london.db import models


class QuestionQuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)


class Question(models.Model):
    class Meta:
        query = 'faq.models.QuestionQuerySet'

    QUESTION_STATUS_SOLVED = 'Solved'
    QUESTION_STATUS_PENDING = 'Pending'
    QUESTION_STATUS_CHOICES = (
        (QUESTION_STATUS_SOLVED, u'Solved'),
        (QUESTION_STATUS_PENDING, u'Pending'),
    )

    owner = models.CharField(max_length=100)
    text = models.CharField(max_length=250)
    status = models.CharField(max_length=10, choices=QUESTION_STATUS_CHOICES,
        default=QUESTION_STATUS_PENDING, db_index=True)
    modified_date = models.DateTimeField(blank=True, default=datetime.datetime.now, db_index=True)

    def __unicode__(self):
        return self['text']

    @property
    def root_comments(self):
        for comment in self['comments']:
            if comment['parent_comment'] is None:
                yield comment


class Comment(models.Model):
    question = models.ForeignKey(Question, related_name="comments", delete_cascade=True)
    owner = models.CharField(max_length=100)
    parent_comment = models.ForeignKey('self', null=True, blank=True,
        related_name='children_comments', delete_cascade=True)
    text = models.TextField()
    modified_date = models.DateTimeField(blank=True, default=datetime.datetime.now, db_index=True)

    def __unicode__(self):
        return self['text']