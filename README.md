# 🛍️ Shop E-Commerce API

A complete Django REST Framework backend for e-commerce product management with full CRUD operations, authentication, and admin capabilities.

## 🚀 Quick Start Guide

### 📥 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/Ahmed194724496/shop.git
cd shop

# 2. Install required packages
pip install -r requirements.txt

# 3. Setup database
python manage.py migrate

# 4. Create admin account (follow the prompts)
python manage.py createsuperuser

# 5. Start the development server
python manage.py runserver
```

### 🛠️ If You Encounter Issues

**Port 8000 is busy:**
```bash
# Stop any running Django server
pkill -f runserver

# Start on a different port
python manage.py runserver 8080
```

**Database problems:**
```bash
python manage.py migrate
```

**Missing packages:**
```bash
pip install -r requirements.txt
```

## 🌐 Access Points

After starting the server, visit these URLs in your browser:

- **🏠 Home Page** - http://127.0.0.1:8000/
  - *Automatically redirects to products page*

- **📦 Products API** - http://127.0.0.1:8000/products/products/
  - *View all products with search and filters*
  - *Test API endpoints directly*

- **📁 Categories API** - http://127.0.0.1:8000/products/categories/
  - *Browse product categories*
  - *See category-based organization*

- **⚙️ Admin Panel** - http://127.0.0.1:8000/admin/
  - *Full admin dashboard*
  - *Manage products, categories, and users*
  - *Requires superuser login*

## ✨ Key Features

### 🔍 Product Management
- **Complete CRUD operations** - Create, Read, Update, Delete products
- **Advanced search** - Find products by name and description
- **Smart filtering** - Filter by category, price range, stock status
- **Pagination** - Handle large product lists efficiently

### 👨‍💼 Admin Capabilities
- **Full admin interface** - Manage all data through Django admin
- **User management** - Control user accounts and permissions
- **Database administration** - Direct access to all models

### 🔐 Security & Authentication
- **JWT ready** - Token-based authentication system implemented
- **Secure endpoints** - Protected API routes
- **Admin authorization** - Role-based access control

## 🛠️ Technology Stack

- **Backend Framework:** Django 5.1.3
- **API Framework:** Django REST Framework 3.15.1
- **Authentication:** JWT (Simple JWT)
- **Database:** SQLite (Development)
- **Filtering:** Django Filter
- **API Documentation:** Built-in DRF interface

## 📁 Project Structure

```
shop/
├── 📂 api/                 # API configuration & authentication
├── 📂 products/            # Product & category management
├── 📂 shop/                # Project settings & configuration
├── 📂 users/               # Custom user model & authentication
├── 📄 manage.py            # Django management script
├── 📄 requirements.txt     # Project dependencies
├── 📄 db.sqlite3           # Database file
└── 📄 README.md           # Project documentation
```

## 🎯 API Testing Guide

### For Reviewers:
1. **Start with Products API** - Test the main functionality
2. **Try search & filters** - Use the built-in DRF interface
3. **Check admin panel** - Verify full management capabilities
4. **Test categories** - Explore category-based organization

### Sample Testing:
- Search for products using the search box
- Filter by different categories
- Test pagination with large result sets
- Verify admin CRUD operations

## 📞 Support & Contact

**Developer:** Ahmed Zidan  
**Email:** az7923140@gmail.com  
**GitHub:** [Ahmed194724496](https://github.com/Ahmed194724496)  
**Repository:** https://github.com/Ahmed194724496/shop
