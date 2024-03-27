from django.urls import path
from .views import *

urlpatterns = [
    #index page
    path('', Index.as_view(), name='index'),
    

    # Believer URLs
    path('believer/', BelieverList.as_view(), name='believer_list'),
    path('believer/add/', BelieverCreate.as_view(), name='believer_add'),
    path('believer/<int:pk>/', BelieverUpdate.as_view(), name='believer_update'),
    path('believer/<int:pk>/delete/', BelieverDelete.as_view(), name='believer_delete'),

    # Education URLs
    path('education/', EducationList.as_view(), name='education_list'),
    path('education/add/', EducationCreate.as_view(), name='education_add'),
    path('education/<int:pk>/', EducationUpdate.as_view(), name='education_update'),
    path('education/<int:pk>/delete/', EducationDelete.as_view(), name='education_delete'),

     # Event URLs
    path('Event/', EventList.as_view(), name='event_list'),
    path('Event/add/', EventCreate.as_view(), name='event_add'),
    path('Event/<int:pk>/', EventUpdate.as_view(), name='event_update'),
    path('Event/<int:pk>/delete/', EventDelete.as_view(), name='event_delete'),
  
    
    # Expense URLs
    path('expense/', ExpenseList.as_view(), name='expense_list'),
    path('expense/add/', ExpenseCreate.as_view(), name='expense_add'),
    path('expense/<int:pk>/update/', ExpenseUpdate.as_view(), name='expense_update'),
    path('expense/<int:pk>/delete/', ExpenseDelete.as_view(), name='expense_delete'),

    # FAQ URLs
    path('faq/', FAQList.as_view(), name='faq_list'),
    path('faq/add/', FAQCreate.as_view(), name='faq_add'),
    path('faq/<int:pk>/', FAQUpdate.as_view(), name='faq_update'),
    path('faq/<int:pk>/delete/', FAQDelete.as_view(), name='faq_delete'),

    # Fellowship URLs
    path('fellowship/', FellowshipList.as_view(), name='fellowship_list'),
    path('fellowship/add/', FellowshipCreate.as_view(), name='fellowship_add'),
    path('fellowship/<int:pk>/', FellowshipUpdate.as_view(), name='fellowship_update'),
    path('fellowship/<int:pk>/delete/', FellowshipDelete.as_view(), name='fellowship_delete'),

    # Group URLs
    path('group/', GroupList.as_view(), name='group_list'),
    path('group/add/', GroupCreate.as_view(), name='group_add'),
    path('group/<int:pk>/', GroupUpdate.as_view(), name='group_update'),
    path('group/<int:pk>/delete/', GroupDelete.as_view(), name='group_delete'),

# Income URLs
    path('income/', IncomeList.as_view(), name='income_list'),
    path('income/add/', IncomeCreate.as_view(), name='income_add'),
    path('income/<int:pk>/update/', IncomeUpdate.as_view(), name='income_update'),
    path('income/<int:pk>/delete/', IncomeDelete.as_view(), name='income_delete'),
   
    # Stock URLs
    path('inventory/', StockList.as_view(), name='inventory_list'),
    path('inventory/add/', StockCreate.as_view(), name='inventory_add'),
    path('inventory/<int:pk>/update/', StockUpdate.as_view(), name='inventory_update'),
    path('inventory/<int:pk>/delete/', StockDelete.as_view(), name='inventory_delete'),
  
     # News URLs
    path('News/', NewsList.as_view(), name='news_list'),
    path('News/add/', NewsCreate.as_view(), name='news_add'),
    path('News/<int:pk>/', NewsUpdate.as_view(), name='news_update'),
    path('News/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
 
  # Testimonial URLs
    path('testimonial/', TestimonialList.as_view(), name='testimonial_list'),
    path('testimonial/add/', TestimonialCreate.as_view(), name='testimonial_add'),
    path('testimonial/<int:pk>/', TestimonialUpdate.as_view(), name='testimonial_update'),
    path('testimonial/<int:pk>/delete/', TestimonialDelete.as_view(), name='testimonial_delete'),

]
