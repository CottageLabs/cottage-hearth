from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page



class HomePage(Page):
    tagline = models.TextField(blank=True)

    content_panels = [
        FieldPanel('title'),
        FieldPanel('tagline'),
    ]