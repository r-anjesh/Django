from django.shortcuts import render, HttpResponse, redirect
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    return render(request, 'food/index.html', context={
        "item_list":item_list,
    })



class IndexClassView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'
    login_url = '/login/'  # Redirect non-logged-in users to this URL


@login_required
def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    
    return render(request, "food/detail.html", context={
        "item":item,
    })


class DetailClassView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'food/detail.html'
    login_url = '/login/'

    
@login_required
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form':form})



class CreateItem(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

@login_required
def update_item_list(request):
    items = Item.objects.all()  # Retrieve all items from the database
    return render(request, 'food/update-item-list.html', {'items': items})

@login_required
def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return render('food:index')
    
    return render(request, 'food/item-form.html',context={
        'form':form,
        'item':item,
    })



@login_required
def delete_item(request, id):
    item = Item.objects.get(pk=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {
        'item':item,
    })