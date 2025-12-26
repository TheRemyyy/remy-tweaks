from ..utils import run_command, registry_add

def disable_gamedvr():
    registry_add(r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR", "AppCaptureEnabled", "REG_DWORD", 0)
    registry_add(r"HKCU\System\GameConfigStore", "GameDVR_Enabled", "REG_DWORD", 0)
    registry_add(r"HKLM\SOFTWARE\Wow6432Node\Policies\Microsoft\Windows\GameDVR", "AllowgameDVR", "REG_DWORD", 0)

def system_tweaks():
    # Mix of gaming and system tweaks from option 24
    registry_add(r"HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\Maintenance", "MaintenanceDisabled", "REG_DWORD", 1)
    registry_add(r"HKLM\SYSTEM\ControlSet001\Control\GraphicsDrivers\Scheduler", "EnablePreemption", "REG_DWORD", 0)
    
    # Game Config Store
    run_command(r'Reg delete "HKCU\System\GameConfigStore" /v "Win32_AutoGameModeDefaultProfile" /f')
    run_command(r'Reg delete "HKCU\System\GameConfigStore" /v "Win32_GameModeRelatedProcesses" /f')
    
    base_gcs = r"HKCU\System\GameConfigStore"
    registry_add(base_gcs, "GameDVR_DSEBehavior", "REG_DWORD", 2)
    registry_add(base_gcs, "GameDVR_DXGIHonorFSEWindowsCompatible", "REG_DWORD", 1)
    registry_add(base_gcs, "GameDVR_EFSEFeatureFlags", "REG_DWORD", 0)
    registry_add(base_gcs, "GameDVR_Enabled", "REG_DWORD", 0)
    registry_add(base_gcs, "GameDVR_FSEBehavior", "REG_DWORD", 2)
    registry_add(base_gcs, "GameDVR_FSEBehaviorMode", "REG_DWORD", 2)
    registry_add(base_gcs, "GameDVR_HonorUserFSEBehaviorMode", "REG_DWORD", 1)
    
    registry_add(r"HKLM\SOFTWARE\Policies\Microsoft\Windows\GameDVR", "AllowGameDVR", "REG_DWORD", 0)
    registry_add(r"HKLM\SOFTWARE\Microsoft\PolicyManager\default\ApplicationManagement\AllowGameDVR", "value", "REG_DWORD", 0)

    # Fortnite Priority (Specific form original script)
    registry_add(r"HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\FortniteClient-Win64-Shipping.exe\PerfOptions", "CpuPriorityClass", "REG_DWORD", 2)
    
    # Priority Control
    registry_add(r"HKLM\SYSTEM\ControlSet001\Control\PriorityControl", "Win32PrioritySeparation", "REG_DWORD", 38)
    
    # Menu Delay
    registry_add(r"HKU\.DEFAULT\Control Panel\Desktop", "MenuShowDelay", "REG_SZ", "0")
    
    # Autologgers disable
    loggers = [
        "AppModel", "Cellcore", "Circular Kernel Context Logger", "CloudExperienceHostOobe",
        "DataMarket", "DefenderApiLogger", "DefenderAuditLogger", "HolographicDevice",
        "iclsClient", "iclsProxy", "LwtNetLog", "Mellanox-Kernel",
        "Microsoft-Windows-AssignedAccess-Trace", "Microsoft-Windows-Setup",
        "PEAuthLog", "RdrLog", "ReadyBoot", "SetupPlatform", "SetupPlatformTel",
        "TCPIPLOGGER", "Tpm", "WFP-IPsec Trace"
    ]
    for logger in loggers:
        registry_add(rf"HKLM\SYSTEM\CurrentControlSet\Control\WMI\Autologger\{logger}", "Start", "REG_DWORD", 0)
