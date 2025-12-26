from ..utils import run_command, registry_add, schtasks_disable

def make_windows_secure():
    # Privacy & Telemetry
    registry_add(r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search", "AllowSearchToUseLocation", "REG_DWORD", 0)
    registry_add(r"HKLM\SYSTEM\CurrentControlSet\Services\nvlddmkm\Global\Startup", "SendTelemetryData", "REG_DWORD", 0)
    
    # Nvidia Tasks
    schtasks_disable(r"NvTmMon_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}")
    schtasks_disable(r"NvTmRep_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}")
    schtasks_disable(r"NvTmRepOnLogon_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}")
    
    # Chrome Policies
    chrome = r"HKLM\SOFTWARE\Policies\Google\Chrome"
    registry_add(chrome, "MetricsReportingEnabled", "REG_DWORD", 0)
    registry_add(chrome, "ChromeCleanupReportingEnabled", "REG_DWORD", 0)
    
    # Explorer
    registry_add(r"HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun", "1", "REG_SZ", "software_reporter_tool.exe")
    
    # Privacy / Feedback
    registry_add(r"HKLM\Software\Policies\Microsoft\SQMClient\Windows", "CEIPEnable", "REG_DWORD", 0)
    registry_add(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Biometrics\FacialFeatures", "EnhancedAntiSpoofing", "REG_DWORD", 1)
    
    # Assistance
    registry_add(r"HKEY_CURRENT_USER\Software\Policies\Microsoft\Assistance\Client\1.0", "NoExplicitFeedback", "REG_DWORD", 1)
    registry_add(r"HKEY_CURRENT_USER\Software\Policies\Microsoft\Assistance\Client\1.0", "NoImplicitFeedback", "REG_DWORD", 1)
    registry_add(r"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Assistance\Client\1.0", "NoActiveHelp", "REG_DWORD", 1)

    # Input / Handwriting
    registry_add(r"HKEY_CURRENT_USER\Software\Policies\Microsoft\InputPersonalization", "RestrictImplicitInkCollection", "REG_DWORD", 1)
    registry_add(r"HKEY_CURRENT_USER\Software\Policies\Microsoft\InputPersonalization", "RestrictImplicitTextCollection", "REG_DWORD", 1)
    
    # Error Reporting
    registry_add(r"HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Windows Error Reporting", "Disabled", "REG_DWORD", 1)
    
    # Delivery Optimization
    registry_add(r"HKLM\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization", "DODownloadMode", "REG_DWORD", 0)


def disable_telemetry():
    registry_add(r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "Start_TrackProgs", "REG_DWORD", 0)
    
    tasks = [
        r"\Microsoft\Windows\Customer Experience Improvement Program\Consolidator",
        r"\Microsoft\Windows\Customer Experience Improvement Program\BthSQM",
        r"\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask",
        r"\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser",
        r"\Microsoft\Windows\Application Experience\ProgramDataUpdater",
        r"\Microsoft\Windows\Application Experience\StartupAppTask",
        r"\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector",
        r"\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem",
        r"\Microsoft\Windows\Shell\FamilySafetyMonitor",
        r"\Microsoft\Windows\Shell\FamilySafetyUpload",
        r"\Microsoft\Windows\Autochk\Proxy",
        r"\Microsoft\Windows\Maintenance\WinSAT",
        r"\Microsoft\Windows\Application Experience\AitAgent",
        r"\Microsoft\Windows\Windows Error Reporting\QueueReporting",
        r"\Microsoft\Windows\CloudExperienceHost\CreateObjectTask",
        r"\Microsoft\Windows\DiskFootprint\Diagnostics",
        r"\Microsoft\Windows\FileHistory\File History (maintenance mode)",
        r"\Microsoft\Windows\PI\Sqm-Tasks",
        r"\Microsoft\Windows\AppID\SmartScreenSpecific",
        r"\Microsoft\Office\OfficeTelemetryAgentFallBack2016",
        r"\Microsoft\Office\OfficeTelemetryAgentLogOn2016"
    ]
    for task in tasks:
        schtasks_disable(task)

def disable_tipc():
    registry_add(r"HKLM\SOFTWARE\Microsoft\Input\TIPC", "Enabled", "REG_DWORD", 0)
    registry_add(r"HKCU\SOFTWARE\Microsoft\Input\TIPC", "Enabled", "REG_DWORD", 0)
