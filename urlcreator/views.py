from django.shortcuts import render, HttpResponse
from .models import PDFRetriever
import urllib
# Create your views here.


def shortened_url(request, token):
    model = PDFRetriever.objects.get(token=token)
    url = model.pdf_url
    model.delete()

    with urllib.request.urlopen(url) as pdf:
        response = HttpResponse(
            pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename=filpdt'
        

    pdf.close()
    return response
