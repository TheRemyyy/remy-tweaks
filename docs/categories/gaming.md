# Gaming Tweaks

The gaming module is designed to minimize input lag, prioritize game processes, and optimize GPU communication.

## 🎮 GPU Optimization

### Hardware-Accelerated GPU Scheduling (HAGS)
- **Key**: `HwSchMode` set to `2`.
- **Effect**: Allows the GPU to manage its own memory more effectively.
- **Benefit**: Reduces latency and improves performance in supported games.

### GPU Priority Tuning
- **Key**: `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games`
- **Settings**:
    - `GPU Priority`: `18`
    - `Priority`: `6`
    - `Scheduling Category`: `High`
- **Benefit**: Ensures that the OS gives maximum priority to gaming applications over background processes.

## ⌨️ Input Latency

### Hardware Queue Sizes
- **Keys**: `MouseDataQueueSize` and `KeyboardDataQueueSize` in `mouclass` and `kbdclass`.
- **Effect**: Sets to `20` (default is often higher).
- **Benefit**: Reduces the buffer size for input data, leading to more immediate mouse and keyboard response.

## 🎥 Windows Gaming Features

### Disabling GameDVR
- **Effect**: Disables background game recording and the Game Bar.
- **Benefit**: Saves CPU cycles and prevents performance drops during gameplay.

### System Responsiveness
- **Key**: `SystemResponsiveness` set to `0`.
- **Benefit**: Gives multimedia and gaming tasks 100% of the CPU resources when they are in the foreground, rather than reserving a percentage for the system.
