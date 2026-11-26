# Platform Surveillance System

A Python command-line utility that periodically records a snapshot of system and running-process information to timestamped log files.

## What it records

Each report includes:

- CPU core count and system CPU usage
- RAM usage and total RAM
- Network bytes sent and received, shown in MB
- Running processes: PID, name, status, CPU usage, and memory usage

The script does not currently send email or collect disk-storage details.

## Requirements

- Python 3
- `psutil`
- `schedule`

Install the required packages from Command Prompt:

```cmd
py -3 -m pip install psutil schedule
```

If `py` is not available, use `python` instead:

```cmd
python -m pip install psutil schedule
```

## Run

Open Command Prompt in the repository folder and provide the interval in minutes followed by the log-folder path:

```cmd
py -3 PlatformServilence_Process_LogXX.py <interval_minutes> <log_folder>
```

For example, to create reports every minute in a `Logs` folder:

```cmd
py -3 PlatformServilence_Process_LogXX.py 1 Logs
```

The folder is created if it does not exist. For a path containing spaces, put it in quotes:

```cmd
py -3 PlatformServilence_Process_LogXX.py 5 "C:\My Logs"
```

The script creates the first report after the specified interval, then repeats on that schedule. Each report is named `Marvellous_<timestamp>.log`. Press **Ctrl+C** in the terminal to stop the scheduler. If you provide a nested folder path, its parent directories must already exist.

## Help

```cmd
py -3 PlatformServilence_Process_LogXX.py --h
py -3 PlatformServilence_Process_LogXX.py --u
```
