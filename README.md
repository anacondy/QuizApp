# 🎓 QuizApp - Government Exam Preparation Platform

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://anacondy.github.io/QuizApp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)](https://flask.palletsprojects.com/)

**Live Demo:** [https://anacondy.github.io/QuizApp/](https://anacondy.github.io/QuizApp/)

A modern, AI-powered quiz application designed for Indian government competitive exam preparation. Practice questions for SSC, Bank, and RRB exams with automated daily updates.

## ✨ Features

- 🤖 **AI-Powered Questions**: Automated question generation using Google Gemini API
- 📅 **Daily Updates**: Automatic question refresh at midnight
- 📱 **Mobile Optimized**: Perfect rendering on all devices (16:9 and 20:9 aspect ratios)
- 🎨 **Dual Themes**: Matrix and Glass UI themes
- 📊 **Instant Results**: Comprehensive performance review
- 🔄 **Smart Navigation**: Keyboard shortcuts and pagination
- 💾 **Persistent Database**: New questions append without deleting old ones
- 🎯 **Quality Content**: High-quality questions for SSC, Bank, and RRB exams

## 📱 Mobile Optimization

The application is fully optimized for mobile devices:
- ✅ Responsive design for all screen sizes
- ✅ Perfect rendering on 16:9 aspect ratio devices
- ✅ Perfect rendering on 20:9 aspect ratio devices
- ✅ Touch-friendly interface
- ✅ No rendering issues or lags
- ✅ Smooth transitions and animations

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/anacondy/QuizApp.git
   cd QuizApp
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**
   ```bash
   python setup_database.py
   ```

4. **Configure API Key (Optional for AI features)**
   
   Create a `.env` file in the project root:
   ```bash
   GEMINI_API_KEY=your_api_key_here
   ```
   
   Get your free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the app**
   
   Open your browser and navigate to: `http://localhost:5000`

## 🤖 AI Question Generation

### Automatic Updates

The application can automatically generate new questions daily at midnight:

```bash
# Start the scheduler (runs in background)
python scheduler.py
```

### Manual Generation

Generate questions on demand:

```bash
# Generate questions immediately
python scheduler.py --now
```

Or use the question generator directly:

```bash
python question_generator.py
```

### How It Works

1. **API Integration**: Uses Google Gemini API for question generation
2. **Quality Control**: Validates and formats questions automatically
3. **Duplicate Prevention**: Checks for existing questions before adding
4. **Database Append**: New questions are added without deleting old ones
5. **Category Coverage**: Generates questions for all exam categories and sections

## 📦 Deployment Guides

### 🔷 GitHub Pages (Static Landing)

The repository includes a GitHub Pages deployment for the landing page:

1. **Enable GitHub Pages**:
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: main → /docs folder
   - Save

2. **Access your site**:
   `https://yourusername.github.io/QuizApp/`

**Note**: GitHub Pages hosts only the static landing page. For full functionality, deploy the Flask backend to a platform below.

### 🔶 Heroku

1. **Create a Heroku account** at [heroku.com](https://heroku.com)

2. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # Ubuntu
   curl https://cli-assets.heroku.com/install.sh | sh
   
   # Windows
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

3. **Create Procfile** (already included)
   ```
   web: gunicorn app:app
   ```

4. **Deploy to Heroku**
   ```bash
   # Login to Heroku
   heroku login
   
   # Create a new Heroku app
   heroku create your-quiz-app-name
   
   # Set environment variables (if using AI features)
   heroku config:set GEMINI_API_KEY=your_api_key_here
   
   # Deploy
   git push heroku main
   
   # Open your app
   heroku open
   ```

5. **Enable scheduled tasks** (for automatic question updates)
   ```bash
   # Add Heroku Scheduler add-on
   heroku addons:create scheduler:standard
   
   # Open scheduler dashboard
   heroku addons:open scheduler
   
   # Add daily job: python scheduler.py --now
   # Set to run daily at 00:00
   ```

### 🔷 PythonAnywhere

1. **Create account** at [pythonanywhere.com](https://www.pythonanywhere.com)

2. **Upload files**:
   - Use the Files tab to upload all project files
   - Or clone from GitHub:
     ```bash
     git clone https://github.com/anacondy/QuizApp.git
     ```

3. **Set up virtual environment**:
   ```bash
   cd QuizApp
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configure Web App**:
   - Go to Web tab → Add a new web app
   - Choose Manual configuration → Python 3.x
   - Set source code directory: `/home/yourusername/QuizApp`
   - Set working directory: `/home/yourusername/QuizApp`
   - Edit WSGI configuration file:
     ```python
     import sys
     path = '/home/yourusername/QuizApp'
     if path not in sys.path:
         sys.path.append(path)
     
     from app import app as application
     ```

5. **Set environment variables**:
   - In Web tab, scroll to environment variables
   - Add: `GEMINI_API_KEY` with your API key

6. **Set up scheduled tasks**:
   - Go to Tasks tab
   - Add: `cd /home/yourusername/QuizApp && /home/yourusername/QuizApp/venv/bin/python scheduler.py --now`
   - Set to run daily at 00:00

7. **Reload web app** and visit your URL

### 🔶 Render

1. **Create account** at [render.com](https://render.com)

2. **Create new Web Service**:
   - Connect your GitHub repository
   - Name: your-quiz-app
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt && python setup_database.py`
   - Start Command: `gunicorn app:app`

3. **Set environment variables**:
   - Add `GEMINI_API_KEY` in Environment Variables section

4. **Deploy**: Render will automatically deploy your app

5. **Set up Cron Job** (for scheduled tasks):
   - Create a new Cron Job in Render
   - Schedule: `0 0 * * *` (daily at midnight)
   - Command: `python scheduler.py --now`

### 🔷 Railway

1. **Create account** at [railway.app](https://railway.app)

2. **Deploy from GitHub**:
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your QuizApp repository
   - Railway will auto-detect Python and install dependencies

3. **Configure**:
   - Add environment variable: `GEMINI_API_KEY`
   - Ensure `Procfile` is present (already included)

4. **Set up scheduled tasks**:
   - Railway doesn't have built-in cron
   - Use external cron service or GitHub Actions

### 🔶 Google Cloud Platform (App Engine)

1. **Create app.yaml** (already included):
   ```yaml
   runtime: python39
   entrypoint: gunicorn -b :$PORT app:app
   
   env_variables:
     GEMINI_API_KEY: "your_api_key_here"
   ```

2. **Deploy**:
   ```bash
   # Install Google Cloud SDK
   # https://cloud.google.com/sdk/docs/install
   
   # Initialize
   gcloud init
   
   # Deploy
   gcloud app deploy
   ```

## 🧪 Testing

### Manual Testing

1. **Test the Flask app**:
   ```bash
   python app.py
   ```
   - Visit `http://localhost:5000`
   - Test category selection
   - Complete a quiz
   - Check results page

2. **Test database setup**:
   ```bash
   python setup_database.py
   ```
   - Verify `quiz.db` is created
   - Check question count

3. **Test question generator** (requires API key):
   ```bash
   python question_generator.py
   ```
   - Verify questions are generated
   - Check database for new entries

4. **Test scheduler**:
   ```bash
   python scheduler.py --now
   ```
   - Verify questions are added
   - Check console output for errors

### Automated Testing

Run the test suite (if tests are added):
```bash
pytest
```

### Mobile Testing

1. **Chrome DevTools**:
   - Press F12 → Toggle device toolbar
   - Test various device sizes:
     - iPhone 12 Pro (16:9)
     - Samsung Galaxy S20 (20:9)
     - iPad Pro
     - Generic mobile sizes

2. **Real Device Testing**:
   - Get local network IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
   - Run app: `python app.py --host=0.0.0.0`
   - Access from mobile: `http://YOUR_IP:5000`

3. **Responsive Breakpoints**:
   - Mobile: < 768px
   - Tablet: 768px - 1024px
   - Desktop: > 1024px

## 📁 Project Structure

```
QuizApp/
├── app.py                    # Main Flask application
├── questions.py              # Legacy question data
├── setup_database.py         # Database initialization
├── question_generator.py     # AI question generation
├── scheduler.py              # Automated task scheduler
├── requirements.txt          # Python dependencies
├── Procfile                  # Heroku deployment config
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules
├── quiz.db                   # SQLite database (auto-generated)
├── README.md                 # This file
├── docs/
│   └── index.html            # GitHub Pages landing page
├── templates/
│   ├── index.html            # Home page
│   ├── quiz.html             # Quiz interface
│   └── results.html          # Results page
├── static/
│   ├── css/
│   │   └── style.css         # Application styles
│   └── js/
│       └── script.js         # Client-side logic
└── .github/
    └── workflows/
        └── pages.yml         # GitHub Pages deployment
```

## 🎯 Exam Categories

### SSC (Staff Selection Commission)
- General Awareness
- Quantitative Aptitude
- English Comprehension
- General Intelligence & Reasoning

### BANK (Banking Sector)
- Reasoning Ability
- Quantitative Aptitude
- English Language
- General / Financial Awareness

### RRB (Railway Recruitment Board)
- Mathematics
- General Intelligence and Reasoning
- General Awareness

## 🔧 Configuration

### Environment Variables

Create a `.env` file:

```bash
# Required for AI question generation
GEMINI_API_KEY=your_google_gemini_api_key

# Optional configurations
FLASK_ENV=production
FLASK_DEBUG=0
PORT=5000
```

### Database Configuration

The app uses SQLite by default. To use PostgreSQL (recommended for production):

1. Install PostgreSQL adapter:
   ```bash
   pip install psycopg2-binary
   ```

2. Update `app.py` connection string:
   ```python
   DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///quiz.db')
   ```

## 🛠️ Development

### Adding New Questions Manually

Edit `setup_database.py` and add to `sample_questions`:

```python
('CATEGORY', 'Section Name', 'Question text?', 
 'Option A', 'Option B', 'Option C', 'Option D', 
 'Correct Answer'),
```

Then run:
```bash
python setup_database.py
```

### Customizing Themes

Edit `static/css/style.css`:

- Matrix theme: Modify `:root` variables
- Glass theme: Modify `.theme-glass` selectors

### Adding New Exam Categories

1. Update `question_generator.py`:
   ```python
   EXAM_CATEGORIES['NEW_EXAM'] = ['Section 1', 'Section 2']
   ```

2. Update `templates/index.html`:
   ```html
   <a href="/quiz?category=NEW_EXAM"><button>NEW EXAM</button></a>
   ```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini API for AI-powered question generation
- Flask framework for web application
- Government exam preparation community

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/anacondy/QuizApp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/anacondy/QuizApp/discussions)
- **Email**: Contact repository owner

## 🔄 Version History

- **v1.0.0** (2024-11-23)
  - Initial release
  - AI-powered question generation
  - Mobile optimization
  - Automated daily updates
  - Multi-platform deployment support

---

**Made with ❤️ for exam preparation**
