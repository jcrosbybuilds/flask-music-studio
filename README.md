# Flask Music Studio

A multi-page web application built with Python and Flask featuring dynamic routing, reusable Jinja2 templates, shared CSS styling, and server-rendered content.
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey)
![HTML](https://img.shields.io/badge/HTML5-Markup-orange)
![CSS](https://img.shields.io/badge/CSS3-Styling-blue)

## Screenshot

### Home
![Homepage](screenshots/homepage.png)

### About
![About](screenshots/about.png)

### Contact
![Contact](screenshots/contact.png)

## Technologies

- Python
- Flask
- HTML5
- CSS3
- Jinja2

## Features

- Multi-page website
- Shared layout using template inheritance
- Dynamic date and time
- Navigation bar
- External resource links
- Responsive project organization

## Project Structure

```text
flask-music-studio/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── screenshots/
│   ├── homepage.png
│   ├── about-page.png
│   └── contact-page.png
├── static/
│   └── style.css
└── templates/
    ├── about.html
    ├── base.html
    ├── contact.html
    └── home.html

## Future Improvements

- User authentication
- Contact form
- SQLite database
- Responsive design

## Installation

### Clone the Repository

```bash
git clone https://github.com/jcrosbybuilds/flask-music-studio.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

## What I learned

This project strengthened my understanding of:

- Developing web applications with Flask
- Using Jinja2 template inheritance to create reusable layouts
- Organizing HTML templates and static assets
- Passing dynamic data from Python to HTML templates
- Structuring a small Python web application
- Using Git and GitHub for version control and project documentation