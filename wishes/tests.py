from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import WishItem, WishList


class WishListFlowTests(TestCase):
    def test_create_list_requires_login(self):
        response = self.client.get(reverse("wishes:create_list"))
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('wishes:create_list')}",
        )

    def test_authenticated_user_can_create_list(self):
        User.objects.create_user(username="sam", password="safe-test-password")
        self.client.login(username="sam", password="safe-test-password")
        response = self.client.post(reverse("wishes:create_list"), {
            "title": "Christmas 2026",
            "recipient_name": "Sam",
            "occasion": "Christmas",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(WishList.objects.filter(title="Christmas 2026").exists())

    def test_signup_logs_user_in(self):
        response = self.client.post(reverse("wishes:signup"), {
            "username": "alex",
            "password1": "A-strong-test-password-2026",
            "password2": "A-strong-test-password-2026",
        })
        self.assertRedirects(response, reverse("wishes:home"))
        self.assertIn("_auth_user_id", self.client.session)

    def test_htmx_claim_hides_claimant_name(self):
        wish_list = WishList.objects.create(title="Birthday", recipient_name="Sam")
        item = WishItem.objects.create(wish_list=wish_list, name="Book")
        response = self.client.post(
            reverse("wishes:claim_item", args=[item.pk]),
            {"claimed_by": "Alex"},
            HTTP_HX_REQUEST="true",
        )
        self.assertContains(response, "Claimed by another shopper")
        self.assertNotContains(response, "Alex")
