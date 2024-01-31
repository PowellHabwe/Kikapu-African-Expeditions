from django import forms
from . import models
from .models import Tour_Booking, Tour
from .models import Tour_Booking, Tour, Excursion, ExcusionBooking
class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body',  'thumb',]


class CreateTour(forms.ModelForm):
    class Meta:
        model = models.Tour
        fields = '__all__'



from datetime import date

class DateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, attrs=None):
        super().__init__(attrs={'min': date.today().strftime('%Y-%m-%d'), **(attrs or {})})

class BookingForm(forms.ModelForm):
    class Meta:
        model = Tour_Booking
        fields = ['number_of_people', 'travel_date', 'first_name', 'last_name', 'email', 'selected_pax', ]

        widgets = {
            'travel_date': DateInput(),
        }

    def __init__(self, tour_id, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

        # Get the Tour instance
        self.tour = Tour.objects.get(id=tour_id)

        # Create choices for selected_pax field
        pax_choices = [
            ('pax1', f'Pax 1 - ${self.tour.pax1}' if self.tour.pax1 else ''),
            ('pax2', f'Pax 2 - ${self.tour.pax2}' if self.tour.pax2 else ''),
            ('pax3', f'Pax 3 - ${self.tour.pax3}' if self.tour.pax3 else ''),
        ]

        self.fields['selected_pax'] = forms.ChoiceField(
            label='Select Pax',
            choices=pax_choices,
            widget=forms.RadioSelect
        )


        self.fields['travel_date'].widget = DateInput()
        # self.category_name = self.tour.category.category_name if self.tour.category else None

    def clean(self):
        cleaned_data = super().clean()

        # Set the category_name based on the tour's category
        if hasattr(self, 'tour'):
            cleaned_data['category_name'] = self.tour.category.category_name

        return cleaned_data
    
    def clean_selected_pax(self):
        selected_pax = self.cleaned_data['selected_pax']

        # Convert the selected_pax back to the corresponding field on the Tour model
        if selected_pax == 'pax1':
            return self.tour.pax1
        elif selected_pax == 'pax2':
            return self.tour.pax2
        elif selected_pax == 'pax3':
            return self.tour.pax3

        # Handle the case where selected_pax is not valid
        raise forms.ValidationError('Invalid selected_pax value')



class ExcursionBookingForm(forms.ModelForm):
    class Meta:
        model = ExcusionBooking
        fields = ['number_of_people', 'travel_date', 'first_name', 'last_name', 'email',  ]

        widgets = {
            'travel_date': DateInput(),
        }

    def __init__(self, excursion_id, *args, **kwargs):
        super(ExcursionBookingForm, self).__init__(*args, **kwargs)

        # Get the Tour instance
        self.excursion = Excursion.objects.get(id=excursion_id)

        
        self.fields['travel_date'].widget = DateInput()
        # self.category_name = self.tour.category.category_name if self.tour.category else None

   