from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    # setUp() runs before every tests that we run
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@mail.com',
            password='123456'
        )
        # force_login() comes from Client(), this allows to login without
        # having to do it manually
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@mail.com',
            password='123456',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        #  Updates the url in the function at reverse (dinamic url)
        url = reverse('admin:core_user_changelist')
        #  Test Client for HTTP GET to url
        res = self.client.get(url)

        #  assertContains() check if res contains
        # the attributes of a given object
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        #  Creates the below url: /admin/core/user/{id}
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
