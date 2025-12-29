# Performance Tweaks

The performance module focuses on reducing CPU overhead, optimizing memory management, and ensuring that system resources are prioritized for user tasks.

## 🧠 Memory Management

### Filesystem Memory Usage
- **Command**: `fsutil behavior set memoryusage 2`
- **Effect**: Increases the size of the NTFS internal cache and the paged pool memory.
- **Benefit**: Faster file operations and improved responsiveness for large file systems.

### Large System Cache
- **Key**: `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\LargeSystemCache`
- **Effect**: Sets to `1`.
- **Benefit**: Improves performance of the file system cache at the cost of some application memory.

### Disabling Paging Executive
- **Key**: `DisablePagingExecutive` set to `1`.
- **Effect**: Prevents kernel-mode drivers and system code from being paged to the disk.
- **Benefit**: Faster system response as critical code is always kept in physical RAM.

## ⚡ CPU & Power

### Power Throttling
- **Effect**: Disables Intel/AMD Power Throttling across all control sets.
- **Benefit**: Prevents the OS from lowering the CPU clock speed of background tasks, reducing micro-stuttering.

### Ultimate Performance Power Plan
- **Command**: `powercfg setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c`
- **Effect**: Activates the hidden "Ultimate Performance" plan (Windows 10/11 Pro/Workstation only).
- **Benefit**: Eliminates latencies associated with power state transitions.

## 💿 Disk & Boot

### Fast Startup
- **Effect**: Enables `HiberbootEnabled`.
- **Benefit**: Speeds up the boot process by saving the kernel state during shutdown.

### Disabling Hibernation
- **Effect**: Disables `HibernateEnabled`.
- **Benefit**: Frees up gigabytes of disk space (size of your RAM) and reduces SSD wear.

### BCD Tweaks
- **Commands**:
  - `bcdedit /set disabledynamictick yes`
  - `bcdedit /set useplatformtick yes`
- **Benefit**: Fixes several timer-related issues and improves synchronization between CPU and hardware timers.
