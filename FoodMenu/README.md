# FoodMenu

FoodMenu is a Django-based web application that enables users to explore and manage recipes, update food items, and maintain personalized profiles. It is built with the latest Django technologies, including authentication, admin panel management, forms, models, and static file handling.

---

## Features

### User Features

- **User Registration and Login:** Secure user authentication with Django's built-in authentication system.
- **Automatic Profile Creation:** Profiles are automatically created for users during registration using Django signals.
- **Profile Management:** Users can view and manage their profiles, including profile pictures.
- **Menu Management:** Users can add, update, and view menu.

### Admin Features

- **Admin Panel:** Full control over the database through Django's admin interface.
- **User Management:** Admins can manage users and their profiles.
- **Food Items Management:** Admins can add, update, and delete food items.

---

## Technologies Used

- **Python:** For backend logic.
- **Django:** Core framework for building the application.
- **Bootstrap:** For responsive and modern frontend design.
- **SQLite:** Default database for development.
- **HTML/CSS:** For structuring and styling the web pages.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/foodmenu.git
   cd foodmenu
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install django pillow
   ```

4. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the server:

   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000`.

---

## Routes

- **Home:** `/` - The homepage of the application.
- **Register:** `/register/` - User registration page.
- **Login:** `/login/` - User login page.
- **Logout:** `/logout/` - Logout route.
- **Profile:** `/profile/` - User profile page.
- **Update Food Items:** `/food/update/` - List of food items to update.
- **Admin Panel:** `/admin/` - Admin dashboard.

---

## Implementation Details

### Automatic Profile Creation

Django signals are used to automatically create a user profile when a new user registers. This eliminates the need for manual profile creation.

**Code:**

```python
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
```

### Admin Panel

The admin panel allows for easy management of users, food items, and profiles. Simply log in with superuser credentials to access it.

### Static Files

Static files, including images and CSS, are stored and served using Django's static files system. Profile pictures are uploaded to the `pictures/profile_pictures/` directory.

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request.

---

Thank you for exploring FoodMenu. Enjoy discovering recipes and managing your culinary world effortlessly!

