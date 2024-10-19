from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, InventoryItemForm
from .models import InventoryItem, Category, Location
#from StockDB.settings import LOW_QUANTITY

# Create your views here.
class Index(TemplateView):
    template_name = 'stock/index.html'

class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        items = InventoryItem.objects.order_by('id')
        #items = InventoryItem.objects.filter(user=self.request.user.id).order_by('id')

        #low_inventory = InventoryItem.objects.filter(
        #    user=self.request.user.id,
        #    quantity__lte=LOW_QUANTITY
        #)

        return render(request, 'stock/dashboard.html', {'items': items})

class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'stock/signup.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                        username=form.cleaned_data['username'],
                        password=form.cleaned_data['password1']
                    )

            login(request, user)

            return redirect('index')

        return render(request, 'stock/signup.html', {'form': form})
    
class AddItem(LoginRequiredMixin, CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'stock/item_form.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['locations'] = Location.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditItem(LoginRequiredMixin, UpdateView):
    model = InventoryItem
    template_name = 'stock/update_stock.html'
    form_class = InventoryItemForm
    success_url = reverse_lazy('dashboard')

class DeleteItem(LoginRequiredMixin, DeleteView):
    model = InventoryItem
    template_name = 'stock/delete_item.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'item'

