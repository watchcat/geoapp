# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.views.generic.simple import direct_to_template
from geoforms import GeoForm

def main(request):
	form = GeoForm(request.POST or None)
	
	context = { 'form': form, 'location': None }
	if request.method == 'POST' and form.is_valid():
		location = form.cleaned_data.get('place', None)
		context['location']=location
		return direct_to_template(request, 'main.html', context)

	return direct_to_template(request, 'main.html', context)

def ajaxmap(request, location):
	context = { 'location': location }
	return direct_to_template(request, 'map.html', context)
