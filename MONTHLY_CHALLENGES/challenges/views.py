from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "The future depends on what you do today. – Mahatma Gandhi",
    "february": "Success is the sum of small efforts, repeated day in and day out. – Robert Collier",
    "march": "The only way to do great work is to love what you do. – Steve Jobs",
    "april": "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "may": "Believe you can and you're halfway there. – Theodore Roosevelt",
    "june": "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "july": "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
    "august": "The harder you work for something, the greater you'll feel when you achieve it. – Unknown",
    "september": "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "october": "The way to get started is to quit talking and begin doing. – Walt Disney",
    "november": "Don't stop when you're tired. Stop when you're done. – Unknown",
    "december": None
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months" : months
    })


def monthly_challenge_num(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("NOT FOUND!")
    
    redirect_month = months[month-1]
    redirect_path = reverse("monthly-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", { 
            "text": challenge_text,
            "month" : month
        })
    except:
        raise Http404
    
    
