# Create form

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=12)
    GENDER = {
        ('M', 'Man'),
        ('W', 'Woman'),
        ('Non-Biner', 'Non Biner'),
    }
    gender = forms.ChoiceField(choices=GENDER,
                               widget=forms.CheckboxSelectMultiple,
                               )
    email  = forms.EmailField(label='Email Address')
    address = forms.CharField(required=False,
                              widget=forms.Textarea,
                              max_length=100)
    date_birth = forms.DateField(
        widget= forms.SelectDateWidget()
    )
    pos_code = forms.IntegerField(required=False)
    city = forms.CharField(required=True)
    province = forms.CharField(required=False)
    agree_or_not = forms.BooleanField()






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