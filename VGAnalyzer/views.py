import json
import os
import sys

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from services import snail as snail
from services import analyze as analyze
from services import systems
from services import navigation as navigation


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


def mainPage(request):
    return render(request, 'mainPage.html')


@csrf_exempt
def getCryptoData(request):
    crypto_data = systems.vgsy.getStatGeckoPrice()
    return JsonResponse(crypto_data, safe=False)


@csrf_exempt
def getNewsData(request, title="SnOutsite"):
    news_data = systems.vgsy.Navread(title)
    return JsonResponse(news_data, safe=False)

#           -------------------------***API Navigation***------------------------

#    ------ EX LINK: http://127.0.0.1:8000/api/finance/?key=admin


def api_nav(request, id):
    print(f"this is the request:{request} and id:{id}")
    key = request.GET.get('key', 'admin')

    if key == 'admin':
        if id in ['crypto', 'economy', 'finance', 'investing', 'markets', 'science', 'tecnology', 'news']:
            if id == 'crypto':
                return getCryptoData(request)
            elif id == 'economy':
                return getNewsData(request, 'SnEconomy')
            elif id == 'finance':
                return getNewsData(request, 'SnFinance')
            elif id == 'investing':
                return getNewsData(request, 'SnInvesting')
            elif id == 'markets':
                return getNewsData(request, 'SnMarkets')
            elif id == 'science':
                return getNewsData(request, 'SnScience')
            elif id == 'tecnology':
                return getNewsData(request, 'SnTecnology')
            elif id == 'news':
                return getNewsData(request, 'SnOutput')
    else:
        return JsonResponse('bad request', safe=False)
#           -------------------------***Admin Panel***------------------------


def showOpiniononTmp(request, id):
    lastOp = navigation.nav.lastOP('PriceOp')
    if id == '.html':
        return render(request, f'{lastOp}.html')
    else:
        pass
        # sending the .md file to the user


def getOpinion(request):
    return render()


@csrf_exempt
def admin_panel_view(request):
    return render(request, 'admin_panel.html')


@csrf_exempt
def control_view(request):
    """Handles POST requests from toggle buttons and run buttons."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            code = data.get('code')
            status = data.get('status')
            params = data.get('params')
            response_message = f"Command for code {code} processed."

            # Global Toggle (Snail)
            if code == '100':
                if status == 'on':
                    snail.snail.active = True
                    snail.snail.runserver()
                elif status == 'off':
                    if snail.snail.active and snail.snail.durationsBackup:
                        print("deactivating the snail server...")
                    snail.snail.active = False
            # Instant Run Button
            elif code == '400':
                snail.snail.instantrun('all')

            # --- API Toggles ---
            elif code == '201':  # GeckoCoin Toggle
                if status == 'on':
                    snail.snail.activate('gecko', params)
                elif status == 'off':
                    snail.snail.deactivate('gecko')

            # --- Scraper Toggles ---
            elif code == '301':  # Bloomberg Toggle
                if status == 'on':
                    snail.snail.activate('bloomberg', params)
                elif status == 'off':
                    snail.snail.deactivate('bloomberg')

            elif code == '302':  # Bonbast Toggle
                if status == 'on':
                    snail.snail.activate('bonbast', params)
                elif status == 'off':
                    snail.snail.deactivate('bonbast')

            elif code == '303':  # DNSD Toggle
                if status == 'on':
                    snail.snail.activate('dnsd', params)
                elif status == 'off':
                    snail.snail.deactivate('dnsd')

            elif code == '304':  # ESDN Toggle
                if status == 'on':
                    snail.snail.activate('esdn', params)
                elif status == 'off':
                    snail.snail.deactivate('esdn')

            elif code == '305':  # NYTimes Toggle
                if status == 'on':
                    snail.snail.activate('nytimes', params)
                elif status == 'off':
                    snail.snail.deactivate('nytimes')

            elif code == '306':  # Yahoo Toggle
                if status == 'on':
                    snail.snail.activate('yahoo', params)
                elif status == 'off':
                    snail.snail.deactivate('yahoo')
            # --- Analyze Toggles ---
            elif code == '501':  # Analyze Toggle
                if status == "on":
                    snail.snail.activate('analyze', params)
                elif status == "off":
                    snail.snail.deactivate('analyze')
            elif code == '502':  # Gemini AI Toggle
                if status == 'on':
                    snail.snail.activate('gemini', params)
                    analyze.az.gemeni_active = True
                    print("gemeni activated")
                elif status == 'off':
                    snail.snail.deactivate('gemini')
                    analyze.az.gemeni_active = False
                    print("gemeni deactivated")

            elif code == '503':  # Local AI Toggle
                if status == 'on':
                    snail.snail.activate('localAi', params)
                    analyze.az.localai_active = True
                    print("local-ai activated")
                elif status == 'off':
                    snail.snail.deactivate('localAi')
                    analyze.az.localai_active = False
                    print("local-ai deactivated")
            elif code == '504':  # Price Analyze Toggle
                if status == 'on':
                    snail.snail.activate('priceAnalyze', params)
                    analyze.az.priceAnalyzeActive = True
                    print("price Analyze Activated")
                elif status == 'off':
                    snail.snail.deactivate('priceAnalyze')
                    analyze.az.priceAnalyzeActive = False
                    print("price Analyze deactivated")

            # --- Individual Run Buttons (Now they just trigger the run) ---
            elif code == '201-run':
                snail.snail.instantrun('gecko')
            elif code == '301-run':
                snail.snail.instantrun('bloomberg')
            elif code == '302-run':
                snail.snail.instantrun('bonbast')
            elif code == '303-run':
                snail.snail.instantrun('dnsd')
            elif code == '304-run':
                snail.snail.instantrun('esdn')
            elif code == '305-run':
                snail.snail.instantrun('nytimes')
            elif code == '306-run':
                snail.snail.instantrun('yahoo')
            elif code == '501-run':
                snail.snail.instantrun('analyze')
            elif code == '502-run':
                analyze.az.manage("external")
            elif code == '503-run':
                analyze.az.manage("local")
            elif code == '504-run':
                analyze.az.priceAnalyze(True)

            else:
                return JsonResponse({'status': 'error', 'message': f"Unknown command code: {code}"}, status=400)

            return JsonResponse({'status': 'success', 'message': response_message})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON in request body.'}, status=400)    
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed for control_view.'}, status=405)
