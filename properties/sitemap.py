from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Properties


class PropertiesStaticUrl(Sitemap):

    changefreq = "daily"
    priority = 0.5

    def items(self):
        return [
            "properties:properties",
        ]

    def location(self, items):
        return reverse(items)


class PropertiesDynamicUrl(Sitemap):

    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Properties.objects.all()

    def location(self, items):
        return "/properties/detail/%i" % items.id
