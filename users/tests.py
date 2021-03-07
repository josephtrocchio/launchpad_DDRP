from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class CustomUserTests(TestCase):

    def test_super_user(self):
        User = get_user_model()
        admin_user = User.objects.create_user(
            username='root',
            email='trocchioje@gmail.com',
            password='Earl!221'
        )
        self.assertEqual(admin_user.username, 'root')
        self.assertEqual(admin_user.email, 'trocchioje@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertFalse(admin_user.is_superuser)    

    