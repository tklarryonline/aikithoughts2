from os import linesep

from django.conf import settings
from django.db import models


class Excerptable(models.Model):
    MARKDOWN_PARAGRAPH_SPLIT = linesep

    class Meta:
        abstract = True

    @property
    def excerpt(self):
        '''
        Produce excerpt for the text of Excerptable object.

        If EXCERPTABLE_MAX_CHARS and EXCERPTABLE_END_MARK are set in settings,
        use them as the limit for excerpt and the end letters respectfully.

        Otherwise, just take the first paragraph of the text.
        '''
        try:
            max_chars = settings.EXCERPTABLE_MAX_CHARS
            end_mark = settings.EXCERPTABLE_END_MARK
        except AttributeError:
            return self.text.split(self.MARKDOWN_PARAGRAPH_SPLIT)[0]
        else:
            return self.text[:max_chars - len(end_mark)] + end_mark
