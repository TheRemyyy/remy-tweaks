import sys
import time
from .ui import show_loading, show_menu, print_done, print_invalid, set_title
from .tweaks import network, performance, privacy, services, gaming

def main():
    set_title()
    try:
        show_loading()
    except KeyboardInterrupt:
        sys.exit()

    while True:
        try:
            choice = show_menu()
            
            if choice == "1":
                performance.set_memory_usage()
                print_done()
            elif choice == "2":
                network.disable_wifi_sense()
                print_done()
            elif choice == "3":
                network.disable_wmp_network()
                print_done()
            elif choice == "4":
                network.disable_wallet_service()
                print_done()
            elif choice == "5":
                network.disable_bing_search()
                print_done()
            elif choice == "6":
                network.disable_xbox_network()
                print_done()
            elif choice == "7":
                performance.disable_power_throttling()
                print_done()
            elif choice == "8":
                performance.enable_gpu_scheduling()
                print_done()
            elif choice == "9":
                performance.tweak_gpu()
                print_done()
            elif choice == "10":
                services.disable_background_apps()
                print_done()
            elif choice == "11":
                performance.tweak_cpu()
                print_done()
            elif choice == "12":
                services.disable_aero_peek()
                print_done()
            elif choice == "13":
                services.disable_prelaunch()
                print_done()
            elif choice == "14":
                gaming.disable_gamedvr()
                print_done()
            elif choice == "15":
                privacy.make_windows_secure()
                print_done()
            elif choice == "16":
                performance.auto_defrag_ssd()
                print_done()
            elif choice == "17":
                performance.disable_hibernation()
                print_done()
            elif choice == "18":
                performance.set_high_performance()
                print_done()
            elif choice == "19":
                performance.tweak_hardware_queue()
                print_done()
            elif choice == "20":
                performance.bcd_tweaks()
                print_done()
            elif choice == "21":
                performance.memory_tweaks()
                print_done()
            elif choice == "22":
                privacy.disable_telemetry()
                print_done()
            elif choice == "23":
                services.disable_unnecessary_services()
                print_done()
            elif choice == "24":
                gaming.system_tweaks()
                print_done()
            elif choice == "25":
                performance.fast_startup()
                print_done()
            elif choice == "26":
                privacy.disable_tipc()
                print_done()
            elif choice == "0":
                sys.exit()
            else:
                print_invalid()
                
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(2)

if __name__ == "__main__":
    main()
