# GitHub Pages Setup Instructions

## Quick Setup Guide

Follow these simple steps to enable GitHub Pages for your QuizApp:

### Step 1: Access Repository Settings

1. Go to your repository on GitHub: `https://github.com/anacondy/QuizApp`
2. Click on **Settings** (top right, next to About)

### Step 2: Navigate to Pages

1. In the left sidebar, scroll down to find **Pages**
2. Click on **Pages**

### Step 3: Configure Source

1. Under "Source", click the dropdown
2. Select **Deploy from a branch**

### Step 4: Select Branch and Folder

1. Under "Branch":
   - Select **main** from the first dropdown
   - Select **/docs** from the second dropdown
2. Click **Save**

### Step 5: Wait for Deployment

1. GitHub will start building your site
2. Wait 1-2 minutes for the deployment to complete
3. Refresh the page to see the deployment status

### Step 6: Access Your Site

Once deployed, your site will be available at:
```
https://anacondy.github.io/QuizApp/
```

You'll see a green checkmark and this URL at the top of the Pages settings.

---

## Verification

To verify your site is live:

1. Click the URL shown in Pages settings
2. You should see a beautiful landing page with:
   - QuizApp title
   - Exam category descriptions (SSC, BANK, RRB)
   - Features list
   - Link to GitHub repository

---

## Troubleshooting

### "404 - Page Not Found"

**Solution:**
- Wait a few more minutes (initial deployment can take up to 5 minutes)
- Ensure you selected `/docs` folder, not root `/`
- Check that the docs/index.html file exists in your main branch

### "Build Failed"

**Solution:**
- Check the Actions tab for error details
- Ensure `.github/workflows/pages.yml` exists
- Make sure Pages is enabled in repository settings

### Custom Domain

If you want to use a custom domain:

1. Add your domain in the "Custom domain" field
2. Follow GitHub's DNS configuration instructions
3. Enable "Enforce HTTPS" after DNS propagates

---

## What Gets Published?

Only the files in the `/docs` folder are published to GitHub Pages:
- `docs/index.html` - Static landing page

The full Flask application needs to be deployed separately to:
- Heroku
- PythonAnywhere
- Render
- Railway
- Google Cloud Platform

See README.md for deployment guides to these platforms.

---

## Updating Your Site

Any changes pushed to `main` branch in the `/docs` folder will automatically update your GitHub Pages site.

The GitHub Actions workflow (`.github/workflows/pages.yml`) handles this automatically.

---

## Next Steps

After enabling GitHub Pages:

1. ✅ Share the link: `https://anacondy.github.io/QuizApp/`
2. ✅ Add it to your repository description
3. ✅ Add it to your README (already done!)
4. ✅ Deploy the full Flask app to a platform for dynamic features

---

**Questions?** Check the [Troubleshooting Guide](wiki/Troubleshooting.md) or [FAQ](wiki/FAQ.md)
