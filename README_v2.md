# 🕐 WatchHouse - Premium Watch E-commerce Platform

A stunning, modern e-commerce website for luxury watches built with Django, featuring a beautiful dark theme and multiple image support with carousel functionality.

## ✨ New Features (v2.0)

### 🖼️ Image Management
- **Multiple Images per Watch** - Upload 1-5 images for each watch
- **Image Carousel** - Beautiful image slider with navigation arrows
- **Admin Upload** - Upload images directly through Django admin panel
- **Automatic Placeholders** - Generated placeholders for watches without images

### 🎨 Beautiful Dark Theme
- **Modern UI** - Sleek dark theme inspired by premium watch marketplaces
- **Smooth Animations** - Hover effects, transitions, and micro-interactions
- **Responsive Design** - Looks amazing on desktop, tablet, and mobile
- **Card-Based Layout** - Clean, organized presentation

### 📱 Improved Layout
- **New Catalog Design** - Grid layout with badges (Featured/Popular)
- **Enhanced Detail Page** - Image carousel on left, info on right, description below
- **Better Order Flow** - Streamlined checkout experience

## 🚀 Quick Start

### 1. Extract and Setup

```bash
# Extract the project
tar -xzf watchhouse.tar.gz
cd watchhouse

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Create Admin User

```bash
python manage.py createsuperuser
```

### 4. Add Sample Data

```bash
# Add sample watches
python populate_sample_data.py

# Add placeholder images (optional - for demo)
python add_placeholder_images.py
```

### 5. Run Server

```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**

## 📸 Managing Watch Images

### Through Admin Panel

1. Go to http://127.0.0.1:8000/admin
2. Click on "Watches"
3. Select a watch or create new one
4. Scroll down to "Watch images" section
5. Click "Add another Watch Image"
6. Upload image and set order (0 = primary image)
7. Add up to 5 images per watch
8. Save

### Image Guidelines

- **Format**: JPG, PNG, WEBP
- **Recommended Size**: 800x800 to 1200x1200 pixels
- **Aspect Ratio**: Square (1:1) works best
- **File Size**: Under 2MB per image
- **Quality**: High resolution for detail

## 🎨 Design Features

### Dark Theme
- Background: Deep navy (#0a0e1a)
- Cards: Dark blue (#141824)
- Accent: Blue (#3b82f6)
- Success: Green (#4ade80)
- Borders: Subtle gray (#1e2432)

### UI Components
- **Watch Cards** - Hoverable cards with image, info, and CTA
- **Image Carousel** - Smooth sliding with navigation arrows
- **Badges** - Featured and Popular indicators
- **Stock Status** - Live stock indicators with pulsing dot
- **Responsive Grid** - Adapts to any screen size

### Animations
- Card hover elevations
- Image zoom on hover
- Smooth carousel transitions
- Button micro-interactions
- Slide-in messages

## 📊 Database Models

### Watch Model
```python
- name: Watch name (CharField)
- brand: Brand name (CharField)
- price: Price (DecimalField)
- description: Detailed description (TextField)
- stock: Available quantity (IntegerField)
- created_at: Creation timestamp (DateTimeField)
```

### WatchImage Model (New!)
```python
- watch: Foreign key to Watch (ForeignKey)
- image: Image file (ImageField)
- order: Display order, 0 = primary (IntegerField)
- uploaded_at: Upload timestamp (DateTimeField)
```

### Order Model
```python
- watch: Foreign key to Watch (ForeignKey)
- customer_name: Customer name (CharField)
- customer_phone: Customer phone (CharField)
- order_date: Order timestamp (DateTimeField)
- status: Order status (CharField)
```

## 🛠️ New File Structure

```
watchhouse/
├── media/                     ← NEW! User uploaded images
│   └── watch_images/
├── watches/
│   ├── models.py             ← Updated with WatchImage model
│   ├── admin.py              ← Inline image management
│   ├── templates/watches/
│   │   ├── base.html         ← Dark theme
│   │   ├── catalog.html      ← New design with badges
│   │   ├── watch_detail.html ← Carousel + new layout
│   │   └── order_form.html   ← Dark theme form
├── add_placeholder_images.py ← NEW! Generate placeholder images
└── requirements.txt          ← Updated with Pillow
```

## 🎯 Key Pages

### Catalog Page (/)
- Grid of watch cards
- Featured/Popular badges
- Heart icon for favorites (visual)
- Hover effects and animations
- Stock indicators

### Watch Detail Page (/watch/{id}/)
- **Left**: Image carousel with navigation
- **Right**: Brand, name, price, stock, order button
- **Bottom**: Full description
- Auto-playing carousel (5s interval)

### Order Form (/watch/{id}/order/)
- Order summary at top
- Simple 2-field form (name + phone)
- Validation and error handling
- Dark themed inputs

### Admin Panel (/admin/)
- Inline image upload
- Drag to reorder images
- View image count
- Full watch management

## 💡 Usage Tips

### Adding Real Watch Images

1. Take or find high-quality watch photos
2. Edit to square aspect ratio (1:1)
3. Optimize file size (under 2MB)
4. Upload through admin panel
5. Set image order (0, 1, 2, etc.)
6. Primary image (order=0) shows in catalog

### Customizing the Theme

All styles are in template files:
- `base.html` - Main colors and layout
- `catalog.html` - Catalog-specific styles
- `watch_detail.html` - Detail page styles
- `order_form.html` - Form styles

Change colors by editing the CSS variables in each template.

### Managing Stock

1. Go to admin panel
2. Edit watch
3. Update "Stock" field
4. Save
5. Out of stock watches show red indicator

## 🌐 Supabase Integration

The project supports Supabase PostgreSQL:

1. Create Supabase project
2. Get connection string
3. Create `.env` file:
   ```env
   DATABASE_URL=your_supabase_connection_string
   ```
4. Update `settings.py` to use environment variables
5. Run migrations
6. Deploy!

See `SUPABASE_SETUP.md` for detailed instructions.

## 📱 Responsive Breakpoints

- **Desktop**: 1200px+ (4 columns)
- **Laptop**: 968px-1199px (3 columns)
- **Tablet**: 768px-967px (2 columns)
- **Mobile**: <768px (1-2 columns)

## 🔒 Security Notes

For production:
- Set `DEBUG = False`
- Use environment variables for secrets
- Configure `ALLOWED_HOSTS`
- Enable HTTPS
- Use strong `SECRET_KEY`
- Set up proper media file serving
- Configure CORS if needed

## 📦 Dependencies

- **Django 5.2.7** - Web framework
- **Pillow 12.0.0** - Image processing
- **psycopg2-binary** - PostgreSQL adapter
- **supabase** - Supabase client
- **python-decouple** - Environment variables
- **dj-database-url** - Database URL parsing

## 🎨 Color Palette

```css
Background: #0a0e1a
Card Background: #141824
Border: #1e2432
Primary Blue: #3b82f6
Success Green: #4ade80
Text Primary: #e4e4e7
Text Secondary: #94a3b8
```

## 🚀 Deployment

Recommended platforms:
- **Railway** - Easy Django deployment
- **Heroku** - Popular PaaS
- **DigitalOcean** - VPS option
- **Vercel** - With PostgreSQL
- **PythonAnywhere** - Beginner-friendly

## 📝 Changelog

### Version 2.0 (Current)
- ✅ Multiple image support with carousel
- ✅ Beautiful dark theme
- ✅ Improved watch detail layout
- ✅ Enhanced catalog design
- ✅ Admin inline image upload
- ✅ Placeholder image generator
- ✅ Better responsive design

### Version 1.0
- Basic catalog and detail pages
- Single image per watch (URL)
- Purple gradient theme
- Simple order form
- SQLite database

## 🆘 Troubleshooting

**Images not showing?**
- Check `MEDIA_URL` and `MEDIA_ROOT` in settings.py
- Ensure `DEBUG = True` in development
- Verify images uploaded correctly in admin

**Carousel not working?**
- Check browser console for JavaScript errors
- Ensure multiple images uploaded for watch
- Clear browser cache

**Migration errors?**
- Delete `db.sqlite3`
- Delete migration files (keep `__init__.py`)
- Run `makemigrations` then `migrate`

## 📧 Support

For issues or questions:
- Check documentation files
- Review Django docs: https://docs.djangoproject.com
- Check Pillow docs: https://pillow.readthedocs.io

## 🎉 What's Next?

Consider adding:
- Shopping cart
- Payment integration (Stripe)
- User accounts
- Wishlist
- Reviews and ratings
- Advanced search/filters
- Email notifications
- Order tracking
- Multiple currencies

---

Built with ❤️ using Django and modern web technologies

Last Updated: November 2, 2025
Version: 2.0
