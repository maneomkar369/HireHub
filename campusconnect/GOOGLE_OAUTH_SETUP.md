# 🔐 Google OAuth Setup Guide for HireHub

## ✅ What's Already Done

The HireHub application is now **fully configured** for Google OAuth authentication! Here's what's been implemented:

### Backend Configuration ✓
- ✅ Django-allauth installed and configured
- ✅ Google OAuth provider enabled
- ✅ Database migrations completed
- ✅ Authentication middleware added
- ✅ All dependencies installed (requests, PyJWT, cryptography)
- ✅ Settings configured for social authentication

### Frontend Integration ✓
- ✅ "Continue with Google" button added to login page
- ✅ Proper Google branding and logo
- ✅ Fully responsive design for all devices
- ✅ Mobile-friendly hamburger navigation menu

### Responsive Design ✓
- ✅ Mobile responsive (320px - 640px)
- ✅ Tablet responsive (641px - 1024px)
- ✅ Desktop responsive (1025px+)
- ✅ Navigation menu works on all screen sizes
- ✅ All pages optimized for mobile viewing

## 🚀 How to Complete Google OAuth Setup

### Step 1: Create Google Cloud Project

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/

2. **Create a New Project**
   - Click "Select a project" → "New Project"
   - Project Name: `HireHub` (or any name)
   - Click "Create"

### Step 2: Enable Google OAuth

1. **Enable Google+ API**
   - In your project, go to "APIs & Services" → "Library"
   - Search for "Google+ API"
   - Click "Enable"

2. **Configure OAuth Consent Screen**
   - Go to "APIs & Services" → "OAuth consent screen"
   - Select "External" (for public access)
   - Fill in:
     - App name: `HireHub`
     - User support email: Your email
     - Developer contact: Your email
   - Click "Save and Continue"
   - Add scopes: `email`, `profile`
   - Click "Save and Continue"
   - Add test users (your email) if needed
   - Click "Save and Continue"

### Step 3: Create OAuth Credentials

1. **Create OAuth 2.0 Client ID**
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "OAuth 2.0 Client ID"
   - Application type: "Web application"
   - Name: `HireHub Web Client`

2. **Add Authorized URLs**
   
   **For Local Development:**
   - Authorized JavaScript origins:
     ```
     http://localhost:8000
     http://127.0.0.1:8000
     ```
   - Authorized redirect URIs:
     ```
     http://localhost:8000/accounts/google/login/callback/
     http://127.0.0.1:8000/accounts/google/login/callback/
     ```

   **For Production (Railway):**
   - Authorized JavaScript origins:
     ```
     https://hire-hub-production.up.railway.app
     ```
   - Authorized redirect URIs:
     ```
     https://hire-hub-production.up.railway.app/accounts/google/login/callback/
     ```

3. **Save Credentials**
   - Click "Create"
   - **Copy the Client ID and Client Secret** (you'll need these!)

### Step 4: Add Credentials to Railway

1. **Go to Railway Dashboard**
   - Visit: https://railway.app/
   - Select your `hire-hub` project
   - Click on your service

2. **Add Environment Variables**
   - Go to "Variables" tab
   - Add these two variables:
   ```
   GOOGLE_CLIENT_ID=your-client-id-here.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=your-client-secret-here
   ```
   - Replace with the credentials from Step 3

3. **Redeploy**
   - Railway will automatically redeploy with new variables
   - Or manually click "Deploy" to restart

### Step 5: Configure Social App in Django Admin

1. **Access Admin Panel**
   - Go to: https://hire-hub-production.up.railway.app/admin/
   - Login with your superuser account

2. **Add Social Application**
   - Click "Social applications" under "SOCIAL ACCOUNTS"
   - Click "Add Social Application"
   - Fill in:
     - Provider: `Google`
     - Name: `Google OAuth`
     - Client id: `your-client-id-here`
     - Secret key: `your-client-secret-here`
     - Sites: Select `example.com` (or your domain)
   - Click "Save"

### Step 6: Test Google Login

1. **Open Login Page**
   - Go to: https://hire-hub-production.up.railway.app/login/

2. **Click "Continue with Google"**
   - You'll be redirected to Google login
   - Sign in with your Google account
   - Grant permissions
   - You'll be redirected back to HireHub dashboard!

## 🎯 Features Now Available

### For Students
- ✅ Sign up with Google (no password needed!)
- ✅ Login with Google
- ✅ Auto-profile creation from Google account
- ✅ Email automatically verified

### For Recruiters
- ✅ Quick signup with company Google account
- ✅ Fast authentication
- ✅ Professional account creation

### Security Features
- ✅ OAuth 2.0 secure authentication
- ✅ No password storage needed
- ✅ Google-verified emails
- ✅ CSRF protection
- ✅ Secure redirect URLs

## 📱 Responsive Design Features

### Mobile (320px - 640px)
- ✅ Hamburger menu navigation
- ✅ Touch-friendly buttons
- ✅ Optimized form layouts
- ✅ Mobile-first design

### Tablet (641px - 1024px)
- ✅ Adaptive navigation
- ✅ Optimized spacing
- ✅ Better use of screen space

### Desktop (1025px+)
- ✅ Full navigation bar
- ✅ Wide layout support
- ✅ Enhanced UI elements

## 🔧 Troubleshooting

### Google Login Not Working?

1. **Check OAuth Redirect URI**
   - Must exactly match: `https://your-domain.com/accounts/google/login/callback/`
   - Include the trailing slash!

2. **Verify Environment Variables**
   ```bash
   railway run env | grep GOOGLE
   ```
   - Should show `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`

3. **Check Social Application**
   - Admin panel → Social applications
   - Verify Client ID and Secret are correct
   - Ensure the correct site is selected

4. **Check Logs**
   ```bash
   railway logs
   ```
   - Look for OAuth-related errors

### "Redirect URI Mismatch" Error?

- **Cause**: URL in Google Console doesn't match callback URL
- **Fix**: Add exact callback URL to Google Console:
  ```
  https://hire-hub-production.up.railway.app/accounts/google/login/callback/
  ```

### Mobile Menu Not Working?

- **Cause**: Alpine.js not loaded
- **Fix**: Already included in base.html via CDN
- Clear browser cache and refresh

## 📚 Additional Resources

- **Django Allauth Docs**: https://django-allauth.readthedocs.io/
- **Google OAuth Guide**: https://developers.google.com/identity/protocols/oauth2
- **Railway Docs**: https://docs.railway.app/

## 🎉 Success Checklist

Before going live, ensure:

- ✅ Google Cloud project created
- ✅ OAuth consent screen configured
- ✅ Client ID and Secret created
- ✅ Environment variables added to Railway
- ✅ Social application created in Django admin
- ✅ Callback URLs added to Google Console
- ✅ Tested login flow end-to-end
- ✅ Mobile responsive navigation tested
- ✅ All pages are mobile-friendly

## 💡 Pro Tips

1. **Test Users**: Add your email as a test user during OAuth setup
2. **Production Domain**: Update authorized origins when you add a custom domain
3. **Security**: Never commit Client Secret to Git (use environment variables)
4. **User Experience**: Google login is faster than traditional signup
5. **Mobile First**: Always test on mobile devices for best UX

---

**Need Help?** Check Railway logs or contact support!

**Your app is ready!** Just complete the Google OAuth setup and you're live! 🚀
