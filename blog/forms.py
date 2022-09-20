from django import forms


class PostForm(forms.Form):

    title = forms.CharField(
        label='Title',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title'
            }
        )
    )

    body = forms.CharField(required=False,
             max_length=100,
             widget=forms.Textarea(
             attrs={
                    'class': 'form-control',
                    }
            )
    )

    email = forms.EmailField(
        label='Email Address',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your valid email',
            }
        )
    )

    address = forms.CharField(required=False,
            max_length=100,
            widget=forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            )
    )

    category = forms.CharField(
            label='Category',
            max_length=30,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Category'
                }
            )
        )