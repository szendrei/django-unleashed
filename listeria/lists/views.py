from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect

from .models import List
from .forms import ListForm

def index_view(request):
    return render(request, 'lists/index.html', 
                  {'lists': List.objects.all()[:5]})

def list_list(request):
    return render(request, 'lists/list_list.html', 
                  {'lists': List.objects.all()})

def list_detail(request, slug):
    list_item = List.objects.get(slug__iexact=slug)
    return render(request, 'lists/list_detail.html', {'list_item': list_item})
                  

class ListCreate(View):
    form_class = ListForm
    template_name = 'lists/list_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form':self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_list = bound_form.save()
            return redirect(new_list)
        else:
            return render(request, self.template_name,{'form':bound_form})
