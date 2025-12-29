<div align="center">

# Remy Tweaks

**Ultimate Windows Optimization Utility**

[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square&logo=windows&logoColor=white)](https://microsoft.com/windows)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)

*A powerful, modular Python utility for optimizing Windows performance, privacy, and gaming experience.*

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Documentation](#documentation)

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

## <a id="documentation"></a>📄 Documentation

For deep-dive information on every modification, please refer to our documentation in the `docs/` directory:

### Optimization Categories
- 🚀 **[Performance](docs/categories/performance.md)** — CPU, RAM, and Power.
- 🎮 **[Gaming](docs/categories/gaming.md)** — GPU and Latency.
- 🛡️ **[Privacy](docs/categories/privacy.md)** — Telemetry and Sledování.
- 🌐 **[Network](docs/categories/network.md)** — Connectivity bloat.
- 🧹 **[Services](docs/categories/services.md)** — Bloatware removal.

### Technical & Safety
- 📖 **[Documentation Overview](docs/overview.md)** — Starting point.
- ⚠️ **[Safety & Restoration](docs/technical/safety.md)** — **READ THIS FIRST**.
- 🏗️ **[Architecture](docs/technical/architecture.md)** — How it works.
- 📝 **[Registry Reference](docs/technical/registry.md)** — Modified keys.

## <a id="safety"></a>⚠️ Safety & Disclaimer

**Use at your own risk.**

While these tweaks are tested and commonly used in the optimization community, modifying Windows Registry and Services can potentially affect system stability. **Always create a System Restore Point before applying tweaks.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
<sub>Made with ❤️ by TheRemyyy</sub>
</div>