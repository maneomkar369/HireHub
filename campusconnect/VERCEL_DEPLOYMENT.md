# HireHub - Vercel Deployment

## Deployment Steps

1. **Install Vercel CLI** (if not already installed):
```bash
npm install -g vercel
```

2. **Login to Vercel**:
```bash
vercel login
```

3. **Deploy to Vercel**:
```bash
cd /home/vishal/Desktop/inter/campusconnect
vercel --prod
```

## Important Notes

### Database Configuration
- Vercel uses serverless functions, which means you'll need to use a cloud database
- **Recommended options:**
  - **Vercel Postgres** (easiest integration)
  - **Neon** (PostgreSQL, free tier available)
  - **PlanetScale** (MySQL, free tier available)
  - **MongoDB Atlas** (if switching to MongoDB)

### Environment Variables
Set these in Vercel Dashboard (Settings → Environment Variables):

```
DEBUG=False
SECRET_KEY=your-secure-secret-key-here
DATABASE_URL=your-database-connection-url
ALLOWED_HOSTS=.vercel.app,.now.sh
```

### Media Files Storage
- Vercel's serverless functions are read-only
- You need to use external storage for uploaded files (resumes)
- **Recommended options:**
  - **Vercel Blob Storage**
  - **AWS S3**
  - **Cloudinary**

Install django-storages for S3/Cloudinary:
```bash
pip install django-storages boto3
```

### Static Files
- Already configured in `settings.py`
- Will be collected during build process

### Migration Commands
After deployment, run migrations:
```bash
vercel env pull .env.local
python manage.py migrate --settings=HireHub.settings
```

## Files Created for Vercel

1. **vercel.json** - Vercel configuration
2. **build_files.sh** - Build script for collecting static files
3. **requirements.txt** - Python dependencies

## Quick Deploy Command

```bash
# From campusconnect directory
vercel --prod
```

## Post-Deployment Setup

1. **Set up database** (choose one):
   - Vercel Postgres: https://vercel.com/docs/storage/vercel-postgres
   - Neon: https://neon.tech/
   - PlanetScale: https://planetscale.com/

2. **Configure media storage** (for resume uploads):
   - Vercel Blob: https://vercel.com/docs/storage/vercel-blob
   - Or use S3/Cloudinary

3. **Run migrations**:
```bash
vercel env pull
python manage.py migrate
python manage.py createsuperuser
```

## Troubleshooting

### If deployment fails:
1. Check Vercel build logs
2. Verify all environment variables are set
3. Ensure database is accessible
4. Check that all dependencies are in requirements.txt

### Common Issues:
- **Database connection error**: Set DATABASE_URL in Vercel environment variables
- **Static files not loading**: Check STATIC_ROOT and run collectstatic
- **Media uploads failing**: Configure external storage (S3/Cloudinary/Vercel Blob)

## Alternative: Railway Deployment

If Vercel gives issues with Django, Railway is a better option:

```bash
# Install Railway CLI
npm install -g railway

# Login and deploy
railway login
railway init
railway up
```

Railway handles Django better and includes database by default.
