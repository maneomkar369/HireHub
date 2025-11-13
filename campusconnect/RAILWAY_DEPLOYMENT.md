# 🚂 Deploy HireHub to Railway (Recommended)

Railway is **FREE** and perfect for Django apps with included PostgreSQL database!

## ✅ Why Railway Instead of Vercel?

| Feature | Railway | Vercel |
|---------|---------|--------|
| Database | ✅ Included (PostgreSQL) | ❌ Need external |
| File Uploads | ✅ Works | ❌ Need S3/Cloudinary |
| Request Timeout | ✅ No limit | ❌ 10 seconds |
| Django Support | ✅ Perfect | ⚠️ Limited |
| Cost | ✅ Free tier | ✅ Free tier |

## 🚀 Deploy Steps

### Method 1: Railway Dashboard (Easiest)

1. **Go to**: https://railway.app/

2. **Sign up/Login** with GitHub

3. **Click "New Project"**

4. **Select "Deploy from GitHub repo"**

5. **Choose** `maneomkar369/HireHub` repository

6. **Configure**:
   - Root Directory: `campusconnect`
   - Click "Deploy Now"

7. **Add PostgreSQL Database**:
   - Click "New" → "Database" → "Add PostgreSQL"
   - Railway automatically connects it!

8. **Add Environment Variables**:
   Click your service → Variables → Add:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   DJANGO_SETTINGS_MODULE=HireHub.settings
   ```

9. **Generate Domain**:
   - Go to Settings → Generate Domain
   - Your app will be live at: `your-app.railway.app`

### Method 2: Railway CLI

```bash
# Install Railway CLI
npm install -g railway

# Login
railway login

# Link to project
cd /home/vishal/Desktop/inter/campusconnect
railway init

# Deploy
railway up
```

## 📋 After Deployment

### 1. Run Migrations

```bash
railway run python manage.py migrate
```

### 2. Create Superuser

```bash
railway run python manage.py createsuperuser
```

### 3. Collect Static Files (if needed)

```bash
railway run python manage.py collectstatic --noinput
```

## ⚙️ Configuration Files Created

- ✅ `Procfile` - Deployment command
- ✅ `railway.json` - Railway configuration  
- ✅ `requirements.txt` - Updated with gunicorn, psycopg2, whitenoise

## 🌐 Your Live App

After deployment:
- **Live URL**: `https://your-app-name.railway.app`
- **Admin**: `https://your-app-name.railway.app/admin`
- **Database**: Automatically configured PostgreSQL

## 🎉 Benefits

- ✅ **Free $5/month** credit (enough for small apps)
- ✅ **Automatic HTTPS**
- ✅ **PostgreSQL included**
- ✅ **Auto-deploy** on git push
- ✅ **Resume uploads work** out of the box
- ✅ **No cold starts**
- ✅ **Persistent sessions**

## 🔧 Troubleshooting

### If deployment fails:

1. **Check logs**: Railway Dashboard → Deployments → View Logs

2. **Common issues**:
   - Database not connected: Add PostgreSQL service
   - Static files not loading: Check STATIC_ROOT in settings.py
   - Module not found: Check requirements.txt

### Get Help

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway

## 🆚 Comparison: Railway vs Vercel

**Use Railway if:**
- ✅ You need a database
- ✅ You need file uploads (resumes)
- ✅ You want traditional Django deployment
- ✅ You need long-running requests

**Use Vercel if:**
- Only for static sites or serverless APIs
- You already have external database
- You use external storage (S3)

## 💡 Pro Tips

1. **Custom Domain**: Add your own domain in Railway Settings
2. **Environment Variables**: Use Railway's variable management
3. **Monitoring**: Check Railway metrics for performance
4. **Backups**: Railway auto-backups PostgreSQL daily

---

**Ready to deploy?** Just go to https://railway.app and click "Start a New Project"! 🚀
