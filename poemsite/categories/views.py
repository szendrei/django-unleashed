from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View

from .models import Category
from .forms import CategoryForm

def category_list(request):
    return render(request,'categories/category_list.html',
                  {'category_list': Category.objects.all()})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug__iexact=slug)
    return render(request,'categories/category_detail.html',
                  {'category': category})


class CategoryCreate(View):
    form_class = CategoryForm
    template_name = 'categories/category_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form':self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_category = bound_form.save()
            return redirect(new_category)
        else:
            return render(request, self.template_name, {'form':bound_form})


class CategoryUpdate(View):
    form_class = CategoryForm
    template_name='categories/category_form_update.html'
    
    def get(self, request, slug):
        category = get_object_or_404(Category, slug__iexact=slug)
        context = {'form':self.form_class(instance=category),
                   'category': category,}
        return render(request, self.template_name, context)

    def post(self, request, slug):
        category = get_object_or_404(Category, slug__iexact=slug)
        bound_form = self.form_class(request.POST, instance=category)
        if bound_form.is_valid():
            new_category = bound_form.save()
            return redirect(new_category)
        else:
            context = {'form': bound_form, 'category': category}
            return render(request, self.template_name, context)


class CategoryDelete(View):
    
    def get(self, request, slug):
        category = get_object_or_404(Category, slug__iexact=slug)
        return render(request, 'categories/category_confirm_delete.html',
                      {'category':category})

    def post(self, request, slug):
        category = get_object_or_404(Category, slug__iexact=slug)
        category.delete()
        return redirect('categories_category_list')
