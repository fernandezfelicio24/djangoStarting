# Create form

from django import forms

class ContactForm(forms.Form):

    name = forms.CharField(
        label='Full Name',
        max_length=20,
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your name'
            }
        )
                )

    GENDER = {
        ('M', 'Man'),
        ('W', 'Woman'),
        ('Non-Biner', 'Non Biner'),
    }
    gender = forms.ChoiceField(
        label='Gender',

        widget=forms.RadioSelect(),
                choices=[
                    ('M', 'Man'),
                    ('W', 'Woman')
                ]
                )


    email  = forms.EmailField(
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

    date_birth = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={
                'class': 'form-control col-sm-2',
            },
            )
    )
    pos_code = forms.IntegerField(required=False)
    city = forms.CharField(required=True)
    province = forms.CharField(required=False)
    agree_or_not = forms.BooleanField(label="All the Data that you enter is correct")






    """

    #python data type
    integer_field = forms.IntegerField(required=True)
    decimal_field = forms.DecimalField(required=False)
    float_field = forms.FloatField(required=False)
    boolean_field = forms.BooleanField(required=False)
    char_field = forms.CharField(max_length=10)

    # String input
    email_field = forms.EmailField()
    regex_field = forms.RegexField(regex=r'{P?<test>}')
    slug_field = forms.SlugField()
    url_field = forms.URLField()
    ip_field = forms.GenericIPAddressField()


    # Select input

    CHOICE = {
        ('value0', 'Default'),
        ('value1', 'Felicio'),
        ('value2', 'Reinaldo'),
        ('value3', 'Tiago'),
        ('value3', 'Diego'),

    }


    choice_field = forms.ChoiceField(choices=CHOICE)

    multi_choice_field = forms.MultipleChoiceField(choices=CHOICE)

    multi_type_field = forms.TypedMultipleChoiceField(choices=CHOICE)
    null_boolean_field = forms.NullBooleanField()

    #data time

    data_field = forms.DateField()
    datetime_field = forms.DateTimeField()
    duration_field = forms.DurationField()
    time_field = forms.TimeField()
    splitdatetime_field = forms.SplitDateTimeField()

    # file input
    file_field = forms.FileField()
    image_field = forms.ImageField()

    """