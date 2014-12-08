from django.shortcuts import render
from django.http import HttpResponse
import unirest
import json

def index(request):
    return render(request, 'automated_summarizer/index.html')

def input(request):
    return render(request, 'automated_summarizer/input.html')

def output(request):
    license_url = request.POST['license']
# These code snippets use an open-source library. http://unirest.io/python
    response_api = unirest.get("https://tldr.p.mashape.com/summary?url=" + license_url,
  headers={
    "X-Mashape-Key": "95AGNvbrEomshnn9Dg4nujilCBscp15H3URjsnoKyyCuTQrszR"
  }
)
    summary_result = response_api.body['data']['summary']
    return render(request, 'automated_summarizer/output.html', {'summary_result': summary_result})

def proposals(request):
    return render(request, 'automated_summarizer/proposals.html')

def about(request):
    return render(request, 'automated_summarizer/about.html')

def contact(request):
    return render(request, 'automated_summarizer/contact.html')