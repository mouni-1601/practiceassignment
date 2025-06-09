


import os
import platform

def get_uptime():
    system = platform.system()
    if system == "Windows":
        # Windows does not provide uptime directly; use 'net stats srv'
        try:
            output = os.popen('net stats srv').read()
            for line in output.splitlines():
                if line.lower().startswith('statistics since'):
                    from datetime import datetime
                    import re
                    # Extract the date/time from the line
                    date_str = line[len('Statistics since'):].strip()
                    # Try parsing the date
                    for fmt in ("%m/%d/%Y %I:%M:%S %p", "%d-%m-%Y %H:%M:%S", "%d/%m/%Y %H:%M:%S"):
                        try:
                            boot_time = datetime.strptime(date_str, fmt)
                            break
                        except Exception:
                            continue
                    else:
                        print("Could not parse boot time.")
                        return
                    uptime = datetime.now() - boot_time
                    print(f"System Uptime: {uptime}")
                    return
            print("Could not determine uptime from command output.")
        except Exception as e:
            print(f"Error retrieving uptime: {e}")
    else:
        # Unix/Linux/Mac
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                hours = int(uptime_seconds // 3600)
                minutes = int((uptime_seconds % 3600) // 60)
                seconds = int(uptime_seconds % 60)
                print(f"System Uptime: {hours} hours, {minutes} minutes, {seconds} seconds")
        except FileNotFoundError:
            # macOS fallback: use 'uptime' command
            output = os.popen('uptime').read().strip()
            print(f"System Uptime: {output}")

if __name__ == "__main__":
    get_uptime()
