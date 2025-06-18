from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import sys
import os
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from services import systems
from services import snail as snail


def get_crypto_data(request):
    crypto_data = systems.vgsy.getStatGeckoPrice()
    return JsonResponse(crypto_data, safe=False)

def get_main_news(request):
    news_data = systems.vgsy.get_snail_data()
    return JsonResponse(news_data, safe=False)


# --- Global state for demonstration (Simplified - no more complex process simulation) ---
# In a real app, use a database or proper state management.
# These variables will now ONLY store the state of the toggles, not guard run actions.
snail_is_on = False
geckocoin_api_enabled = False
bloomberg_scraper_enabled = False
bonbast_scraper_enabled = False
dnsd_scraper_enabled = False
esdn_scraper_enabled = False
nytimes_scraper_enabled = False
yahoo_scraper_enabled = False
analyze_enabled = False
gemini_ai_enabled = False
local_ai_enabled = False

@csrf_exempt # REMINDER: Use proper CSRF protection in production!
def admin_panel_view(request):
    """Renders the main admin panel HTML page."""
    return render(request, 'admin_panel.html')

@csrf_exempt # REMINDER: Use proper CSRF protection in production!
def control_view(request):
    """Handles POST requests from toggle buttons and run buttons."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            code = data.get('code')
            status = data.get('status') # 'on' or 'off' (for toggles)
            response_message = f"Command for code {code} processed."

            # --- Process Commands Based on Code ---
            global snail_is_on, geckocoin_api_enabled, bloomberg_scraper_enabled, \
                   bonbast_scraper_enabled, dnsd_scraper_enabled, esdn_scraper_enabled, \
                   nytimes_scraper_enabled, yahoo_scraper_enabled, analyze_enabled, \
                   gemini_ai_enabled, local_ai_enabled

            # Global Toggle (Snail)
            if code == '100':
                if status == 'on':
                    snail.snail.active = True
                    snail.snail.runserver()
                elif status == 'off':
                    if snail.snail.active and snail.snail.durationsBackup:
                        print(f'snail will be deactivated in {int(min(snail.snail.durations.values()) / 60)} minutres! after {snail.snail.next_process_name}!')
                    snail.snail.active = False
                # You can add logic here to start/stop the main Snail service
            # Instant Run Button
            elif code == '400':
                response_message = "Instant Run command received. Initiating quick task."
                # Trigger your quick task here, regardless of Snail's global state
                print("DEBUG: Executing Instant Run logic...")

            # --- API Toggles ---
            elif code == '201': # GeckoCoin Toggle
                if status == 'on':
                    snail.snail.activate('gecko')
                elif status == 'off':
                    snail.snail.deactivate('gecko')

            # --- Scraper Toggles ---
            elif code == '301': # Bloomberg Toggle
                if status == 'on':
                    snail.snail.activate('bloomberg')
                elif status == 'off':
                    snail.snail.deactivate('bloomberg')

            elif code == '302': # Bonbast Toggle
                if status == 'on':
                    snail.snail.activate('bonbast')
                elif status == 'off':
                    snail.snail.deactivate('bonbast')

            elif code == '303': # DNSD Toggle
                if status == 'on':
                    snail.snail.activate('dnsd')
                elif status == 'off':
                    snail.snail.deactivate('dnsd')

            elif code == '304': # ESDN Toggle
                if status == 'on':
                    snail.snail.activate('esdn')
                elif status == 'off':
                    snail.snail.deactivate('esdn')

            elif code == '305': # NYTimes Toggle
                if status == 'on':
                    snail.snail.activate('nytimes')
                elif status == 'off':
                    snail.snail.deactivate('nytimes')

            elif code == '306': # Yahoo Toggle
                if status == 'on':
                    snail.snail.activate('yahoo')
                elif status == 'off':
                    snail.snail.deactivate('yahoo')
            # --- Analyze Toggles ---
            elif code == '501': # Analyze Toggle
                if status == "on":
                    snail.snail.analyze_active = True
                elif status == "off":
                    snail.snail.analyze_active = False
            elif code == '502': # Gemini AI Toggle
                gemini_ai_enabled = (status == 'on')
                response_message = f"Gemini AI module is now: {'Enabled' if gemini_ai_enabled else 'Disabled'}."
            elif code == '503': # Local AI Toggle
                local_ai_enabled = (status == 'on')
                response_message = f"Local AI module is now: {'Enabled' if local_ai_enabled else 'Disabled'}."

            # --- Individual Run Buttons (No more checks for 'enabled' status here) ---
            elif code == '201-run': # GeckoCoin Run
                snail.snail.instantrun('gecko')

            elif code == '301-run': # Bloomberg Run
                snail.snail.instantrun('bloomberg')

            elif code == '302-run': # Bonbast Run
                snail.snail.instantrun('bonbast')

            elif code == '303-run': # DNSD Run
                snail.snail.instantrun('dnsd')

            elif code == '304-run': # ESDN Run
                snail.snail.instantrun('esdn')

            elif code == '305-run': # NYTimes Run
                snail.snail.instantrun('nytimes')

            elif code == '306-run': # Yahoo Run
                snail.snail.instantrun('yahoo')

            elif code == '501-run': # Analyze Run
                response_message = "Analyze run initiated."
                print(f"DEBUG: Executing Analyze run logic. Module Enabled: {analyze_enabled}")
            elif code == '502-run': # Gemini AI Run
                response_message = "Gemini AI run initiated."
                print(f"DEBUG: Executing Gemini AI run logic. Module Enabled: {gemini_ai_enabled}")
            elif code == '503-run': # Local AI Run
                response_message = "Local AI run initiated."
                print(f"DEBUG: Executing Local AI run logic. Module Enabled: {local_ai_enabled}")

            else:
                return JsonResponse({'status': 'error', 'message': f"Unknown command code: {code}"}, status=400)

            return JsonResponse({'status': 'success', 'message': response_message})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON in request body.'}, status=400)
        except Exception as e:
            print(f"Error processing command: {e}")
            return JsonResponse({'status': 'error', 'message': f'Server error: {str(e)}'}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed for control_view.'}, status=405)
