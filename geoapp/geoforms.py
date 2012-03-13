from django import forms
from django.utils.translation import ugettext as _

class GeoForm(forms.Form):
    place = forms.CharField(label=u'Place to geocode', max_length=50)
    