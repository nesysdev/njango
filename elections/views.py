from django.shortcuts import render
from django.http import HttpResponse
import pdfkit

# Create your views here.
def index(request):
	return HttpResponse("Hello world")
	#config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
	#pdf = pdfkit.from_url('https://www.neungyule.com','',configuration=config)

	#response = HttpResponse(pdf,content_type='application/pdf')
	#response['Content-Disposition'] = 'attachment; filename="test.pdf"'	

	#return response


