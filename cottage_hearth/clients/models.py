from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


class ClientPage(Page):
    blurb = RichTextField()

    content_panels = [
        FieldPanel('title'),
        FieldPanel('blurb'),
    ]

    def get_context(self, request, *args, **kwargs):
        return {
            **super().get_context(request, *args, **kwargs),
            'clients': Client.objects.all(),
        }

@register_snippet
class Client(models.Model):
    title = models.CharField(max_length=128)
    order = models.PositiveIntegerField(default=100)
    logo = models.ForeignKey('wagtailimages.Image', on_delete=models.PROTECT)
    showcase = models.BooleanField(help_text="Should this client be shown on the home page?")
    url = models.URLField(blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('order'),
        ImageChooserPanel('logo'),
        FieldPanel('showcase'),
        FieldPanel('url'),
    ]

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order', 'title')