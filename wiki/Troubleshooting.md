# Troubleshooting Guide

Common issues and their solutions when using QuizApp.

## 🔧 Installation Issues

### "Module not found" Error

**Problem:** Missing Python packages

**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

If that doesn't work:
```bash
pip3 install -r requirements.txt --user
```

### "Permission denied" Error

**Problem:** Insufficient permissions to install packages

**Solution:**
```bash
# Install in user directory
pip install -r requirements.txt --user

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🗄️ Database Issues

### "Database is locked" Error

**Problem:** Multiple processes accessing the database

**Solution:**
```bash
# Close all running instances
killall python
# Or restart your computer

# Recreate database
rm quiz.db
python setup_database.py
```

### No Questions Appearing

**Problem:** Database is empty or corrupted

**Solution:**
```bash
# Backup existing database (if needed)
cp quiz.db quiz.db.backup

# Recreate database
python setup_database.py

# Verify questions
sqlite3 quiz.db "SELECT COUNT(*) FROM questions;"
```

### Database Schema Error

**Problem:** Old database format

**Solution:**
```bash
# Delete old database
rm quiz.db

# Create new database with current schema
python setup_database.py
```

## 🌐 Server Issues

### "Port already in use" Error

**Problem:** Port 5000 is occupied

**Solution:**
```bash
# Use a different port
PORT=5001 python app.py

# Or kill the process using port 5000
# On Linux/Mac:
lsof -ti:5000 | xargs kill -9

# On Windows:
netstat -ano | findstr :5000
taskkill /PID [PID_NUMBER] /F
```

### "Address already in use" Error

**Problem:** Flask is already running

**Solution:**
```bash
# Find and kill the process
ps aux | grep app.py
kill [PID]

# Or restart your computer
```

### Cannot Access from Mobile

**Problem:** Firewall or network configuration

**Solution:**
1. Make sure you're on the same network
2. Run with host parameter:
   ```bash
   python app.py --host=0.0.0.0
   ```
3. Check firewall:
   ```bash
   # Allow port 5000
   # On Linux: sudo ufw allow 5000
   # On Windows: Check Windows Firewall settings
   ```
4. Use correct IP address (not localhost)

## 🤖 API Issues

### "API key not found" Error

**Problem:** Missing or incorrectly configured API key

**Solution:**
1. Create `.env` file:
   ```bash
   cp .env.example .env
   ```
2. Add your key:
   ```
   GEMINI_API_KEY=your_actual_key_here
   ```
3. Verify:
   ```bash
   cat .env | grep GEMINI_API_KEY
   ```

### "API quota exceeded" Error

**Problem:** Too many API requests

**Solution:**
- Wait for quota reset (usually 24 hours)
- Reduce generation frequency
- Use manual question addition instead

### "Invalid API response" Error

**Problem:** API returned unexpected format

**Solution:**
- Check API key is valid
- Verify internet connection
- Try again after a few minutes
- Check Google AI Studio status

## 📱 Mobile Issues

### Layout Broken on Mobile

**Problem:** CSS not loading or cached

**Solution:**
1. Hard refresh:
   - Chrome: Ctrl+Shift+R (Cmd+Shift+R on Mac)
   - Safari: Cmd+Option+R
2. Clear browser cache
3. Try different browser

### Buttons Not Working on Mobile

**Problem:** JavaScript not loaded

**Solution:**
1. Check browser console for errors
2. Enable JavaScript in browser settings
3. Clear cache and reload
4. Update browser to latest version

### Text Too Small/Large

**Problem:** Viewport not configured

**Solution:**
- Browser zoom should be at 100%
- Check if viewport meta tag exists in HTML
- Try different browser

## 🎨 Theme Issues

### Theme Not Switching

**Problem:** localStorage access blocked

**Solution:**
1. Enable localStorage in browser settings
2. Clear browser data
3. Try incognito/private mode
4. Check browser console for errors

### Theme Not Persisting

**Problem:** Browser clearing localStorage

**Solution:**
- Don't use private/incognito mode
- Check browser privacy settings
- Allow cookies and site data

## 📊 Quiz Issues

### Quiz Not Starting

**Problem:** API endpoint failing

**Solution:**
1. Check browser console
2. Verify database has questions:
   ```bash
   sqlite3 quiz.db "SELECT COUNT(*) FROM questions WHERE category='SSC';"
   ```
3. Restart server
4. Check network tab in DevTools

### Results Not Showing

**Problem:** sessionStorage not available

**Solution:**
1. Enable sessionStorage in browser
2. Don't use private browsing
3. Check browser console for errors
4. Clear browser cache

### Navigation Not Working

**Problem:** JavaScript error

**Solution:**
1. Open browser console (F12)
2. Look for error messages
3. Hard refresh the page
4. Clear cache
5. Try different browser

## 🚀 Deployment Issues

### Heroku Deployment Failed

**Problem:** Missing Procfile or dependencies

**Solution:**
1. Verify Procfile exists:
   ```bash
   cat Procfile
   ```
2. Check requirements.txt:
   ```bash
   pip freeze > requirements.txt
   ```
3. View Heroku logs:
   ```bash
   heroku logs --tail
   ```

### PythonAnywhere Not Working

**Problem:** WSGI configuration

**Solution:**
1. Check WSGI file path is correct
2. Verify virtual environment activated
3. Reload web app
4. Check error logs in Files tab

### GitHub Pages Not Updating

**Problem:** Workflow not running

**Solution:**
1. Check Actions tab on GitHub
2. Enable GitHub Pages in repository settings
3. Verify docs folder exists
4. Check workflow file syntax

## 🔍 Debugging Tips

### Enable Debug Mode

```python
# In app.py, set debug=True
if __name__ == '__main__':
    app.run(debug=True)
```

### Check Logs

```bash
# View Flask logs
python app.py 2>&1 | tee app.log

# View database queries
export FLASK_ENV=development
python app.py
```

### Browser DevTools

1. Press F12 to open DevTools
2. Check Console tab for JavaScript errors
3. Check Network tab for failed requests
4. Check Application tab for localStorage/sessionStorage

### Test API Endpoints

```bash
# Test questions endpoint
curl http://localhost:5000/api/questions?category=SSC

# Check if server is running
curl http://localhost:5000/
```

## 📞 Getting More Help

If your issue isn't listed here:

1. **Search GitHub Issues**: [QuizApp Issues](https://github.com/anacondy/QuizApp/issues)
2. **Ask in Discussions**: [GitHub Discussions](https://github.com/anacondy/QuizApp/discussions)
3. **Report a Bug**: Create a new issue with:
   - Python version
   - Operating system
   - Error message
   - Steps to reproduce

## 🐛 Reporting Bugs

When reporting issues, include:

```
**Environment:**
- OS: [e.g., Windows 10, macOS 12, Ubuntu 20.04]
- Python version: [e.g., 3.9.7]
- Browser: [e.g., Chrome 95, Safari 15]

**Steps to Reproduce:**
1. Step one
2. Step two
3. ...

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happened

**Error Messages:**
```
[Paste error message here]
```

**Screenshots:**
[If applicable]
```

---

**See Also:**
- [FAQ](FAQ.md) - Frequently asked questions
- [Getting Started](Getting-Started.md) - Setup guide
- [User Guide](User-Guide.md) - Usage instructions
