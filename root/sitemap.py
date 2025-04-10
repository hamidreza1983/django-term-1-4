from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class RootStaticUrl(Sitemap):

    changefreq = "daily"
    priority = 0.5

    def items(self):
        return [
            "root:home",
            "root:about",
            "root:contact",
            "root:agent",
        ]

    def location(self, items):
        return reverse(items)
