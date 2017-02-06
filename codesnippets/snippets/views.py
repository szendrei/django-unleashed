from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from django.utils.text import slugify

from .models import Snippet
from .forms import SnippetForm

def index_view(request):
    return render(request, 'snippets/homepage.html',
                  {'snippet_list':Snippet.objects.all()[:5]})

def snippet_list(request):
    return render(request, 'snippets/snippet_list.html',
                  {'snippet_list':Snippet.objects.all()})

def snippet_detail(request, slug):
    snippet = get_object_or_404(Snippet, slug__iexact=slug)
    return render(request, 'snippets/snippet_detail.html',
                  {'snippet': snippet})


class SnippetCreate(View):
    form_class = SnippetForm
    template_name = 'snippets/snippet_form.html'

    def get(self, request):
        return render(request, self.template_name,{'form':self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_snippet = bound_form.save()
            if new_snippet.title == '':
                new_snippet.slug = slugify(new_snippet.pk)
            else:
                new_snippet.slug = slugify(new_snippet.title)
            new_snippet.save()
            return redirect(new_snippet)
        else:
            return render(request, self.template_name,{'form':bound_form})


class SnippetUpdate(View):
    form_class = SnippetForm
    template_name = 'snippets/snippet_form_update.html'

    def get(self, request, slug):
        snippet = get_object_or_404(Snippet, slug__iexact=slug)
        context = {'form':self.form_class(instance=snippet),
                   'snippet':snippet}
        return render(request, self.template_name,context)

    def post(self, request, slug):
        snippet = get_object_or_404(Snippet, slug__iexact=slug)
        bound_form = self.form_class(request.POST, instance=snippet)
        if bound_form.is_valid():
            new_snippet = bound_form.save()
            return redirect(new_snippet)
        else:
            context = {'form':bound_form, 'snippet':snippet}
            return render(request, self.template_name, context)


class SnippetDelete(View):
    def get(self, request, slug):
        snippet = get_object_or_404(Snippet, slug__iexact=slug)
        return render(request, 'snippets/snippet_confirm_delete.html',
                      {'snippet':snippet})

    def post(self, request, slug):
        snippet = get_object_or_404(Snippet, slug__iexact=slug)
        snippet.delete()
        return redirect('snippets_snippet_list')
