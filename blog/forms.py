from django import forms
from django.template.defaultfilters import title

#import model from models.py
from .models import Post

# class PostForm(forms.Form):
#
#     title = forms.CharField(
#         label='Title',
#         max_length=50,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter the title'
#             }
#         )
#     )
#
#     body = forms.CharField(required=False,
#              max_length=1000,
#              widget=forms.Textarea(
#              attrs={
#                     'class': 'form-control',
#                     }
#             )
#     )
#
#     email = forms.EmailField(
#         label='Email Address',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter your valid email',
#             }
#         )
#     )
#
#     address = forms.CharField(required=False,
#             max_length=100,
#             widget=forms.Textarea(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             )
#     )
#
#     category = forms.CharField(
#             label='Category',
#             max_length=30,
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Category'
#                 }
#             )
#         )




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'email',
            'adress',
            'category'
        ]
        labels = {
            'title': 'Title',
            'body': 'Paragraph',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder': 'Enter the title...', }
            ),
            'body' : forms.Textarea(
                attrs={'class': 'form-control', }
            ),
            'email' : forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your valid email', }
            ),
            'adress': forms.Textarea(
                attrs={'class': 'form-control',}
            ),
            'category' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Category'}
            ),

        }
        # https: // stackoverflow.com / questions / 12097825 / specifying - widget -
        # for -model - form - extra - field - django

    def clean_title(self):

        title_input = self.cleaned_data.get('title')

        if title_input == 'pornhub':
            raise forms.ValidationError("the title is under age topic")
        return title_input