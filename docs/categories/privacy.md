# Privacy & Telemetry Tweaks

Remy Tweaks takes a strict stance on user privacy. This module disables invasive telemetry, tracking services, and background data collection.

## 🛡️ Core Telemetry

### Disabling Diagnostic Data
- **Effect**: Disables Windows Error Reporting and Customer Experience Improvement Programs (CEIP).
- **Benefit**: Reduces background network activity and prevents system snapshots from being sent to Microsoft.

### Scheduled Tasks Cleanup
- **Effect**: Disables over 20+ hidden diagnostic tasks including:
    - `Microsoft Compatibility Appraiser`
    - `ProgramDataUpdater`
    - `DiskDiagnosticDataCollector`
- **Benefit**: Eliminates random CPU spikes caused by background "maintenance" tasks.

## 🕵️ Third-Party Telemetry

### Nvidia Telemetry
- **Effect**: Disables `SendTelemetryData` in registry and stops Nvidia-specific diagnostic scheduled tasks.
- **Benefit**: Keeps your GPU driver focused on rendering, not reporting.

### Chrome & Browser Privacy
- **Effect**: Implements policies to disable Metrics Reporting and the "Software Reporter Tool" (which scans your drive).
- **Benefit**: Faster browser startup and improved local privacy.

## ✍️ Input Privacy

### Handwriting & Inking
- **Effect**: Disables `RestrictImplicitInkCollection` and `RestrictImplicitTextCollection`.
- **Benefit**: Prevents Windows from learning your typing and writing patterns for "improvement".

### TIPC (Touch Input Personalization)
- **Effect**: Completely disables the TIPC engine.
- **Benefit**: Prevents personalization data from being collected from touch and ink inputs.
