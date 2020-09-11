from django.shortcuts import render
import speech_recognition as sr
import pyttsx3
import wolframalpha
import wikipedia
import webbrowser


def index(request):
    return render(request, 'webbot/index.htm')


def bot_search(request):
    query = request.GET.get('query')

    try:
        client = wolframalpha.Client("P33UYY-GYVE6A37PQ")
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'webbot/index.htm', {'ans': ans, 'query': query})

    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request, 'webbot/index.htm', {'ans': ans, 'query': query})

        except Exception:
            ans = "FOUND NOTHING"
            return render(request, 'webbot/index.htm', {'ans': ans, 'query': query})
