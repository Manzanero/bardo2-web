from django.views.generic.base import TemplateView
from django.conf import settings
from django.shortcuts import render


def index(request):
    return render(request, 'web/index.html', {'base_url': settings.BASE_URL})


class IndexView(TemplateView):
    template_name = "index.html"


