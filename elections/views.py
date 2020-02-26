from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello world111")
	#config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
	#pdf = pdfkit.from_url('https://www.neungyule.com','',configuration=config)

	#response = HttpResponse(pdf,content_type='application/pdf')
	#response['Content-Disposition'] = 'attachment; filename="test.pdf"'	

	#return response

def	index2(request):
	return HttpResponse("Hello world22222")

def	index3(request):
	return HttpResponse("Hello world33333")	