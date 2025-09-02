# BeA: Bacoor e-Assistant

BeA is a simple desktop chatbot built with Python and Tkinter. It provides quick answers about local services like Postal ID, Police Clearance, Senior Citizen ID, Business Permit, Civil Registration, and Cedula.

## Requirements
- Windows 10/11
- Python 3.9+ (includes Tkinter by default on Windows)

## Project structure
- `chatApp.py` — Tkinter UI (main entry point)
- `bot_2.py` — Rule-based chatbot responses

## Run locally
```powershell
# From the project folder
py -3 chatApp.py
```

If you have multiple Python versions:
```powershell
python chatApp.py
```

## Package as a Windows .exe (PyInstaller)
1. Create/activate a virtual environment and install PyInstaller:
```powershell
py -3 -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip pyinstaller
```

2. Build the executable:
```powershell
pyinstaller --onefile --windowed --name BeA chatApp.py
```
- Output: `dist\BeA.exe`
- Optional icon: add `--icon path\to\icon.ico`

3. Distribute
- Share `dist\BeA.exe` directly, or zip it first to avoid browser/AV false positives.
- For maximum compatibility with antivirus, use the non-onefile build:
```powershell
pyinstaller --windowed --name BeA chatApp.py
# Then distribute the entire folder: dist\BeA
```

## Usage tips
- Enter your question in the input box and press Enter or click Send.
- Use quick action buttons on the right for common queries.
