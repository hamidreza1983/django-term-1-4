from django.contrib import admin
from .models import Agents, Ability, Score, Testimonials, ContactUs

admin.site.register(Agents)
admin.site.register(Ability)
admin.site.register(Score)
admin.site.register(ContactUs)
#admin.site.register(Testimonials)

#@admin.register(Testimonials)
class TestimonialsCustomPanel(admin.ModelAdmin):
    list_display = ["title", "stars", "status", "created_at"]
    list_filter = ["stars", "status"]
    search_fields = ("title",)

admin.site.register(Testimonials, TestimonialsCustomPanel)