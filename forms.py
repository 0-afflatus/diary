#! /usr/bin/env python3
# -*- coding: UTF8 -*-

"""Host/diary - forms.py

Event Organiser
"""

__version__ = 0.1
__maintainer__ = "tim@assemblyrooms.org.uk"

# Modules

from django import forms

from .models import Event

time_choices = [
    ('None', '---'),
    ('08:00:00', '8am'),
    ('08:30:00', '8.30am'),
    ('09:00:00', '9am'),
    ('09:30:00', '9.30am'),
    ('10:00:00', '10am'),
    ('10:00:00', '10.30am'),
    ('11:00:00', '11am'),
    ('11:00:00', '11.30am'),
    ('12:00:00', 'midday'),
    ('12:00:00', '12.30'),
    ('13:00:00', '1pm'),
    ('13:00:00', '1.30pm'),
    ('14:00:00', '2pm'),
    ('14:00:00', '2.30pm'),
    ('15:00:00', '3pm'),
    ('15:00:00', '3.30pm'),
    ('16:00:00', '4pm'),
    ('16:00:00', '4.30pm'),
    ('17:00:00', '5pm'),
    ('17:00:00', '5.30pm'),
    ('18:00:00', '6pm'),
    ('18:00:00', '6.30pm'),
    ('19:00:00', '7pm'),
    ('19:00:00', '7.30pm'),
    ('20:00:00', '8pm'),
    ('20:00:00', '8.30pm'),
    ('21:00:00', '9pm'),
    ('21:00:00', '9.30pm'),
    ('22:00:00', '10pm'),
    ('22:00:00', '10.30pm'),
    ('23:00:00', '11pm'),
    ('23:00:00', '11.30pm'),
    ('00:00:00', 'midnight')
]

class EventEditForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = (
                'title',
                'details',
                'featured_img',
                'space',
                'is_public',
                'start_date',
                'end_date',
                'getin_time',
                'setup_time',
                'open_time',
                'end_time',
                'is_weekly',
                'adv_price',
                'door_price',
                'conc_price',
                'ticket_link',
                'total_fee',
                'deposit',
                'balance_due',
                'deposit_date',
                'balance_date',
                'hirer_name',
                'hirer_address',
                'hirer_postcode',
                'hirer_email',
                'hirer_phone',
                'hirer_mobile',
                'event_slug',
                'date_created',
                'date_updated',
                'owner'
        )
        widgets = {
                'start_date': forms.SelectDateWidget(),
                'end_date': forms.SelectDateWidget(),
                'balance_date': forms.SelectDateWidget(),
                'deposit_date': forms.SelectDateWidget(),
                'open_time': forms.Select(choices=time_choices),
                'getin_time': forms.Select(choices=time_choices),
                'setup_time': forms.Select(choices=time_choices),
                'end_time': forms.Select(choices=time_choices),
        }
