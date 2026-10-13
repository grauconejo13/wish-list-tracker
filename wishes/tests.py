from django.test import TestCase
from django.urls import reverse

from .models import WishItem, WishList


class WishListFlowTests(TestCase):
    def test_create_list(self):
        response = self.client.post(reverse("wishes:create_list"), {
            "title": "Christmas 2026",
            "recipient_name": "Sam",
            "occasion": "Christmas",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(WishList.objects.filter(title="Christmas 2026").exists())

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
