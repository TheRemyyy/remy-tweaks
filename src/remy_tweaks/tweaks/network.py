from ..utils import run_command, registry_add, service_config

def disable_wifi_sense():
    registry_add(r"HKEY_LOCAL_MACHINE\Software\Microsoft\WcmSvc\wifinetworkmanager", "WiFiSenseCredShared", "REG_DWORD", 0)
    registry_add(r"HKEY_LOCAL_MACHINE\Software\Microsoft\WcmSvc\wifinetworkmanager", "WiFiSenseOpen", "REG_DWORD", 0)

def disable_wmp_network():
    service_config("WMPNetworkSvc", "disabled")

def disable_wallet_service():
    service_config("WalletService", "disabled")

def disable_bing_search():
    registry_add(r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Search", "BingSearchEnabled", "REG_DWORD", 0)

def disable_xbox_network():
    service_config("XblAuthManager", "disabled")
    service_config("XboxNetApiSvc", "disabled")
