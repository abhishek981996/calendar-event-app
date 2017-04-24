
from django import forms
# importing the form method from django
# django form will be used to create the form for Events
from webapp.models import EventsDetails


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['event'].required = True
        self.fields['date_begin'].required = True
        self.fields['date_end'].required = True
        self.fields['Location'].required = True
        self.fields['Description'].required = True

    class Meta:
        model = EventsDetails
        exclude = ['created_at', 'id', 'year']
