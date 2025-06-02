# from django.views.decorators.csrf import csrf_exempt # برای این مورد خاص احتمالا نیاز نیست
from django.shortcuts import render
from django.http import JsonResponse
import sys
import os
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from services import systems


def get_crypto_data(request):
    crypto_data = systems.vgsy.getStatGeckoPrice()
    return JsonResponse(crypto_data, safe=False)