import time
from halo import Halo # pip install halo
import sys

def main_animation_loop():
    spinner_animation = Halo(text='Snail.py is working...', spinner='dots', color='green')
    spinner_animation.start()
    last_message_time = time.time()
    message_interval = 5 * 60 # 5 دقیقه

    try:
        while True:
            current_time = time.time()
            if current_time - last_message_time >= message_interval:
                print(f"\n[{time.strftime('%H:%M:%S')}] Server working...", flush=True)
                last_message_time = current_time
            
            time.sleep(0.2)
    except (KeyboardInterrupt, SystemExit):
        spinner_animation.succeed("Animation stopping.")
    except Exception:
        spinner_animation.fail("Animation error.")
    finally:
        spinner_animation.stop() # متد stop در halo ایمن است
        print("Animation script finished.")

if __name__ == "__main__":
    main_animation_loop()