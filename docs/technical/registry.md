# Internal Registry Logic

This document serves as a reference for the most critical registry modifications performed by Remy Tweaks.

## Registry Helper (`utils.py`)
Remy Tweaks uses a helper function to modify registry keys safely via the Windows command line:
`reg add "<key>" /v "<value_name>" /t <type> /d <data> /f`

## Critical Keys Reference

| Category | Registry Path | Value Name | Target Data |
| :--- | :--- | :--- | :--- |
| **HAGS** | `...\Control\GraphicsDrivers` | `HwSchMode` | `2` |
| **Throttling** | `...\Control\Power\PowerThrottling` | `PowerThrottlingOff` | `1` |
| **Responsiveness**| `...\Multimedia\SystemProfile` | `SystemResponsiveness`| `0` |
| **Kernel Paging** | `...\Memory Management` | `DisablePagingExecutive`| `1` |
| **Bg Apps** | `...\BackgroundAccessApplications`| `GlobalUserDisabled` | `1` |
| **Fast Startup** | `...\Session Manager\Power` | `HiberbootEnabled` | `1` |

## Key Cleaning
The utility also performs cleaning of the following autorun paths:
- `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
- `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
- `HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run`

*Note: Remy Tweaks uses `/f` to force the modification or deletion, ensuring that existing values are overwritten.*
