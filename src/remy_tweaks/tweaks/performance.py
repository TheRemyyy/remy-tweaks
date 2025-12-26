from ..utils import run_command, registry_add, service_config, schtasks_disable

def set_memory_usage():
    run_command("fsutil behavior set memoryusage 2")

def disable_power_throttling():
    keys = [
        r"HKLM\SYSTEM\ControlSet001\Control\Power\PowerThrottling",
        r"HKLM\SYSTEM\ControlSet002\Control\Power\PowerThrottling",
        r"HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling"
    ]
    for key in keys:
        registry_add(key, "PowerThrottlingOff", "REG_DWORD", 1)

def enable_gpu_scheduling():
    registry_add(r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers", "HwSchMode", "REG_DWORD", 2)

def tweak_gpu():
    base = r"HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile"
    registry_add(base, "SystemResponsiveness", "REG_DWORD", 0)
    registry_add(base, "NoLazyMode", "REG_DWORD", 1)
    
    games = base + r"\Tasks\Games"
    registry_add(games, "Background Only", "REG_SZ", "False")
    registry_add(games, "GPU Priority", "REG_DWORD", 18)
    registry_add(games, "Priority", "REG_DWORD", 6)
    registry_add(games, "Scheduling Category", "REG_SZ", "High")
    registry_add(games, "SFIO Priority", "REG_SZ", "High")
    
    registry_add(r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\FontCache", "Start", "REG_DWORD", 4)
    registry_add(r"HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\FontCache3.0.0.0", "Start", "REG_DWORD", 4)

def tweak_cpu():
    keys = [
        r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Power",
        r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management",
        r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel",
        r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Executive",
        r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager",
        r"HKLM\SYSTEM\CurrentControlSet\Control\Power",
        r"HKLM\SYSTEM\CurrentControlSet\Control"
    ]
    for key in keys:
        registry_add(key, "CoalescingTimerInterval", "REG_DWORD", 0)
        
    registry_add(r"HKLM\SYSTEM\CurrentControlSet\Services\TimeBrokerSvc", "Start", "REG_DWORD", 3)
    registry_add(r"HKLM\SYSTEM\CurrentControlSet\Services\CryptSvc", "Start", "REG_DWORD", 2)
    registry_add(r"HKCU\Control Panel\Desktop", "HungApptimeout", "REG_SZ", "1000")

def auto_defrag_ssd():
    registry_add(r"HKLM\SYSTEM\CurrentControlSet\Services\defragsvc", "Start", "REG_DWORD", 4)
    schtasks_disable(r"\Microsoft\Windows\Defrag\ScheduledDefrag")

def disable_hibernation():
    for set_id in ["ControlSet001", "ControlSet002", "CurrentControlSet"]:
        registry_add(rf"HKLM\SYSTEM\{set_id}\Control\Power", "HibernateEnabled", "REG_DWORD", 0)

def set_high_performance():
    run_command("powercfg setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")

def tweak_hardware_queue():
    registry_add(r"HKLM\SYSTEM\CurrentControlSet\Services\mouclass\Parameters", "MouseDataQueueSize", "REG_DWORD", 20)
    registry_add(r"HKLM\SYSTEM\CurrentControlSet\Services\kbdclass\Parameters", "KeyboardDataQueueSize", "REG_DWORD", 20)

def bcd_tweaks():
    run_command("bcdedit /set disabledynamictick yes")
    run_command("bcdedit /set useplatformtick yes")
    run_command("bcdedit /deletevalue useplatformclock")

def memory_tweaks():
    key = r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management"
    registry_add(key, "LargeSystemCache", "REG_DWORD", 1)
    registry_add(key, "DisablePagingExecutive", "REG_DWORD", 1)
    registry_add(key, "DisablePagingCombining", "REG_DWORD", 1)
    
    prefetch = key + r"\PrefetchParameters"
    registry_add(prefetch, "EnablePrefetcher", "REG_DWORD", 0)
    registry_add(prefetch, "EnableSuperfetch", "REG_DWORD", 0)

def fast_startup():
    registry_add(r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Power", "HiberbootEnabled", "REG_DWORD", 1)
