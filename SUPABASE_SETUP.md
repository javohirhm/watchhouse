# WatchHouse - Supabase Configuration Guide

## Step 1: Create a Supabase Project

1. Go to https://supabase.com and sign up/login
2. Click "New Project"
3. Fill in:
   - Name: WatchHouse
   - Database Password: (choose a strong password and save it)
   - Region: Choose closest to you
4. Click "Create new project" and wait for setup to complete

## Step 2: Get Your Supabase Credentials

1. In your Supabase project dashboard, go to "Settings" → "API"
2. You'll need:
   - **Project URL**: Found under "Project URL"
   - **API Key (anon/public)**: Found under "Project API keys"
   - **Database Password**: The one you set during project creation

## Step 3: Get Database Connection String

1. Go to "Settings" → "Database"
2. Scroll down to "Connection string" → "URI"
3. Copy the connection string (it looks like):
   ```
   postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@aws-0-[REGION].pooler.supabase.com:6543/postgres
   ```
4. Replace `[YOUR-PASSWORD]` with your actual database password

## Step 4: Configure Django Settings

1. Create a `.env` file in your project root (/home/claude/watchhouse/.env):

```env
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here
DATABASE_URL=your_database_connection_string_here
SECRET_KEY=your_django_secret_key
```

2. Install python-decouple:
```bash
pip install python-decouple --break-system-packages
```

3. Update your settings.py with the configuration below.

## Step 5: Update Django settings.py

Add these imports at the top of settings.py:
```python
from decouple import config
import dj_database_url
```

Replace the DATABASES section with:
```python
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
```

## Step 6: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Step 7: Verify in Supabase

1. Go to your Supabase dashboard
2. Click "Table Editor" on the left sidebar
3. You should see your Django tables:
   - watches_watch
   - watches_order
   - auth_user
   - django_migrations
   - etc.

## Alternative: Using Supabase Python Client (Optional)

If you want to use Supabase's Python client directly instead of Django ORM:

```python
from supabase import create_client, Client
from decouple import config

supabase: Client = create_client(
    config('SUPABASE_URL'),
    config('SUPABASE_KEY')
)

# Example: Insert order
data = supabase.table('watches_order').insert({
    "watch_id": 1,
    "customer_name": "John Doe",
    "customer_phone": "+1234567890"
}).execute()
```

## Important Notes

1. **Security**: Never commit your .env file to version control!
2. **Connection Pooling**: Supabase uses connection pooling by default
3. **SSL**: Supabase requires SSL connections (handled automatically)
4. **Row Level Security**: You may want to configure RLS policies in Supabase for production

## Troubleshooting

### Can't connect to database
- Verify your connection string is correct
- Check that you replaced [YOUR-PASSWORD] with actual password
- Ensure your IP is allowed (Supabase allows all by default)

### Tables not showing in Supabase
- Make sure migrations ran successfully
- Check Django logs for errors
- Verify DATABASE_URL is correctly set

### Authentication issues
- Double-check SUPABASE_KEY is the anon/public key
- Verify SUPABASE_URL doesn't have trailing slash

## Current Configuration

The project is currently set up with:
- SQLite as default (for development)
- Models: Watch, Order
- Admin interface enabled
- All migrations ready to run

To switch to Supabase, follow steps above and update settings.py accordingly.
