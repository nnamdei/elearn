from django.test import TestCase

from courses.models import Course,Module, Subject

class SubjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Subject.objects.create(title='Astrology', slug='astrology')

    def test_title_label(self):
        subject = Subject.objects.get(id=1)
        field_label = subject._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_slug_label(self):
        subject=Subject.objects.get(id=1)
        field_label = subject._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    def test_title_length(self):
        subject = Subject.objects.get(id=1)
        max_length = subject._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

''''class CourseModelTest(TestCase):
    def setUpTestData(cls):
        Course.objects.create()'''
    