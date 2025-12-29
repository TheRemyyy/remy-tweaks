# Services & Bloat Cleanup

Windows comes with hundreds of services, many of which are useless for the average user. Remy Tweaks disables over 50 of these by default.

## 🧹 Service Optimization

The `disable_unnecessary_services` function targets services in the following categories:

- **Diagnostics & Feedback**: `DiagTrack` (Connected User Experiences), `diagsvc`, `WdiServiceHost`.
- **Remote & Sensors**: `SensorService`, `SensorDataService`, `lfsvc` (Geolocation).
- **Print & Imaging**: `StiSvc` (Still Image Acquisition) if not needed.
- **Legacy & Compatibility**: `TapiSvc` (Telephony), `ALG` (Application Layer Gateway).
- **Redundancy**: `SysMain` (Superfetch - often detrimental on modern SSDs), `defragsvc`.

## 📱 Background Apps

### Global Disable
- **Effect**: Sets `GlobalUserDisabled` to `1` in the `BackgroundAccessApplications` registry key.
- **Benefit**: Prevents UWP/Microsoft Store apps from running in the background, saving significant RAM and CPU cycles.

## 🖥️ UI & Experience

### Aero Peek
- **Effect**: Disables the Aero Peek transparency feature.
- **Benefit**: Reduces GPU load and simplifies the desktop window manager (DWM) composition.

### Prelaunch & Startup
- **Effect**: Disables Microsoft Edge prelaunching.
- **Benefit**: Prevents Edge from consuming memory even when it's not open.
- **Cleanup**: Removes common "Run" and "RunOnce" entries from the registry to ensure a clean startup.
