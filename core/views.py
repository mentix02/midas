from django.conf import settings
from django.views.generic import TemplateView, RedirectView


class IndexView(TemplateView):
    template_name = 'index.html'


class FaviconView(RedirectView):
    permanent = True
    url = settings.STATIC_URL + 'favicon.ico'
