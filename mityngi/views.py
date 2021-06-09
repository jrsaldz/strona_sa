from django.views.generic.list import ListView

from .models import Mityng


class MityngListView(ListView):
    model = Mityng
