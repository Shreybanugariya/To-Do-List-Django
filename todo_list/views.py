from django.shortcuts import render, redirect
from .models import List 
from django.urls import reverse
from .forms import ListForms, AddForm
from django.contrib import messages
from django.views.generic.edit import UpdateView

def home(request):
  if request.method == 'POST':
    form = AddForm(request.POST or None)
    all_items = List.objects.all

    if form.is_valid():
      form.save()
      messages.success(request, ('Item is added to the List!'))
    return render(request, 'index.html', {'all_items': all_items})

  else:
    all_items = List.objects.all
    return render(request, 'index.html', {'all_items': all_items})
  messages.success(request, ('Item is added to the List!'))

def delete(request, list_id):
  item = List.objects.get(pk=list_id)
  item.delete()
  messages.success(request, ('Item has been Deleted!'))
  return redirect('home')

def cross_off(request, list_id):
  item = List.objects.get(pk=list_id)
  item.completed = True
  item.save()
  messages.success(request, ('Item has been completed'))
  return redirect('home')

def uncross(request, list_id):
  item = List.objects.get(pk=list_id)
  item.completed = False
  item.save()
  messages.success(request, ('Item added to remaining remaining'))
  return redirect('home')


class ListUpdateView(UpdateView):
  model = List
  form_class = ListForms
  template_name = 'edit.html'

  def get_success_url(self):
    return reverse('home')