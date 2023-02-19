from rest_framework import serializers

from django.forms import ModelForm, CharField, TextInput, DateField
from django import forms
from .models import Author, Quote


class QuoteForm(ModelForm):
    quote = CharField(max_length=2500, required=True, widget=TextInput())
    tags = forms.CharField(required = True, label='Tags (comma-separated)')

    class Meta:
        model = Quote
        fields = ['quote', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all()

    def save(self, commit=True):
        instance = super().save(commit=commit)
        instance.save()
        return instance


class AuthorForm(ModelForm):
    fullname = CharField(max_length=100, required=True, widget=TextInput())
    born_date = DateField(required=True, input_formats=['%Y-%m-%d', '%m/%d/%Y'])
    born_location = CharField(max_length=100, required=True, widget=TextInput())
    description = CharField(max_length=5000, required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
        exclude = ['tags']
