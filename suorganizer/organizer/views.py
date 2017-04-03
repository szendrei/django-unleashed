from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import (CreateView, DeleteView, DetailView, 
                                 ListView)

from core.utils import UpdateView
from .forms import NewsLinkForm, StartupForm, TagForm
from .models import NewsLink, Startup, Tag
from .utils import PageLinksMixin


class NewsLinkCreate(CreateView):
    form_class = NewsLinkForm
    model = NewsLink


class NewsLinkDelete(DeleteView):
    model = NewsLink

    def get_success_url(self):
        return self.object.startup.get_absolute_url()


class NewsLinkUpdate(UpdateView):
    form_class = NewsLinkForm
    model = NewsLink


class StartupCreate(CreateView):
    form_class = StartupForm
    model = Startup


class StartupDelete(DeleteView):
    model = Startup
    success_url = reverse_lazy('organizer_startup_list')


class StartupDetail(DetailView):
    model = Startup


class StartupList(PageLinksMixin, ListView):
    model = Startup
    paginate_by = 5


class StartupUpdate(UpdateView):
    form_class = StartupForm
    model = Startup


class TagCreate(CreateView):
    form_class = TagForm
    model = Tag


class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('organizer_tag_list')


class TagDetail(DetailView):
    model = Tag


class TagList(PageLinksMixin, ListView):
    model = Tag
    paginate_by = 5


class TagUpdate(UpdateView):
    form_class = TagForm
    model = Tag




