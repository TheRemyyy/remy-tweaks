# Safety & Restoration

Modifying system settings and registry keys always carries a risk. Please follow these guidelines to ensure you can recover your system if anything goes wrong.

## 🛡️ Step 1: Create a System Restore Point

Before running any tweaks, you **MUST** create a restore point:
1.  Open the **Start Menu**, search for "Create a restore point".
2.  Click the **Create** button at the bottom.
3.  Name it (e.g., "Before Remy Tweaks") and click **Create**.

## 🔄 Step 2: Backup your Registry

1.  Press `Win + R`, type `regedit`, and press Enter.
2.  Select **File -> Export**.
3.  Select "All" under Export range and save the `.reg` file to an external drive.

## ⚠️ Known Risks

- **Services**: Disabling certain services might break specific features (e.g., disabling `FontCache` might slightly delay text rendering in some apps).
- **BCD Tweaks**: On some older hardware, BCD modifications might lead to boot issues. If this happens, use Windows Recovery to revert BCD settings.
- **Background Apps**: Disabling them globally means you won't receive notifications from Mail, Calendar, or other Windows apps unless they are open.

## 🛠️ Reverting Changes

Currently, Remy Tweaks does not have an automatic "Undo" button. To revert changes:
1.  **Use System Restore**: This is the fastest and most reliable way.
2.  **Manual Revert**: You can find the specific registry key in the documentation and set its value back to the Windows default (usually `0` or `1`).
