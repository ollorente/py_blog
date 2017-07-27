from django.shortcuts import render
from django.http import HttpResponseRedirect


def indexBackoffice(request):
	if request.user.is_authenticated():
		us = 'Home'
		uslink = '/'
		vs = 'Backoffice'
		context = {
			'us':us,
			'uslink':uslink,
			'vs':vs,
		}
		return render(request, 'backoffice/index.html', context)
	else:
		return HttpResponseRedirect('/')