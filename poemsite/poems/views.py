from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View

from .models import Poem
from .forms import PoemForm

def poem_list(request):
    return render(request, 'poems/poem_list.html', 
                  {'poem_list': Poem.objects.all()})

def poem_detail(request, slug):
    poem = get_object_or_404(Poem, slug__iexact=slug)
    return render(request, 'poems/poem_detail.html',
                  {'poem': poem})


class PoemCreate(View):
    form_class = PoemForm
    template_name = 'poems/poem_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form':self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_poem = bound_form.save()
            return redirect(new_poem)
        else:
            return render(request, self.template_name, {'form':bound_form})


class PoemUpdate(View):
    form_class = PoemForm
    template_name = 'poems/poem_form_update.html'

    def get(self, request, slug):
        poem = get_object_or_404(Poem, slug__iexact=slug)
        context = {'form': self.form_class(instance=poem),
                   'poem': poem}
        return render(request, self.template_name, context)

    def post(self, request, slug):
        poem = get_object_or_404(Poem, slug__iexact=slug)
        bound_form = self.form_class(request.POST, instance=poem)
        if bound_form.is_valid():
            new_poem = bound_form.save()
            return redirect(new_poem)
        else:
            context = {'form': bound_form, 'poem': poem}
            return render(request, self.template_name, context)


class PoemDelete(View):
    def get(self, request, slug):
        poem = get_object_or_404(Poem, slug__iexact=slug)
        return render(request, 'poems/poem_confirm_delete.html',
                      {'poem':poem})

    def post(self, request, slug):
        poem = get_object_or_404(Poem, slug__iexact=slug)
        poem.delete()
        return redirect('poems_poem_list')
