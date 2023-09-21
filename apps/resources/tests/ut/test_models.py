from django.test import TestCase
from apps.resources import models

# Test Case class #Test<model-name>Model

class TestTagModel(TestCase):
    def setUp(self):
        self.tag_name="Python"
        self.tag = models.Tag(name=self.tag_name)

    #unit test 1 #test_<logic-name>
    def test_create_tag_object_successful(self):
        #check if the object created is of the instance Tag
        self.assertIsInstance(self.tag, models.Tag)

    #unit test 2
    def test_dunder_str(self):
        self.assertEqual(str(self.tag), self.tag_name )
        # or self.tag.__str__()


class TestCategoryModel(TestCase):
    def setUp(self):
        self.cat_name="Databases"
        self.category = models.Category(cat=self.cat_name)

    def test_create_category_object_successful(self):
        self.assertIsInstance(self.category, models.Category)

    def test_dunder_str(self):
        self.assertEqual(str(self.category), self.cat_name)

    def test_plural(self):
        expected_verbose_name_plural = "Categories"
        actual_verbose_name_plural = self.category._meta.verbose_name_plural
        self.assertEqual(actual_verbose_name_plural, expected_verbose_name_plural)
    