# Architecture

Remy Tweaks is built with a modular, functional design using Python.

## Directory Structure

- `main.py`: The entry point and TUI (Text User Interface) menu.
- `ui.py`: Handles all console output, colors, and the main menu display.
- `utils.py`: Contains low-level wrapper functions for interacting with the Windows OS.
- `tweaks/`: A package containing specialized modules for each optimization category.

## Core Modules

### `utils.py`
Provides abstractions for:
- `run_command(cmd)`: Executes shell commands.
- `registry_add(key, name, type, data)`: Adds/Modifies registry values.
- `registry_delete(path)`: Removes registry keys or values.
- `service_config(name, start_type)`: Configures Windows services.
- `schtasks_disable(task_path)`: Disables scheduled tasks.

### `tweaks/*.py`
Each file (performance, gaming, privacy, etc.) is a collection of functions that use the `utils` layer to apply specific modifications. This makes the code highly readable and easy to audit.

## Execution Flow

1.  **Launch**: `main.py` is executed with Admin privileges.
2.  **Menu**: `ui.show_menu()` displays the available options.
3.  **Dispatch**: The user's choice triggers a specific function in one of the `tweaks` modules.
4.  **Application**: The function calls `utils` helpers to modify the system.
5.  **Feedback**: `ui.print_done()` notifies the user that the tweak has been applied.
