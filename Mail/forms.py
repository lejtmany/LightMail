from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, MultiField, Div

__author__ = 'lejtman'

from django import forms
from .models import Email, Contact


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['receiver', 'subject', 'content']

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.fields['receiver'].label = "To"
        self.helper.layout = Layout(
            Div(
                Field('receiver', id='contacts_auto_complete'), id='ui-widget'
            ))


class ContactForm(forms.ModelForm):
    submit_button_txt = 'Submit'
    add_submit = True

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'dob']
        widgets = {
            'dob': forms.DateInput(attrs={'class': 'datepicker'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = self.get_layout_helper(self.submit_button_txt)

    def get_layout_helper(self, submit_button_txt):
        helper = FormHelper()
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-lg-2'
        helper.field_class = 'col-lg-8'
        if(self.add_submit):
            helper.add_input(Submit('submit', submit_button_txt))
        return helper



class AddContactForm(ContactForm):
    submit_button_txt = 'Add Contact'

class UpdateContactForm(ContactForm):
    add_submit = False


