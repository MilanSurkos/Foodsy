# Foodsy - Food Ordering System
Foodsy is a Django-based web application for managing and ordering food online. 
It provides a complete solution for restaurants and food businesses to showcase their menu, 
handle orders, and manage customer interactions.
## Features
- *Product Management*: Categorize and manage food and drink items
- *User Authentication*: Secure user registration and login system
- *Shopping Basket*: Add/remove items to/from the basket
- *Order Processing*: Track and manage customer orders
- *Admin Dashboard*: Comprehensive admin interface for managing the system
- *Responsive Design*: Works on both desktop and mobile devices
## Tech Stack
- *Backend*: Django 5.2.1
- *Frontend*: HTML, CSS, JavaScript, Bootstrap
- *Database*: SQLite (default), can be configured for PostgreSQL/MySQL
- *Additional Packages*:
  - django-crispy-forms for better form rendering
  - Pillow for image processing
  - django-extensions for development utilities
## Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)
## Installation
1. *Clone the repository*
bash
   git clone <https://github.com/MilanSurkos/Foodsy>
   cd Foodsy
   
2. *Set up a virtual environment (recommended)*
bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
3. *Install dependencies*
bash
   pip install -r requirements.txt
   
4. *Run migrations*
bash
   python manage.py migrate
   
5. *Create a superuser*
bash
   python manage.py createsuperuser
   
6. *Run the development server*
bash
   python manage.py runserver
   
7. *Access the application*
   - Frontend: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/
## Project Structure
Foodsy/
├── basket/           # Shopping basket functionality
├── discounts/        # Discount and promotion system
├── foodsy/           # Main project configuration
├── media/            # User-uploaded files
├── orders/           # Order processing
├── products/         # Product management
├── recipes/          # Recipe management
├── static/           # Static files (CSS, JS, images)
├── templates/        # HTML templates
├── users/            # User authentication and profiles
└── viewer/           # (Additional functionality)
## Configuration
1. *Environment Variables*
   Create a .env file in the project root with the following variables:
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   
## Contributing
1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
## Support
For support, please open an issue in the repository or contact the development team.