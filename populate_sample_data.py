"""
Sample data script for WatchHouse
Run this to populate the database with sample watches
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watchhouse_project.settings')
django.setup()

from watches.models import Watch

# Clear existing watches (optional)
# Watch.objects.all().delete()

# Create sample watches
sample_watches = [
    {
        'name': 'Classic Elegance',
        'brand': 'Rolex',
        'price': 12500.00,
        'description': 'A timeless masterpiece featuring Swiss precision engineering, sapphire crystal, and 18k gold case. Perfect for formal occasions and everyday luxury.',
        'stock': 3
    },
    {
        'name': 'Sport Pro Diver',
        'brand': 'Omega',
        'price': 8900.00,
        'description': 'Professional diving watch with 300m water resistance, automatic movement, and luminous hands. Built for adventure and performance.',
        'stock': 5
    },
    {
        'name': 'Aviator Chrono',
        'brand': 'Breitling',
        'price': 6750.00,
        'description': 'Aviation-inspired chronograph with precision timing, slide rule bezel, and robust stainless steel construction.',
        'stock': 4
    },
    {
        'name': 'Minimalist Modern',
        'brand': 'Daniel Wellington',
        'price': 249.99,
        'description': 'Sleek Scandinavian design with ultra-thin case, genuine leather strap, and minimalist dial. Perfect for the modern professional.',
        'stock': 12
    },
    {
        'name': 'Smartwatch Elite',
        'brand': 'Apple',
        'price': 799.00,
        'description': 'Advanced health monitoring, GPS tracking, cellular connectivity, and stunning OLED display. Your complete fitness and communication companion.',
        'stock': 8
    },
    {
        'name': 'Heritage Vintage',
        'brand': 'Seiko',
        'price': 1250.00,
        'description': 'Japanese craftsmanship meets vintage styling. Automatic movement, exhibition caseback, and premium leather strap.',
        'stock': 6
    },
    {
        'name': 'Luxury Chronometer',
        'brand': 'Patek Philippe',
        'price': 45000.00,
        'description': 'An investment-grade timepiece with perpetual calendar, moon phase, and hand-finished movement. The pinnacle of horological art.',
        'stock': 1
    },
    {
        'name': 'Urban Sport',
        'brand': 'Casio G-Shock',
        'price': 179.99,
        'description': 'Rugged construction, shock resistance, 200m water resistance, and multi-functional digital display. Built to withstand anything.',
        'stock': 15
    },
]

created_count = 0
for watch_data in sample_watches:
    watch, created = Watch.objects.get_or_create(
        name=watch_data['name'],
        brand=watch_data['brand'],
        defaults=watch_data
    )
    if created:
        created_count += 1
        print(f"✓ Created: {watch.brand} - {watch.name}")
    else:
        print(f"- Already exists: {watch.brand} - {watch.name}")

print(f"\nSummary: Created {created_count} new watches, {len(sample_watches) - created_count} already existed.")
print(f"Total watches in database: {Watch.objects.count()}")
