from django.test.utils import override_settings

from behavioralist.tests import faker
from behavioralist.tests.test_case_mixins import BehaviorTestCaseMixin


class ExcerptableTests(BehaviorTestCaseMixin):
    def test_excerpt_no_limit_settings(self):
        paragraphs = faker.paragraphs()

        obj = self.create_instance(
            text='\n\n'.join(paragraphs)
        )

        excerpt = obj.excerpt
        self.assertEqual(excerpt, paragraphs[0])

    def test_excerpt_text_exceed_maximum_characters(self):
        paragraphs = faker.paragraphs()

        obj = self.create_instance(
            text='\n\n'.join(paragraphs)
        )

        max_chars = int(len(paragraphs[0]) / 2)
        end_mark = '...'
        with override_settings(EXCERPTABLE_MAX_CHARS=max_chars), override_settings(EXCERPTABLE_END_MARK=end_mark):
            excerpt = obj.excerpt

        self.assertEqual(excerpt, paragraphs[0][:max_chars - len(end_mark)] + end_mark)
