# Getting Started with QuizApp

This guide will help you set up QuizApp on your local machine or deploy it to a cloud platform.

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.8+** installed ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package installer)
- **Git** ([Download Git](https://git-scm.com/downloads))
- *(Optional)* **Google Gemini API Key** for AI features ([Get API Key](https://makersuite.google.com/app/apikey))

## 🔧 Local Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/anacondy/QuizApp.git
cd QuizApp
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- google-generativeai (AI question generation)
- python-dotenv (environment variable management)
- schedule (task scheduling)
- gunicorn (production server)

### Step 3: Set Up the Database

```bash
python setup_database.py
```

This creates `quiz.db` with sample questions for all exam categories.

### Step 4: Configure Environment Variables (Optional)

For AI-powered question generation, create a `.env` file:

```bash
cp .env.example .env
```

Edit `.env` and add your API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

### Step 5: Run the Application

```bash
python app.py
```

The application will start at `http://localhost:5000`

### Step 6: Test the Application

1. Open your browser and navigate to `http://localhost:5000`
2. Select an exam category (SSC, BANK, or RRB)
3. Take a quiz
4. Review your results

## 🌐 Accessing from Mobile Devices

To test on mobile devices on the same network:

1. Find your computer's local IP address:
   - **Windows**: `ipconfig` → Look for IPv4 Address
   - **Mac/Linux**: `ifconfig` → Look for inet address

2. Run the app with network access:
   ```bash
   python app.py --host=0.0.0.0
   ```

3. Access from mobile:
   ```
   http://YOUR_IP_ADDRESS:5000
   ```

## 🤖 Setting Up AI Question Generation

### Getting a Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key to your `.env` file

### Testing Question Generation

```bash
# Generate questions immediately
python scheduler.py --now
```

This will generate and add new questions to the database.

### Setting Up Automated Updates

For daily automatic question updates:

```bash
# Run scheduler (keeps running in background)
python scheduler.py
```

Or use a system service (see [Deployment Guide](Deployment-Guide.md) for production setup).

## 📱 Verifying Mobile Optimization

Test on various screen sizes:

1. **Chrome DevTools**:
   - Press F12 → Click device toggle icon
   - Test on iPhone, Samsung Galaxy, iPad

2. **Responsive Breakpoints**:
   - Mobile: < 768px
   - Tablet: 768px - 1024px
   - Desktop: > 1024px

## ✅ Verification Checklist

After setup, verify:

- [ ] Application runs without errors
- [ ] Database contains questions
- [ ] All three categories work (SSC, BANK, RRB)
- [ ] Quiz can be completed
- [ ] Results page displays correctly
- [ ] Theme toggle works
- [ ] Mobile view renders properly

## 🔄 Next Steps

- [User Guide](User-Guide.md) - Learn how to use all features
- [Developer Guide](Developer-Guide.md) - Start developing
- [Deployment Guide](Deployment-Guide.md) - Deploy to production

## ❓ Troubleshooting

### Common Issues

**"Module not found" errors**
```bash
pip install -r requirements.txt --upgrade
```

**"Port already in use"**
```bash
# Use a different port
python app.py --port=5001
```

**Database errors**
```bash
# Recreate database
rm quiz.db
python setup_database.py
```

For more help, see [Troubleshooting Guide](Troubleshooting.md).
