from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
monthly_plannner = {
    "jan": "jan",
    "feb": "feb",
    "march": "march",
    "april": "april",
    "may": "may",
    "june": "june",
    "july": "july",
    "aug": "aug",
    "sept": "sept",
    "oct": "oct",
    "nov": "nov",
    "dec": "dec",
}


def index_number(request, month):
    months = list(monthly_plannner.keys())
    if month > len(months):
        return HttpResponseNotFound("not a month")
    redirect_month = months[month - 1]
    
    return HttpResponseRedirect("/challanges/" + redirect_month)


def index(request, month):
    try:
        text = monthly_plannner[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("not a month")
