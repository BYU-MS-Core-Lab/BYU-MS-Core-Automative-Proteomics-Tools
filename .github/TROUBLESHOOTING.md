# Troubleshooting Guide

## Common Issues and Solutions

### 1. "No module named 'encodings'" or "Failed to import encodings module"

**Error Message:**
```
Fatal Python error: Failed to import encodings module
ModuleNotFoundError: No module named 'encodings'
```

**Cause:**
Your Python installation is corrupted or the system Python is not properly configured.

**Solutions:**

**Option A: Use Virtual Environment (Recommended)**
```bash
# Windows (PowerShell or Command Prompt)
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -e ".[dev]"

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Then use the launcher scripts which will automatically detect and use the virtual environment.

**Option B: Reinstall Python**
1. Download Python 3.10+ from [python.org](https://www.python.org/downloads/)
2. **Important:** Check "Add Python to PATH" during installation
3. Restart your terminal/command prompt
4. Run the setup script: `python scripts/setup_dev.py` or `.\scripts\setup_dev.ps1`

**Option C: Use Pixi (If installed)**
```bash
pixi run python launcher.py
```

---

### 2. "Python not found" Error

**Error Message:**
```
ERROR: Python not found or not properly installed!
```

**Cause:**
Python is not installed or not in your system PATH.

**Solution:**
1. Download Python 3.10+ from [python.org](https://www.python.org/downloads/)
2. **Important:** Check "Add Python to PATH" during installation
3. Close all terminal windows completely
4. Open a new terminal and run: `python --version`
5. If still not found, you may need to restart your computer

---

### 3. "Port 5000 already in use"

**Error Message:**
```
Error: Address already in use
```

**Cause:**
Another application is already using port 5000.

**Solutions:**

**Option A: Change the Port**
```bash
# Windows (Command Prompt or PowerShell)
set FLASK_PORT=5001
python launcher.py

# macOS/Linux
export FLASK_PORT=5001
python launcher.py
```

**Option B: Kill the Process Using Port 5000**

**Windows (PowerShell):**
```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace 1234 with the PID)
taskkill /PID 1234 /F
```

**macOS/Linux:**
```bash
# Find and kill process using port 5000
lsof -i :5000
kill -9 <PID>
```

---

### 4. "No module named 'flask'" or Other Missing Dependencies

**Error Message:**
```
ModuleNotFoundError: No module named 'flask'
```

**Cause:**
Dependencies are not installed in your Python environment.

**Solution:**
```bash
# Activate your environment first
# Windows
.\.venv\Scripts\activate.bat
# macOS/Linux
source .venv/bin/activate

# Then install dependencies
pip install -e ".[dev]"
```

Or use the automated setup script:
```bash
# Windows PowerShell
.\scripts\setup_dev.ps1

# macOS/Linux
bash scripts/setup_dev.sh

# Any platform
python scripts/setup_dev.py
```

---

### 5. "Command not found: npm" (For Frontend Development)

**Error Message:**
```
npm: command not found
```

**Cause:**
Node.js is not installed.

**Solution:**
1. Download Node.js 18+ from [nodejs.org](https://nodejs.org/)
2. Install it (it includes npm)
3. Restart your terminal
4. Run: `npm --version` to verify installation
5. Then install frontend dependencies: `cd programs/mspp_web/frontend && npm install`

---

### 6. "CORS errors" or "Cannot POST /api/upload"

**Error Messages:**
```
Access to XMLHttpRequest blocked by CORS policy
POST http://localhost:5000/api/upload 404 (Not Found)
```

**Cause:**
Frontend and backend servers are not properly communicating, or the Flask backend is not running.

**Solution:**

**Check if Flask is Running:**
```bash
# This should show "OK" or no error
curl http://localhost:5000/api/health
```

**Check Port Configuration:**
```bash
# Make sure both are using the correct ports
python launcher.py  # Backend runs on 5000
# In another terminal:
cd programs/mspp_web/frontend && npm run dev  # Frontend on 3000
```

**Check CORS Configuration:**
- Ensure `CORS_ORIGINS` environment variable includes the frontend URL
- Default: `http://localhost:3000,http://localhost:5000`

---

### 7. "Frontend Not Loading" (Blank Page)

**Cause:**
The frontend files haven't been built yet.

**Solution:**

**For Development:**
```bash
cd programs/mspp_web/frontend
npm run dev
# Then open http://localhost:3000 in your browser
```

**For Production:**
```bash
cd programs/mspp_web/frontend
npm run build
# Then visit http://localhost:5000 in your browser
```

---

### 8. Virtual Environment Not Activating

**Error Message:**
```
'activate' is not recognized as an internal command
```

**Cause:**
Incorrect activation command for your OS/shell.

**Solution:**

**Windows:**
```bash
# PowerShell
.\.venv\Scripts\Activate.ps1

# Command Prompt (cmd.exe)
.venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

If you get a permission error on macOS/Linux:
```bash
chmod +x .venv/bin/activate
source .venv/bin/activate
```

---

## Getting Help

If your issue isn't listed here:

1. **Check the logs** - The error message usually tells you what's wrong
2. **Run the setup script** - This fixes most environment issues:
   ```bash
   python scripts/setup_dev.py
   ```
3. **Check CONTRIBUTING.md** - Has more detailed setup and development info
4. **Open an issue** on GitHub with:
   - Error message (full output)
   - Operating system
   - Python version (`python --version`)
   - Steps to reproduce

---

## Quick Reference: Environment Variables

```bash
# Backend Configuration
FLASK_HOST=127.0.0.1          # Where Flask listens (default: localhost only)
FLASK_PORT=5000               # Backend port (default: 5000)
FLASK_ENV=development         # Set to 'production' to disable debug mode
CORS_ORIGINS=http://localhost:3000,http://localhost:5000

# Frontend Configuration
VITE_PORT=3000                # Frontend dev server port
VITE_API_PROXY=http://localhost:5000  # API target

# Application
MSPP_TEMP_DIR=/custom/path    # Custom temp directory for uploads
```

Set these in your terminal before running the launchers, or create a `.env` file based on [.env.example](.env.example).

---

**Last Updated:** March 5, 2026
