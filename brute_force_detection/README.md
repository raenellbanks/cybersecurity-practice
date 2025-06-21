# Brute Force Detection Drill

This drill contains a Python script to analyze auth logs and detect brute force login attempts by identifying IPs with multiple failed attempts within a 5-minute window.

## Files

- `detect_bruteforce.py`: Python script performing the detection
- `auth.log`: Sample authentication log file for testing

## How to run

Run the Python script in the same directory as the log file:

```bash
python detect_bruteforce.py
