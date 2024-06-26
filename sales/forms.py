from django import forms

class dropdownChart(forms.Form):
    PILIH : (
        ('yearly', 'yearly')
        ('weekly', 'weekly'),
        ('quarterly', 'quarterly')
    )
    choice_date = forms.ChoiceField(choices=PILIH)
     