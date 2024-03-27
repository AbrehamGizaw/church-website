from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.views import View 
from django.contrib import messages
from django.urls import reverse_lazy
from .models import *
from .forms import *

class Index(TemplateView):
    template_name = 'staff/index.html'

# Believer Views
class BelieverList(ListView):
    model = Believer
    template_name = 'staff/Believers/list_believer.html'
    context_object_name = 'believers'

class BelieverCreate(CreateView):
    model = Believer
    form_class = BelieverForm
    template_name = 'staff/Believers/add_believer.html'
    success_url = reverse_lazy('staff:believer_list')

class BelieverUpdate(UpdateView):
    model = Believer
    form_class = BelieverForm
    template_name = 'staff/Believers/add_believer.html'
    success_url = reverse_lazy('staff:believer_list')

class BelieverDelete(DeleteView):
    model = Believer
    template_name = 'believer_confirm_delete.html'
    success_url = reverse_lazy('staff:believer_list')


# Education Views
class EducationList(ListView):
    model = Education
    template_name = 'staff/Educations/list_education.html'
    context_object_name = 'educations'

class EducationCreate(CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'staff/Educations/add_education.html'
    success_url = reverse_lazy('staff:education_list')

class EducationUpdate(UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'staff/Educations/add_education.html'
    success_url = reverse_lazy('staff:education_list')

class EducationDelete(DeleteView):
    model = Education
    template_name = 'education_confirm_delete.html'
    success_url = reverse_lazy('staff:education_list')

# Event Views
class EventList(ListView):
    model = Event
    template_name = 'staff/Events/list_event.html'
    context_object_name = 'events'

class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'staff/Events/add_event.html'
    success_url = reverse_lazy('staff:event_list')

class EventUpdate(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'staff/Events/add_event.html'
    success_url = reverse_lazy('staff:event_list')

class EventDelete(DeleteView):
    model = Event
    template_name = 'staff/event_confirm_delete.html'
    success_url = reverse_lazy('staff:event_list')

#Expenses views
class ExpenseList(ListView):
    model = Expense
    template_name = 'staff/Expenses/list_expense.html'  
    context_object_name = 'expenses'

class ExpenseCreate(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'staff/Expenses/add_expense.html'  
    success_url = reverse_lazy('staff:expense_list')

class ExpenseUpdate(UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'staff/Expenses/add_expense.html'  
    success_url = reverse_lazy('staff:expense_list')

class ExpenseDelete(DeleteView):
    model = Expense
    template_name = 'expense_confirm_delete.html'  
    success_url = reverse_lazy('staff:expense_list')

# FAQ Views
class FAQList(ListView):
    model = FAQ
    template_name = 'staff/FAQs/list_faq.html'
    context_object_name = 'faqs'

class FAQCreate(CreateView):
    model = FAQ
    form_class = FAQForm
    template_name = 'staff/FAQs/add_faq.html'
    success_url = reverse_lazy('staff:faq_list')

class FAQUpdate(UpdateView):
    model = FAQ
    form_class = FAQForm
    template_name = 'staff/FAQs/add_faq.html'
    success_url = reverse_lazy('staff:faq_list')

class FAQDelete(DeleteView):
    model = FAQ
    template_name = 'faq_confirm_delete.html'
    success_url = reverse_lazy('staff:faq_list')

# Fellowship Views
class FellowshipList(ListView):
    model = Fellowship
    template_name = 'staff/Fellowships/list_fellowship.html'
    context_object_name = 'fellowships'

class FellowshipCreate(CreateView):
    model = Fellowship
    form_class = FellowshipForm
    template_name = 'staff/Fellowships/add_fellowship.html'
    success_url = reverse_lazy('staff:fellowship_list')

class FellowshipUpdate(UpdateView):
    model = Fellowship
    form_class = FellowshipForm
    template_name = 'staff/Fellowships/add_fellowship.html'
    success_url = reverse_lazy('staff:fellowship_list')

class FellowshipDelete(DeleteView):
    model = Fellowship
    template_name = 'fellowship_confirm_delete.html'
    success_url = reverse_lazy('staff:fellowship_list')


# GroupChat Views
class GroupList(View):
    template_name='staff/Groups/list_group.html'
    def get(self, request):
        groups = GroupChat.objects.all()
        return render(request, self.template_name, {'groups':groups})

class GroupCreate(View):
    template_name = 'staff/Groups/add_group.html'
    def get(self, request):
        form = GroupChatForm()  
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form=GroupChatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ' you have added successfully')
            return redirect('staff:group_list')
        else:
            messages.warning(request, 'please check your input again')
            return render(request, self.template_name, {'form':form})

class GroupUpdate(View):
    template_name = 'staff/Groups/add_group.html'
    def get(self, request, pk):
        # Retrieve the group instance using pk
        group = GroupChat.objects.get(pk=pk)
        # Create a form instance with the retrieved group
        form = GroupChatForm(instance=group)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        # Retrieve the group instance using pk
        group = GroupChat.objects.get(pk=pk)
        # Populate the form with POST data and files
        form = GroupChatForm(instance=group, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Group updated successfully')
            return redirect('staff:group_list')
        else:
            messages.warning(request, 'Please check your input again')
            return render(request, self.template_name, {'form': form})




class GroupDelete(DeleteView):
    model = GroupChat
    template_name = 'group_confirm_delete.html'
    success_url = reverse_lazy('staff:group_list')


#Incomes views
class IncomeList(ListView):
    model = Income
    template_name = 'staff/Incomes/list_income.html'  
    context_object_name = 'incomes'

class IncomeCreate(CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'staff/Incomes/add_income.html'  
    success_url = reverse_lazy('staff:income_list')

class IncomeUpdate(UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = 'staff/Incomes/add_income.html'  
    success_url = reverse_lazy('staff:income_list')

class IncomeDelete(DeleteView):
    model = Income
    template_name = 'income_confirm_delete.html'  
    success_url = reverse_lazy('staff:income_list')

#Stock views
class StockList(ListView):
    model = Stock
    template_name = 'staff/Inventories/list_inventory.html'  
    context_object_name = 'inventory'

class StockCreate(CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'staff/Inventories/add_inventory.html'  
    success_url = reverse_lazy('staff:inventory_list')

class StockUpdate(UpdateView):
    model = Stock
    form_class = StockForm
    template_name = 'staff/Inventories/add_inventory.html' 
    success_url = reverse_lazy('staff:inventory_list')

class StockDelete(DeleteView):
    model = Stock
    template_name = 'staff/inventory_confirm_delete.html'  
    success_url = reverse_lazy('staff:inventory_list')

# News Views
class NewsList(ListView):
    model = News
    template_name = 'staff/News/list_news.html'
    context_object_name = 'news'

class NewsCreate(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'staff/News/add_news.html'
    success_url = reverse_lazy('staff:news_list')

class NewsUpdate(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'staff/News/add_news.html'
    success_url = reverse_lazy('staff:news_list')

class NewsDelete(DeleteView):
    model = News
    template_name = 'news_confirm_delete.html'
    success_url = reverse_lazy('staff:news_list')


# Testimonial Views
class TestimonialList(ListView):
    model = Testimonial
    template_name = 'staff/Testimonials/list_testimonial.html'
    context_object_name = 'testimonials'

class TestimonialCreate(CreateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'staff/Testimonials/add_testimonial.html'
    success_url = reverse_lazy('staff:testimonial_list')

class TestimonialUpdate(UpdateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'staff/Testimonials/add_testimonial.html'
    success_url = reverse_lazy('staff:testimonial_list')

class TestimonialDelete(DeleteView):
    model = Testimonial
    template_name = 'staff/testimonials_confirm_delete.html'
    success_url = reverse_lazy('staff:testimonial_list')
