# E-Commerce Project

This project is an e-commerce application built with Django. It includes features such as product listing, user authentication, shopping cart, payment integration with Razorpay, and automatic email notifications to registered users.

## Features

- User Registration and Authentication
- Product Listing and Search
- Shopping Cart
- Order Management
- Payment Integration with Razorpay
- Automatic Email Notifications to Registered Users

## Deployment

The project is deployed on Railway. You can access it at [https://e-commerce-production-bdbc.up.railway.app/](https://e-commerce-production-bdbc.up.railway.app/).
## Prerequisites

- Python 3.x
- Django
- `python-dotenv` package

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/munna710/e-commerce.git
    cd e-commerce
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the root directory and add your environment variables:**

    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DATABASE_URL=your_database_url
    RAZORPAY_KEY_ID=your_razorpay_key_id
    RAZORPAY_KEY_SECRET=your_razorpay_key_secret
    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    EMAIL_HOST=smtp.your-email-provider.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=your-email@example.com
    EMAIL_HOST_PASSWORD=your-email-password
    ```

5. **Update your `settings.py` to load environment variables:**

    ```python
    import os
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()

    # Get environment variables
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('DEBUG') == 'True'
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')
    DATABASE_URL = os.getenv('DATABASE_URL')
    RAZORPAY_KEY_ID = os.getenv('RAZORPAY_KEY_ID')
    RAZORPAY_KEY_SECRET = os.getenv('RAZORPAY_KEY_SECRET')

    # Email settings
    EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_PORT = int(os.getenv('EMAIL_PORT'))
    EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == 'True'
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    ```

6. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

7. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

8. **Run the Django development server:**

    ```sh
    python manage.py runserver
    ```

## Usage

1. Navigate to the home page in your browser.
2. Register or log in to your account.
3. Browse products and add them to your cart.
4. Proceed to checkout and complete the payment using Razorpay.
5. Registered users will receive an email notification upon successful registration and order placement.


