# Frequently Asked Questions (FAQ)

## General Questions

### What is QuizApp?

QuizApp is a free, open-source web application designed to help students prepare for Indian government competitive exams including SSC, Bank, and RRB.

### Is QuizApp really free?

Yes! QuizApp is completely free and open-source under the MIT License. You can use, modify, and distribute it freely.

### Do I need to create an account?

No. QuizApp doesn't require any registration or login. Just visit the site and start practicing.

### Can I use it offline?

After the first load, basic functionality works offline. However, new question generation requires an internet connection.

### Which exams does QuizApp support?

Currently:
- **SSC** (Staff Selection Commission)
- **BANK** (Banking Sector Exams)
- **RRB** (Railway Recruitment Board)

## Questions About Questions

### How many questions are in each quiz?

Each quiz contains 10 randomly selected questions from the chosen category.

### How often are new questions added?

With AI integration enabled, new questions are automatically generated and added daily at midnight.

### Can I suggest questions?

Yes! You can:
1. Fork the repository
2. Add questions to `setup_database.py`
3. Submit a pull request

### Are the questions updated for current syllabus?

The AI generates questions based on current exam patterns. Manual questions are reviewed periodically.

### What happens to old questions?

Old questions are never deleted. New questions are appended to the database, building a comprehensive question bank over time.

## Technical Questions

### What technologies does QuizApp use?

- **Backend**: Python, Flask, SQLite
- **Frontend**: HTML, CSS, JavaScript
- **AI**: Google Gemini API
- **Deployment**: GitHub Pages, Heroku, PythonAnywhere, etc.

### Can I run it on my own server?

Yes! See the [Deployment Guide](Deployment-Guide.md) for various hosting options.

### Does it work on mobile?

Absolutely! QuizApp is fully optimized for mobile devices with responsive design.

### What browsers are supported?

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- All modern mobile browsers

### Do I need a powerful computer?

No. QuizApp runs smoothly on any device with a web browser.

## AI and API Questions

### Do I need a Gemini API key?

Only if you want automated question generation. The app works fine with existing questions without an API key.

### How do I get a Gemini API key?

Visit [Google AI Studio](https://makersuite.google.com/app/apikey) and create a free API key.

### Is the API key free?

Yes, Google offers a free tier for Gemini API with generous quotas.

### What if I exceed API quota?

The app continues to work with existing questions. New question generation will resume when quota resets.

### Can I use a different AI?

Yes! The `question_generator.py` file can be modified to use any AI service (OpenAI, Anthropic, etc.).

## Features Questions

### Can I track my progress over time?

Currently, progress isn't saved between sessions. This feature may be added in future versions.

### Can I retake quizzes?

Yes! You can take as many quizzes as you want. Questions are randomly selected each time.

### How is scoring calculated?

Score = (Correct Answers / Total Questions) × 100

### Can I see detailed explanations?

Currently, you see the correct answer after completing the quiz. Detailed explanations may be added in future updates.

### Can I choose specific topics?

Questions are randomly selected from all sections within a category. Topic selection may be added later.

## Mobile App Questions

### Is there a mobile app?

Not currently. However, the web app is fully mobile-optimized and can be added to your home screen.

### How do I add QuizApp to my home screen?

**Android (Chrome):**
1. Open QuizApp in Chrome
2. Tap menu (⋮)
3. Select "Add to Home screen"

**iOS (Safari):**
1. Open QuizApp in Safari
2. Tap Share button
3. Select "Add to Home Screen"

### Does it work on tablets?

Yes! QuizApp adapts to any screen size, including tablets.

## Data and Privacy

### Is my data stored?

Only quiz theme preference is stored locally in your browser. No personal data is collected.

### Do you track users?

No. QuizApp doesn't use analytics or tracking.

### Can I delete my data?

Clear your browser's localStorage and sessionStorage to remove all locally stored data.

### Is it GDPR compliant?

Yes, since no personal data is collected or transmitted.

## Deployment Questions

### Can I deploy my own instance?

Yes! Follow the [Deployment Guide](Deployment-Guide.md) for step-by-step instructions.

### Which hosting platform is best?

Depends on your needs:
- **Heroku**: Easy deployment, good free tier
- **PythonAnywhere**: Beginner-friendly, simple setup
- **Render**: Modern platform, automatic deployments
- **GitHub Pages**: Free hosting for static site

### How much does hosting cost?

- **GitHub Pages**: Free
- **Heroku**: Free tier available
- **PythonAnywhere**: Free tier available
- **Render**: Free tier available

### Can I use a custom domain?

Yes! Most platforms support custom domains. Check their documentation.

## Development Questions

### Can I contribute?

Yes! Contributions are welcome. See the [Developer Guide](Developer-Guide.md) for guidelines.

### How do I report bugs?

Create an issue on [GitHub Issues](https://github.com/anacondy/QuizApp/issues).

### Can I fork the project?

Absolutely! Fork it and customize as you like. Just maintain the MIT License attribution.

### How do I add new exam categories?

1. Update `question_generator.py` with new category
2. Add questions to database
3. Update UI in `templates/index.html`

### Can I modify the design?

Yes! Edit `static/css/style.css` to customize the appearance.

## Troubleshooting

### The quiz won't start. What should I do?

1. Check browser console for errors (F12)
2. Verify database has questions
3. Clear browser cache
4. See [Troubleshooting Guide](Troubleshooting.md)

### Questions aren't loading.

1. Check internet connection
2. Verify database exists
3. Restart the server
4. Check API endpoint in browser console

### The theme won't change.

1. Enable localStorage in browser
2. Clear browser cache
3. Don't use private browsing
4. Try different browser

### I'm getting API errors.

1. Check API key is correct
2. Verify `.env` file exists
3. Check internet connection
4. Review API quota

For more solutions, see the [Troubleshooting Guide](Troubleshooting.md).

## Performance Questions

### Why is the app slow?

Possible causes:
- Slow internet connection
- Large database
- Browser extensions interfering
- Too many open tabs

### How can I improve performance?

1. Close unnecessary browser tabs
2. Disable browser extensions
3. Clear browser cache
4. Use latest browser version

### Does it use a lot of data?

No. After initial load, data usage is minimal. Questions are fetched only once per quiz.

## Future Features

### Will there be more exam categories?

Yes! We plan to add more categories based on user demand.

### Will you add user accounts?

This is under consideration for future versions.

### Can we have a leaderboard?

Potentially in future updates. Currently focusing on core functionality.

### Will there be a dark mode?

The Matrix theme is already dark! But we may add more theme options.

### Can you add timed quizzes?

This feature is planned for a future release.

## Getting Help

### Where can I get support?

1. Check this FAQ
2. Read [Troubleshooting Guide](Troubleshooting.md)
3. Search [GitHub Issues](https://github.com/anacondy/QuizApp/issues)
4. Ask in [GitHub Discussions](https://github.com/anacondy/QuizApp/discussions)

### How do I contact the developers?

- GitHub Issues for bugs
- GitHub Discussions for questions
- Email the repository owner

### Is there a community?

Join discussions on GitHub to connect with other users and contributors.

## License and Usage

### Can I use this for commercial purposes?

Yes, under the MIT License terms. You can use it commercially.

### Do I need to credit QuizApp?

Attribution is appreciated but not required under MIT License.

### Can I sell this?

You can, but you must include the original MIT License. However, we encourage keeping it free!

### Can I modify the code?

Yes! Modify, distribute, and use as you wish under MIT License.

---

**Still have questions?**

Ask in [GitHub Discussions](https://github.com/anacondy/QuizApp/discussions) or check the other wiki pages:

- [Getting Started](Getting-Started.md)
- [User Guide](User-Guide.md)
- [Developer Guide](Developer-Guide.md)
- [Deployment Guide](Deployment-Guide.md)
- [Troubleshooting](Troubleshooting.md)
