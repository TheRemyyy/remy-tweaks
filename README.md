<div align="center">

# Remy Tweaks

**Ultimate Windows Optimization Utility**

[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square&logo=windows&logoColor=white)](https://microsoft.com/windows)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)

*A powerful, modular Python utility for optimizing Windows performance, privacy, and gaming experience.*

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Safety](#safety)

</div>

---

## Overview

Remy Tweaks is a comprehensive system optimization tool designed to reclaim your PC's performance. By disabling unnecessary telemetry, optimizing service configurations, and fine-tuning hardware scheduling, it ensures your system runs at its absolute peak potential.

### Key Features

- **🚀 Performance** — Optimize CPU scheduling, memory management, and power plans for raw speed.
- **🛡️ Privacy** — Disable invasive telemetry, tracking services, and unwanted data collection.
- **🎮 Gaming** — Fine-tune GPU settings, disable GameDVR, and prioritize game processes.
- **🧹 Cleanliness** — remove bloatware, disable background apps, and streamline startup.
- **⚙️ Modular** — Clean, safe python codebase that is easy to audit and extend.

## <a id="installation"></a>📦 Installation

### Prerequisites

- Windows 10 or Windows 11
- Python 3.8 or higher

### Setup

```bash
git clone https://github.com/TheRemyyy/remy-tweaks.git
cd remy-tweaks
```

## <a id="usage"></a>🚀 Usage

Run the utility as **Administrator** to ensure all system tweaks can be applied correctly.

```bash
python -m src.remy_tweaks.main
```

### Menu Options

| Category | Option | Description |
| :--- | :--- | :--- |
| **Performance** | `[1]` Memory Usage | Optimize filesystem memory usage |
| | `[7]` Power Throttling | Disable power throttling for max performance |
| | `[8]` HAGS | Enable Hardware Accelerated GPU Scheduling |
| | `[18]` Ultimate Plan | Activate High Performance power plan |
| **Network** | `[2]` Wifi Sense | Disable Wifi Sense credential sharing |
| | `[6]` Xbox Network | Disable Xbox Live networking services |
| **Privacy** | `[15]` Secure Windows | Comprehensive telemetry and tracking disable |
| | `[22]` Telemetry | Disable customer experience improvement programs |
| **Services** | `[10]` Background Apps | Prevent apps from running in the background |
| | `[23]` Bloat Services | Disable 50+ unnecessary system services |

## <a id="safety"></a>⚠️ Safety & Disclaimer

**Use at your own risk.**

While these tweaks are tested and commonly used in the optimization community, modifying Windows Registry and Services can potentially affect system stability.

- Always create a **System Restore Point** before applying tweaks.
- Review the source code in `src/remy_tweaks/tweaks/` to understand exactly what each option does.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
<sub>Made with ❤️ by TheRemyyy</sub>
</div>
