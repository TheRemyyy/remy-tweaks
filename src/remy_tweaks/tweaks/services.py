from ..utils import run_command, registry_add, service_config, schtasks_disable

def disable_background_apps():
    registry_add(r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications", "GlobalUserDisabled", "REG_DWORD", 1)
    registry_add(r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search", "BackgroundAppGlobalToggle", "REG_DWORD", 0)
    registry_add(r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Search", "BackgroundAppGlobalToggle", "REG_DWORD", 0)

def disable_aero_peek():
    registry_add(r"HKEY_CURRENT_USER\Software\Microsoft\Windows\DWM", "EnableAeroPeek", "REG_DWORD", 0)

def disable_prelaunch():
    registry_add(r"HKLM\SOFTWARE\Wow6432Node\Policies\Microsoft\MicrosoftEdge\Main", "AllowPrelaunch", "REG_DWORD", 0)

def disable_unnecessary_services():
    services = [
        ("TapiSrv", 3), ("FontCache3.0.0.0", 4), ("SEMgrSvc", 4), ("PNRPsvc", 4),
        ("LanmanWorkstation", 3), ("WEPHOSTSVC", 3), ("p2psvc", 4), ("p2pimsvc", 4),
        ("PhoneSvc", 4), ("wuauserv", 3), ("Wecsvc", 4), ("SensorDataService", 4),
        ("SensrSvc", 3), ("perceptionsimulation", 4), ("StiSvc", 3), ("OneSyncSvc", 4),
        ("ConsentUxUserSvc", 3), ("DevicePickerUserSvc", 3), ("DevicesFlowUserSvc", 3),
        ("WMPNetworkSvc", 4), ("MessagingService", 3), ("CaptureService", 4),
        ("CDPUserSvc", 4), ("PimIndexMaintenanceSvc", 4), ("BcastDVRUserService", 3),
        ("DeviceAssociationBrokerSvc", 3), ("cbdhsvc", 3), ("edgeupdatem", 4),
        ("MicrosoftEdgeElevationService", 4), ("ALG", 4), ("QWAVE", 4),
        ("IpxlatCfgSvc", 3), ("icssvc", 3), ("DusmSvc", 3), ("MapsBroker", 4),
        ("edgeupdate", 4), ("SensorService", 3), ("shpamsvc", 4), ("svsvc", 4),
        ("SysMain", 4), ("MSiSCSI", 4), ("ssh-agent", 4), ("CscService", 4),
        ("AppReadiness", 3), ("tzautoupdate", 3), ("wisvc", 4), ("defragsvc", 4),
        ("SharedRealitySvc", 4), ("RetailDemo", 4), ("lltdsvc", 4), ("TrkWks", 4),
        ("CryptSvc", 4), ("lfsvc", 4), ("DiagTrack", 3), ("diagsvc", 4),
        ("DPS", 4), ("WdiServiceHost", 4), ("WdiSystemHost", 4), ("dmwappushsvc", 4),
        ("diagnosticshub.standardcollector.service", 4), ("TroubleshootingSvc", 4),
        ("DsSvc", 4), ("dmwappushservice", 4), ("FrameServer", 4),
        ("FontCache", 4), ("InstallService", 3), ("OSRSS", 4), ("sedsvc", 4),
        ("SENS", 4), ("TabletInputService", 3), ("Themes", 4)
    ]

    for svc, val in services:
        registry_add(rf"HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\{svc}", "Start", "REG_DWORD", val)
    
    # CurrentControlSet specific ones in original script
    cc_services = [
        ("ConsentUxUserSvc", 3), ("DevicePickerUserSvc", 3), ("DevicesFlowUserSvc", 3),
        ("MessagingService", 3), ("CaptureService", 4), ("CDPUserSvc", 4),
        ("PimIndexMaintenanceSvc", 4), ("BcastDVRUserService", 3),
        ("DeviceAssociationBrokerSvc", 3), ("cbdhsvc", 3)
    ]
    for svc, val in cc_services:
        registry_add(rf"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\{svc}", "Start", "REG_DWORD", val)

    # Clean up RUN keys
    paths = [
        r"HKSU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce",
        r"HKSU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
        r"HKSU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies",
        r"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce",
        r"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run",
        r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServicesOnce",
        r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServices",
        r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnceEx",
        r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    ]
    # Note: Using registry_delete carefully defined in utils for keys vs values
    for path in paths:
        # Original script used REG DELETE Key /f which deletes the whole key
        from ..utils import registry_delete
        registry_delete(path)
