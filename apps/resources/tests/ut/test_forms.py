# from django.test import TestCase
# from apps.resources.form import PostResourceForm

# class TestPostResourceForm(TestCase):
#     def test_form_is_valid_method_return_true(self):
#         data = {
#             "title":"Python for beginners",
#             "link": 'https://pythonforbeginners.com',
#             'description': 'Best resource for beginners and free',
#             'category':1,
#             'tags':1,
#         }

#         form = PostResourceForm(data=data)

#         self.assertTrue(form.is_valid())


#     def test_form_missing_link_generate_errors(self):
#         data = {
#             "title":"Python for beginners",
#             #"link": 'https://pythonforbeginners.com',
#             'description': 'Best resource for beginners and free'
#         }

#         form = PostResourceForm(data=data)
#         form.is_valid()

#         self.assertEqual(form.errors['link'][0], 'This field is required.')

