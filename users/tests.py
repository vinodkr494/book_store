from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='vinod',email="vinod@gmail.com",password='pass1234')
        self.assertEqual(user.username,'vinod')
        self.assertEqual(user.email,'vinod@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username='superadmin',email='superadmin@gmail.com',password='superadmin1234')
        self.assertEqual(admin_user.username,'superadmin')
        self.assertEqual(admin_user.email,'superadmin@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

