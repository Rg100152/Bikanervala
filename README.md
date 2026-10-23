
# 🍬 Bikanervala Clone — Pure Desi Ghee Indian Mithai Store

A fully functional, single-file **Flask** e-commerce website inspired by [Bikanervala](https://bikanervala.com). Built with **Python + Flask + Tailwind CSS**, featuring a royal Rajasthani aesthetic, dynamic cart, wishlist, search, filters, and checkout — all running from **one `app.py` file**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.3-green?logo=flask&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-CSS-38BDF8?logo=tailwindcss&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🛍️ **Product Catalog** | 12 authentic Indian sweets with Hindi names, ingredients & shelf life |
| 🔍 **Live Search** | Instant autocomplete suggestions with images |
| 🎯 **Smart Filters** | Category, price range, Pure Ghee, Bestseller, Sugar-Free, Vrat-friendly |
| 🛒 **Session Cart** | Add, update quantity, remove items — saved server-side |
| ❤️ **Wishlist** | Save favorites with badge counter |
| 🎟️ **Coupons** | `DIWALI25` (15% off) & `SWEET10` (10% off) |
| 🚚 **Free Delivery Bar** | Progress bar unlocks at ₹999 |
| 💳 **Checkout** | UPI / Card / COD with order ID generation |
| 🎉 **Confetti Celebration** | Order success animation |
| 📍 **Pincode Checker** | Delivery eligibility validation |
| 📦 **Order Tracking** | Live timeline modal |
| 🌐 **LAN Access** | Works on `localhost` + same WiFi devices |
| 📱 **Fully Responsive** | Mobile-first Tailwind design |

---

## 🖼️ Screenshots

> Add these after taking screenshots — replace with your own image paths

| Home | Cart Drawer | Checkout |
|------|-------------|----------|
| ![Home](screenshots/home.png) | ![Cart](screenshots/cart.png) | ![Checkout](screenshots/checkout.png) |

---

## 🛠️ Tech Stack

- **Backend:** Python 3.10+, Flask 3.1.3
- **Frontend:** HTML5, Tailwind CSS (CDN), Vanilla JavaScript
- **Icons:** [Lucide Icons](https://lucide.dev)
- **Fonts:** Cinzel + Inter (Google Fonts)
- **Effects:** Canvas Confetti
- **Storage:** Flask Session (in-memory cookie-based)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Flask installed

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Rg100152/Bikanervala.git
cd Bikanervala
```

2️⃣ Install dependencies

```bash
pip install flask
```

3️⃣ Run the app

```bash
python app.py
```

4️⃣ Open in browser

· Local: http://127.0.0.1:8080
· LAN (same WiFi): http://<your-ip>:8080

💡 Terminal will print the URLs automatically on startup.

---

📱 Run on Android (Pydroid 3)

This project is specially optimized to run on Pydroid 3 without any folder structure:

1. Install Pydroid 3 from F-Droid (recommended) or Play Store
2. Install Flask from the Pip menu in Pydroid 3
3. Create app.py → paste the code → Run ▶️
4. Open Chrome → http://127.0.0.1:8080

⚠️ Keep Pydroid 3 in foreground (screen on) while using the site.

---

📂 Project Structure

```
Bikanervala/
│
├── app.py              # Complete Flask app (HTML embedded)
├── README.md           # You're reading this
└── screenshots/        # (Optional) UI screenshots
    ├── home.png
    ├── cart.png
    └── checkout.png
```

Single-file architecture — no templates/, no static/, no external assets required. The HTML page is embedded directly inside app.py using render_template_string.

---

🔌 API Endpoints

Method Endpoint Description
GET / Render the homepage
POST /api/cart/add Add product to cart
POST /api/cart/update Update quantity (+/-)
POST /api/cart/remove Remove item by index
POST /api/wishlist/toggle Add/remove from wishlist
POST /api/checkout Place order & generate ID

---

🎟️ Test Coupons

Code Discount
DIWALI25 15% off
SWEET10 10% off

---

🧁 Products Included

1. Diamond Cut Kaju Katli — काजू कतली
2. Pure Desi Ghee Gulab Jamun — गुलाब जामुन
3. Handcrafted Motichoor Laddu — मोतीचूर लड्डू
4. Spongy Kolkata Rasgulla — रसगुल्ला
5. Flaky Almond Soan Papdi — सोन पापड़ी
6. Desi Ghee Besan Laddu — बेसन लड्डू
7. Rich Mysore Pak — मैसूर पाक
8. Caramelized Punjabi Dodha Burfi — डोडा बर्फी
9. Sugar-Free Anjeer Dry Fruit Barfi — अंजीर बर्फी
10. Mathura Style Khoya Peda — मथुरा पेड़ा
11. Kaju Pistachio Roll — काजू पिस्ता रोल
12. Royal Mithai Thali Gift Box — शाही मिठाई थाली

Each product includes 3 weight variants (250g / 500g / 1kg) with MRP & discount pricing.

---

🎨 Design Highlights

· Royal Maroon (#7B111F) + Gold (#DCA524) color palette
· Traditional rangoli dot pattern background
· Cinzel serif typography for the royal heritage feel
· Veg symbol (green dot in square) on every product card
· Vacuum-sealed packaging trust badges
· Smooth slide-over drawers for cart & wishlist
· Indian FSSAI certification style badges

---

🛠️ Customization

Change product data

Edit the SWEETS_DATABASE list in app.py:

```python
{"id": 1, "name": "Your Sweet", "category": "kaju",
 "variants": [{"weight": "500g", "price": 500, "originalPrice": 600}],
 ...}
```

Change port

At the bottom of app.py:

```python
app.run(host='0.0.0.0', port=8080, debug=False)
```

Change secret key

```python
app.secret_key = 'your-secure-key-here'
```

---

⚠️ Known Limitations

· Cart & wishlist are session-based — they reset when server restarts
· No real payment gateway (UPI/Card are mock options)
· No persistent database (SQLite/PostgreSQL can be added)
· Product images use Unsplash URLs (online required)

---

🚧 Roadmap

☐ Migrate to SQLite database
☐ Add user authentication (login/signup)
☐ Integrate Razorpay / Stripe payment
☐ Admin dashboard for order management
☐ PDF invoice generation
☐ Email order confirmation
☐ PWA support for offline browsing

---

🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch: git checkout -b feature/cool-feature
3. Commit changes: git commit -m 'Add cool feature'
4. Push: git push origin feature/cool-feature
5. Open a Pull Request

---

📄 License

This project is licensed under the MIT License — feel free to use, modify, and distribute.

⚠️ This project is a educational clone inspired by Bikanervala. It is not affiliated with or endorsed by Bikanervala Foods Pvt. Ltd. All trademarks belong to their respective owners.

---

👨‍💻 Author

Rohit Gupta

· GitHub: @Rg100152
· Repository: Bikanervala

---

🙏 Acknowledgements

· Bikanervala for design inspiration
· Unsplash for product imagery
· Tailwind CSS for rapid styling
· Lucide for crisp icons
· Flask for the lightweight backend

---

<p align="center">
  <strong>🍬 Made with ❤️ and Pure Desi Ghee 🍬</strong><br>
  <em>Mithai Mubarak!</em>
</p>
```

---

📤 GitHub Par Upload Karne Ka Tarika

1. Apne repo Rg100152/Bikanervala par jayein
2. "Add file" → "Create new file" click karein
3. File name mein README.md likhein
4. Upar wala code paste karein
5. Neeche "Commit new file" dabayein

Bas! Aapka README professionally ready hai. 🚀

💡 Extra Tip

Agar aap chahein toh main requirements.txt, .gitignore, aur LICENSE file bhi bana kar de sakta hoon — ek professional repo ke liye. Bas batayein!
