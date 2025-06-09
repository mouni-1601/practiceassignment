# System Uptime Script

This Python script displays the system uptime for Windows, Linux, and macOS systems. It determines the operating system at runtime and uses the appropriate method to fetch and display the uptime.

## Features

- **Cross-platform support**: Works on Windows, Linux, and macOS.
- **Windows**: Uses `net stats srv` to extract the boot time and computes uptime.
- **Linux**: Reads `/proc/uptime` to get the uptime in seconds.
- **macOS**: Falls back to using the `uptime` command.

## Usage

1. **Clone or download the script:**

    Save the script as `get_uptime.py`.

2. **Run the script:**

    ```bash
    python get_uptime.py
    ```

    The script will print the system uptime in a human-readable format.

## Requirements

- Python 3.x
- Works out-of-the-box on most systems (no extra packages required).

## How it works

- **Windows**:
    - Runs `net stats srv` and searches for the line starting with "Statistics since".
    - Parses the boot date/time and calculates the uptime.

- **Linux**:
    - Reads `/proc/uptime` to get the uptime in seconds and formats the output.

- **macOS**:
    - Tries to read `/proc/uptime` first.
    - If not available, falls back to the `uptime` shell command.

## Example Output

```
System Uptime: 2 hours, 34 minutes, 12 seconds
```
or on Windows:
```
System Uptime: 0:34:12.123456
```
or on macOS:
```
System Uptime:  9:44  up 2 days,  2:59, 2 users, load averages: 1.45 1.36 1.29
```

## Notes

- The script attempts to parse several common Windows date formats, but may not work with all locale settings.
- On macOS, the output is the raw result of the `uptime` command.

## License

This script is provided as-is, without warranty or support.
