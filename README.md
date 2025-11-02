# 🕐 WatchHouse - E-commerce Website

A modern e-commerce platform for luxury and lifestyle watches built with Django and configured to work with Supabase PostgreSQL database.

## Features

✅ **Watch Catalog** - Browse through a beautiful collection of watches  
✅ **Watch Details** - View detailed information about each watch  
✅ **Order System** - Simple order form with customer name and phone number  
✅ **Admin Panel** - Manage watches and view orders  
✅ **Responsive Design** - Modern, mobile-friendly interface  
✅ **Supabase Integration** - PostgreSQL database in the cloud  

## Project Structure

```
watchhouse/
├── watches/                    # Main app
│   ├── models.py              # Watch and Order models
│   ├── views.py               # Catalog, detail, and order views
│   ├── forms.py               # Order form
│   ├── admin.py               # Admin configuration
│   ├── templates/watches/     # HTML templates
│   └── migrations/            # Database migrations
├── watchhouse_project/        # Project settings
│   ├── settings.py            # Configuration
│   └── urls.py                # URL routing
├── manage.py                  # Django management script
├── populate_sample_data.py    # Script to add sample watches
├── requirements.txt           # Python dependencies
├── SUPABASE_SETUP.md         # Supabase configuration guide
└── .env.example              # Environment variables template
```

## Quick Start (Development with SQLite)

### 1. Install Dependencies

```bash
cd watchhouse
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt --break-system-packages
```

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Create Admin User

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 4. Add Sample Data

```bash
python populate_sample_data.py
```

This will add 8 sample watches to your database.

### 5. Run Development Server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

### 6. Access Admin Panel

Visit: http://127.0.0.1:8000/admin

Login with the superuser credentials you created.

## Setting Up Supabase (Production Database)

For detailed instructions on connecting to Supabase, see **SUPABASE_SETUP.md**

### Quick Summary:

1. Create a Supabase project at https://supabase.com
2. Get your database connection string
3. Create a `.env` file with your credentials
4. Install additional packages:
   ```bash
   pip install python-decouple dj-database-url --break-system-packages
   ```
5. Update `settings.py` to use environment variables
6. Run migrations: `python manage.py migrate`

## How It Works

### User Flow:

1. **Browse Catalog** → User sees all available watches
2. **Select Watch** → Click on a watch to see details
3. **Order** → Click "Order Now" button
4. **Fill Form** → Enter name and phone number
5. **Submit** → Order is saved to database

### Admin View:

1. Login to `/admin`
2. View all orders with customer information
3. Manage watch inventory
4. Update watch details and prices

## Models

### Watch Model
```python
- name: Watch name
- brand: Watch brand
- price: Price (decimal)
- description: Detailed description
- image_url: Optional image URL
- stock: Available quantity
- created_at: Creation timestamp
```

### Order Model
```python
- watch: Foreign key to Watch
- customer_name: Customer's full name
- customer_phone: Customer's phone number
- order_date: Order timestamp
- status: Order status (default: 'pending')
```

## Frontend Technology

The frontend uses:
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients and animations
- **Django Templates** - Dynamic content rendering
- **No JavaScript** - Pure HTML/CSS for simplicity

The design is:
- ✨ Modern and elegant
- 📱 Fully responsive
- 🎨 Purple gradient theme
- 🚀 Fast and lightweight

## Admin Features

From the Django admin panel, you can:

- ✏️ Add/Edit/Delete watches
- 📋 View all orders
- 🔍 Search orders by customer name, phone, or watch
- 📊 Filter orders by status and date
- 👥 Manage users and permissions

## Customization

### Change Colors
Edit the CSS in template files:
- `base.html` - Main theme colors
- `catalog.html` - Catalog styling
- `watch_detail.html` - Detail page styling
- `order_form.html` - Form styling

### Add More Fields
1. Update models in `watches/models.py`
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. Update forms and templates accordingly

### Add Images
- Set `image_url` field in Watch model
- Images will display automatically in catalog and detail pages

## Deployment Tips

### For Production:

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Use environment variables for sensitive data
4. Set up static files serving
5. Use a production-ready database (Supabase PostgreSQL)
6. Enable HTTPS
7. Set up proper CSRF protection

### Recommended Hosting:

- **Heroku** - Easy Django deployment
- **Railway** - Modern platform with great DX
- **DigitalOcean App Platform** - Scalable and reliable
- **Vercel** - With Postgres database
- **PythonAnywhere** - Beginner-friendly

## Tech Stack

- **Backend**: Django 5.2.7
- **Database**: SQLite (development) / PostgreSQL via Supabase (production)
- **Python**: 3.12+
- **ORM**: Django ORM
- **Admin**: Django Admin
- **Frontend**: Django Templates + CSS

## Troubleshooting

### Issue: Can't access admin panel
**Solution**: Make sure you created a superuser with `python manage.py createsuperuser`

### Issue: No watches showing
**Solution**: Run `python populate_sample_data.py` to add sample data

### Issue: Database errors
**Solution**: 
1. Delete `db.sqlite3` file
2. Delete `watches/migrations/000*.py` (keep `__init__.py`)
3. Run `python manage.py makemigrations`
4. Run `python manage.py migrate`

### Issue: Supabase connection fails
**Solution**: Check SUPABASE_SETUP.md and verify your connection string

## Contributing

This is a basic e-commerce template. Feel free to enhance it with:

- 🛒 Shopping cart functionality
- 💳 Payment integration (Stripe, PayPal)
- 📧 Email notifications
- 📱 SMS confirmations
- 🖼️ Image upload for watches
- ⭐ Reviews and ratings
- 🔐 User authentication
- 📦 Order tracking
- 💰 Multiple payment methods

## License

This project is open source and available for educational purposes.

## Support

For issues or questions:
1. Check SUPABASE_SETUP.md for database configuration
2. Review Django documentation: https://docs.djangoproject.com
3. Check Supabase docs: https://supabase.com/docs

---

Built with ❤️ using Django and Supabase
