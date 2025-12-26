import subprocess
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_command(command, shell=True):
    """Executes a system command silently."""
    try:
        subprocess.run(command, shell=shell, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

def registry_add(key, value_name, value_type, value_data):
    """Adds or updates a registry key."""
    cmd = f'reg add "{key}" /v "{value_name}" /t {value_type} /d "{value_data}" /f'
    run_command(cmd)

def registry_delete(key, value_name=None):
    """Deletes a registry key or value."""
    if value_name:
        cmd = f'reg delete "{key}" /v "{value_name}" /f'
    else:
        cmd = f'reg delete "{key}" /f'
    run_command(cmd)

def service_config(service_name, start_type="disabled"):
    """Configures a Windows service."""
    run_command(f'sc stop "{service_name}"')
    run_command(f'sc config "{service_name}" start= {start_type}')

def schtasks_disable(task_path):
    """Disables a scheduled task."""
    cmd = f'schtasks /change /TN "{task_path}" /DISABLE'
    run_command(cmd)
