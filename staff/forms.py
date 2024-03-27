# forms.py

from django import forms
from .models import *

class BelieverForm(forms.ModelForm):
    class Meta:
        model = Believer
        fields = ['full_name', 'image', 'age', 'occupation', 'address', 'joined_date', 'category', 'service_group', 'status', 'username', 'password']
        widgets = {
            'full_name': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter full name'}),
            'image': forms.FileInput(attrs={"class": "form-control", 'accept': 'image/*'}),
            'age': forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'Enter age'}),
            'occupation': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter occupation'}),
            'address': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter address'}),
            'joined_date': forms.DateInput(attrs={"class": "form-control", 'placeholder': 'YYYY-MM-DD'}),
            'category': forms.Select(attrs={"class": "form-control", 'placeholder': 'Select category'}),
            'service_group': forms.Select(attrs={"class": "form-control", 'placeholder': 'Select service_group'}),
            'status': forms.Select(attrs={"class": "form-control", 'placeholder': 'Select status'}),
            'username': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter username'}),
            'password': forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Enter password'}),
        }
     
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['program', 'lecturer', 'section', 'started_date', 'end_date', 'documents', 'messages', ]
        widgets = {
            'program': forms.TextInput(attrs={"class": "form-control",'placeholder': 'Enter program'}),
            'lecturer': forms.TextInput(attrs={"class": "form-control",'placeholder': 'Enter lecturer'}),
            'section': forms.TextInput(attrs={"class": "form-control",'placeholder': 'Enter class'}),
            'started_date': forms.DateInput(attrs={"class": "form-control",'placeholder': 'YYYY-MM-DD'}),
            'end_date': forms.DateInput(attrs={"class": "form-control",'placeholder': 'YYYY-MM-DD'}),
            'documents': forms.FileInput(attrs={"class": "form-control",'accept': 'documents/*'}),
            'messages': forms.Textarea(attrs={"class": "form-control",'placeholder': 'Enter messages'}),
            #'learners': forms.Select(attrs={"class": "form-control",'type':'dropdown','placeholder': 'Enter learners'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'image', 'start_date', 'end_date']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Enter description'}),
            'start_date': forms.DateInput(attrs={"class": "form-control", 'placeholder': 'YYYY-MM-DD'}),
            'end_date': forms.DateInput(attrs={"class": "form-control", 'placeholder': 'YYYY-MM-DD'}),
        }
 
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['reason', 'taker', 'amount', 'date']
        widgets = {
            'reason': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter reason'}),
            'taker': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter taker'}),
            'amount': forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'Enter amount'}),
            'date': forms.DateInput(attrs={"class": "form-control", 'placeholder': 'YYYY-MM-DD'}),
        }
         
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'date']
        widgets = {
            'question': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter question'}),
            'answer': forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Enter answer'}),
            'date': forms.DateInput(attrs={"class": "form-control", 'placeholder': 'YYYY-MM-DD'}),
        }
 
class FellowshipForm(forms.ModelForm):
    class Meta:
        model = Fellowship
        fields = ['pastor', 'message', 'image', 'documents']
        widgets = {
            'pastor': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter pastor'}),
            # 'believers': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter believers'}),
            'message': forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Enter message'}),
            'image': forms.FileInput(attrs={"class": "form-control", 'accept': 'image/*'}),
            'documents': forms.FileInput(attrs={"class": "form-control", 'accept': 'document/*'}),
        }

class GroupChatForm(forms.ModelForm):
    class Meta:
        model = GroupChat
        fields = ['message', 'image', 'documents', 'group', ]
        widgets = {
            # 'members': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter members'}),
            'message': forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Enter message'}),
            'image': forms.FileInput(attrs={"class": "form-control", 'accept': 'image/*'}),
            'documents': forms.FileInput(attrs={"class": "form-control", 'accept': 'document/*'}),
            'group': forms.Select(attrs={"class": "form-control", 'placeholder': 'Select group'}),
        }

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'reason', 'payer', 'date', 'balance']
        widgets = {
            'amount': forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'Enter amount'}),
            'reason': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter reason'}),
            'payer': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter payer'}),
            'date': forms.DateInput(attrs={"class": "form-control", 'placeholder': 'YYYY-MM-DD'}),
            'balance': forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'Enter balance'}),
        }

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'mark', 'buyer', 'expense', 'date', 'quantity', 'name']
        widgets = {
            'category': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter category'}),
            'mark': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter mark'}),
            'buyer': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter buyer'}),
            'expense': forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'Enter expense'}),
            'date': forms.DateInput(attrs={"class": "form-control", 'placeholder': 'YYYY-MM-DD'}),
            'quantity': forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'Enter quantity'}),
            'name': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter name'}),
        }

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'image', 'date']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Enter description'}),
            'date': forms.DateInput(attrs={"class": "form-control", 'placeholder': 'YYYY-MM-DD'}),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'age', 'place', 'image', 'contact_phone', 'date_served', 'title', 'description']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter name'}),
            'age': forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'Enter age'}),
            'place': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter place'}),
            'contact_phone': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter contact phone'}),
            'date_served': forms.DateInput(attrs={"class": "form-control", 'placeholder': 'YYYY-MM-DD'}),
            'title': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Enter description'}),
        }