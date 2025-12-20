# Django TweetApp

A Django-based social media application similar to Twitter, where users can create, edit, delete, and search tweets with photo uploads.

## 🚀 Features

- 🔐 **User Authentication**: Register and login system with Django's built-in authentication
- 📝 **Tweet Management**: Create, edit, and delete tweets (up to 240 characters)
- 📸 **Photo Uploads**: Add images to your tweets
- 🔍 **Advanced Search**: Search tweets by content or username with real-time filtering
- 👤 **User Profiles**: Each tweet is associated with a user
- 🎨 **Modern UI**: Bootstrap 5 dark theme interface with responsive design
- 🔒 **Authorization**: Users can only edit/delete their own tweets
- ⚙️ **Admin Panel**: Easy access to Django admin for content management

## 🛠️ Technologies Used

- **Backend**: Django 6.0
- **Database**: SQLite (default)
- **Image Processing**: Pillow 12.0.0
- **Frontend**: Bootstrap 5.3.8
- **Python**: 3.x

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sg-2003/Django-Tweet-App.git
   cd Django-Tweet-App/chaiwala
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r ../requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   
   The server will start on `http://127.0.0.1:8000/`

8. **Access the application**
   - Main Application: `http://127.0.0.1:8000/tweet/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`
   - User Registration: `http://127.0.0.1:8000/accounts/register/`
   - User Login: `http://127.0.0.1:8000/accounts/login/`

## 📖 Usage

### Navigation

The application includes a clean navigation bar with the following options:
- **TweetApp** (brand logo) - Links to admin panel
- **Admin** - Direct link to Django admin panel
- **Search Bar** - Search tweets by content or username
- **Tweet Home** - Navigate to the main tweets page
- **Register/Login** - User authentication (when not logged in)
- **Logout** - Sign out (when logged in)

### Creating an Account

1. Click on the **Register** button in the navbar
2. Fill in your username, email, and password
3. You'll be automatically logged in after registration

### Creating a Tweet

1. Log in to your account
2. Navigate to the Tweet Home page
3. Click on **"Add Tweets Here:"** button
4. Enter your tweet text (max 240 characters)
5. Optionally upload a photo
6. Click **Submit** to post your tweet

### Editing/Deleting Tweets

- Only your own tweets will show **Edit** and **Delete** buttons
- Click **Edit** to modify your tweet
- Click **Delete** to remove your tweet (confirmation required)

### Searching Tweets

- Use the search bar in the navbar
- Type your search query and press Enter or click **Search**
- Search by tweet content or username (case-insensitive)
- A search results banner will appear showing your query
- Click **Clear Search** to view all tweets again

### Admin Panel Access

- Click the **Admin** button in the navbar or the **TweetApp** brand logo
- You must be logged in as a superuser to access the admin panel
- Create a superuser using: `python manage.py createsuperuser`

## 📁 Project Structure

```
Django-Tweet-App/
├── chaiwala/              # Main Django project
│   ├── chaiwala/          # Project settings
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── tweet/             # Tweet application
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   ├── tweet_list.html
│   │   │   ├── tweet_form.html
│   │   │   └── tweet_confirm_delete.html
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   └── urls.py
│   ├── templates/        # Base templates
│   │   ├── layout.html
│   │   └── registration/
│   │       ├── login.html
│   │       ├── logout.html
│   │       └── register.html
│   ├── media/            # User uploaded files
│   │   └── photos/
│   ├── static/           # Static files
│   ├── db.sqlite3        # SQLite database
│   └── manage.py
├── requirements.txt      # Python dependencies
└── README.md
```

## 🗄️ Models

### Tweet Model
- `user`: ForeignKey to User (who created the tweet)
- `text`: TextField (max 240 characters)
- `photo`: ImageField (optional)
- `created_at`: DateTimeField (auto-generated)
- `updated_at`: DateTimeField (auto-updated)

## 🔗 URLs

- `/tweet/` - List all tweets (home page)
- `/tweet/create` - Create a new tweet (login required)
- `/tweet/<id>/edit/` - Edit a tweet (login required, owner only)
- `/tweet/<id>/delete/` - Delete a tweet (login required, owner only)
- `/accounts/register/` - User registration
- `/accounts/login/` - User login
- `/accounts/logout/` - User logout
- `/admin/` - Django admin panel

## 🎨 UI Components

### Navigation Bar
The navbar includes:
- **Brand Logo (TweetApp)**: Links to admin panel
- **Admin Link**: Quick access to Django admin
- **Search Bar**: Real-time tweet search functionality
- **Tweet Home Button**: Navigate to main tweets feed
- **Authentication Buttons**: Register/Login (when logged out) or Logout (when logged in)

### Pages
- **Tweet List**: Displays all tweets in a card-based layout
- **Tweet Form**: Create or edit tweets with photo upload
- **Search Results**: Filtered view of tweets matching search criteria
- **User Registration**: Account creation form
- **User Login**: Authentication form

## 💻 Development

### Starting the Server
```bash
cd chaiwala
python manage.py runserver
```

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
```

### Applying Migrations
```bash
python manage.py migrate
```

### Creating a Superuser (for admin access)
```bash
python manage.py createsuperuser
```

### Collecting Static Files (for production)
```bash
python manage.py collectstatic
```

## 🔒 Security Notes

⚠️ **Important**: This project is configured for development only. Before deploying to production:

1. Change `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS`
4. Use a production database (PostgreSQL, MySQL, etc.)
5. Set up proper static file serving
6. Configure HTTPS
7. Review Django security checklist: https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Sg-2003**
- GitHub: [@Sg-2003](https://github.com/Sg-2003)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap for the UI framework
- Pillow for image processing

---

**Note**: This is a development project. For production use, please follow Django's deployment guidelines and security best practices.

