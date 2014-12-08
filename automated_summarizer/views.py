from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'automated_summarizer/index.html')

def input(request):
	return render(request, 'automated_summarizer/input.html')

def output(request):
	return render(request, 'automated_summarizer/output.html')

def proposals(request):
	return render(request, 'automated_summarizer/proposals.html')

def about(request):
	return render(request, 'automated_summarizer/about.html')

def contact(request):
	return render(request, 'automated_summarizer/contact.html')