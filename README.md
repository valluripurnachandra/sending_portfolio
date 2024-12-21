# Personal Portfolio Website

A modern, responsive portfolio website built with Flask, featuring a dark mode toggle, contact form with email integration, and smooth animations.

## Features

- Responsive design using CSS Grid and Flexbox
- Dark mode toggle with local storage persistence
- Smooth scrolling navigation
- Contact form with email integration
- Modern animations and transitions
- Cross-browser compatible
- Mobile-first approach

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd portfolio
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix or MacOS:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the application:
```bash
python app.py
```

The website will be available at `http://localhost:5000`

## Project Structure

```
portfolio/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css  # Main stylesheet
│   └── js/
│       └── main.js    # JavaScript functionality
├── templates/
│   └── index.html     # Main HTML template
└── README.md          # Project documentation
```

## Customization

1. Update the content in `templates/index.html` with your personal information
2. Modify the styles in `static/css/style.css` to match your preferred color scheme
3. Add your projects to the portfolio section
4. Update social media links in the footer

## Deployment Instructions

### Local Development
1. Clone the repository:
```bash
git clone <repository-url>
cd portfolio
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix or MacOS:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

### Deployment Options

#### 1. Deploy to Heroku
1. Create a Heroku account at https://signup.heroku.com/
2. Install Heroku CLI
3. Login to Heroku:
```bash
heroku login
```
4. Create a new Heroku app:
```bash
heroku create your-app-name
```
5. Create Procfile:
```
web: gunicorn app:app
```
6. Add gunicorn to requirements.txt:
```bash
echo "gunicorn==20.1.0" >> requirements.txt
```
7. Deploy to Heroku:
```bash
git push heroku main
```

#### 2. Deploy to PythonAnywhere
1. Sign up for a PythonAnywhere account at https://www.pythonanywhere.com/
2. Upload your code:
   - Use Git: `git clone <your-repository-url>`
   - Or upload files via the Files tab
3. Create a virtual environment:
```bash
mkvirtualenv --python=/usr/bin/python3.8 myenv
```
4. Install requirements:
```bash
pip install -r requirements.txt
```
5. Configure the web app:
   - Go to the Web tab
   - Add a new web app
   - Choose Manual Configuration
   - Set the virtual environment path
   - Update WSGI file with Flask app configuration
   - Reload the web app

#### 3. Deploy to DigitalOcean App Platform
1. Create a DigitalOcean account
2. Install doctl and authenticate
3. Create app:
```bash
doctl apps create --spec app.yaml
```
4. Configure app.yaml:
```yaml
name: portfolio
services:
- name: web
  github:
    repo: your-username/portfolio
    branch: main
  build_command: pip install -r requirements.txt
  run_command: gunicorn app:app
  environment_slug: python
  instance_size_slug: basic-xxs
```
5. Deploy:
```bash
doctl apps create --spec app.yaml
```

### Important Deployment Notes

1. Environment Variables
- Create a `.env` file for local development
- Set environment variables in your deployment platform:
  ```
  FLASK_APP=app.py
  FLASK_ENV=production
  MAIL_USERNAME=your-email@gmail.com
  MAIL_PASSWORD=your-app-password
  ```

2. Media Files
- Create a `static/media` directory
- Add your profile picture as `profile.jpg`
- Add your resume as `resume.pdf`
- Add background video as `background.mp4`

3. Security
- Enable HTTPS
- Set up CORS if needed
- Configure CSP headers
- Use environment variables for sensitive data

4. Performance
- Compress static assets
- Enable caching
- Optimize images and videos
- Use a CDN for static files

5. Monitoring
- Set up error logging
- Configure performance monitoring
- Enable security alerts

## Security Note

Make sure to store sensitive information (like email credentials) in environment variables in production.
