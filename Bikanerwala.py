from flask import Flask, render_template_string, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'bikanervala_secret_2026_key'

# ================= PRODUCTS DATABASE =================
SWEETS_DATABASE = [
    {"id": 1, "name": "Diamond Cut Kaju Katli", "hindiName": "काजू कतली", "category": "kaju",
     "badge": "Bestseller", "badgeColor": "bg-amber-600", "rating": 4.9, "reviews": 1420,
     "description": "Finest Goan cashews grounded to velvety smoothness with edible pure silver leaf garnish.",
     "ingredients": "Cashew Nuts, Sugar, Edible Silver Leaf, Cardamom.", "shelfLife": "30 Days",
     "image": "https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?q=80&w=700&auto=format&fit=crop",
     "isGhee": False, "isSugarFree": False, "isVrat": True,
     "variants": [{"weight": "250g", "price": 320, "originalPrice": 350},
                  {"weight": "500g", "price": 620, "originalPrice": 699},
                  {"weight": "1kg", "price": 1199, "originalPrice": 1350}]},
    {"id": 2, "name": "Pure Desi Ghee Gulab Jamun", "hindiName": "गुलाब जामुन", "category": "ghee",
     "badge": "Desi Ghee", "badgeColor": "bg-red-700", "rating": 4.8, "reviews": 980,
     "description": "Soft, golden dumplings prepared with condensed milk mawa, deep-fried in 100% pure desi cow ghee.",
     "ingredients": "Mawa, Pure Cow Desi Ghee, Saffron, Rose Water.", "shelfLife": "60 Days",
     "image": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?q=80&w=700&auto=format&fit=crop",
     "isGhee": True, "isSugarFree": False, "isVrat": False,
     "variants": [{"weight": "500g", "price": 290, "originalPrice": 340},
                  {"weight": "1kg", "price": 540, "originalPrice": 620}]},
    {"id": 3, "name": "Handcrafted Motichoor Laddu", "hindiName": "मोतीचूर लड्डू", "category": "laddus",
     "badge": "Pure Ghee", "badgeColor": "bg-red-700", "rating": 4.9, "reviews": 2100,
     "description": "Tiny micro-pearls of gram flour fried in aromatic desi ghee, infused with green cardamom.",
     "ingredients": "Gram Flour, Pure Cow Ghee, Melon Seeds, Saffron, Cardamom.", "shelfLife": "15 Days",
     "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?q=80&w=700&auto=format&fit=crop",
     "isGhee": True, "isSugarFree": False, "isVrat": False,
     "variants": [{"weight": "250g", "price": 190, "originalPrice": 220},
                  {"weight": "500g", "price": 360, "originalPrice": 420},
                  {"weight": "1kg", "price": 680, "originalPrice": 790}]},
    {"id": 4, "name": "Spongy Kolkata Rasgulla", "hindiName": "रसगुल्ला", "category": "chenna",
     "badge": "Bestseller", "badgeColor": "bg-amber-600", "rating": 4.7, "reviews": 860,
     "description": "Pristine white dumplings of fresh cow milk chenna boiled in delicate clarified sugar syrup.",
     "ingredients": "Fresh Cow Milk Chenna, Sugar, Rose Water.", "shelfLife": "30 Days",
     "image": "https://images.unsplash.com/photo-1541832676-9b763b0239ab?q=80&w=700&auto=format&fit=crop",
     "isGhee": False, "isSugarFree": False, "isVrat": True,
     "variants": [{"weight": "500g", "price": 210, "originalPrice": 250},
                  {"weight": "1kg", "price": 390, "originalPrice": 450}]},
    {"id": 5, "name": "Flaky Almond Soan Papdi", "hindiName": "सोन पापड़ी", "category": "ghee",
     "badge": "Traditional", "badgeColor": "bg-emerald-700", "rating": 4.6, "reviews": 620,
     "description": "Crisp multilayered golden threads made with roasted besan and pure ghee.",
     "ingredients": "Desi Ghee, Gram Flour, Pistachios, Almonds.", "shelfLife": "90 Days",
     "image": "https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?q=80&w=700&auto=format&fit=crop",
     "isGhee": True, "isSugarFree": False, "isVrat": False,
     "variants": [{"weight": "250g", "price": 160, "originalPrice": 190},
                  {"weight": "500g", "price": 295, "originalPrice": 340}]},
    {"id": 6, "name": "Desi Ghee Besan Laddu", "hindiName": "बेसन लड्डू", "category": "laddus",
     "badge": "Bestseller", "badgeColor": "bg-amber-600", "rating": 4.8, "reviews": 1140,
     "description": "Slow-roasted coarse chickpea flour prepared in bubbling desi ghee.",
     "ingredients": "Roasted Besan, Pure Cow Ghee, Bura Sugar, Cashews.", "shelfLife": "45 Days",
     "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?q=80&w=700&auto=format&fit=crop",
     "isGhee": True, "isSugarFree": False, "isVrat": False,
     "variants": [{"weight": "250g", "price": 180, "originalPrice": 210},
                  {"weight": "500g", "price": 340, "originalPrice": 390},
                  {"weight": "1kg", "price": 650, "originalPrice": 740}]},
    {"id": 7, "name": "Rich Mysore Pak (Ghee Melt)", "hindiName": "मैसूर पाक", "category": "ghee",
     "badge": "Royal Delicacy", "badgeColor": "bg-amber-700", "rating": 4.9, "reviews": 790,
     "description": "South Indian royal sweet made with copious quantities of golden desi ghee.",
     "ingredients": "Pure Cow Ghee, Roasted Gram Flour, Sugar, Cardamom.", "shelfLife": "25 Days",
     "image": "https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?q=80&w=700&auto=format&fit=crop",
     "isGhee": True, "isSugarFree": False, "isVrat": False,
     "variants": [{"weight": "250g", "price": 220, "originalPrice": 260},
                  {"weight": "500g", "price": 420, "originalPrice": 480},
                  {"weight": "1kg", "price": 799, "originalPrice": 920}]},
    {"id": 8, "name": "Caramelized Punjabi Dodha Burfi", "hindiName": "डोडा बर्फी", "category": "ghee",
     "badge": "Desi Ghee", "badgeColor": "bg-red-700", "rating": 4.8, "reviews": 580,
     "description": "Traditional Punjabi fudge crafted from slow-simmered sprouted wheat flour.",
     "ingredients": "Sprouted Wheat, Cow Milk, Desi Ghee, Walnuts.", "shelfLife": "30 Days",
     "image": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?q=80&w=700&auto=format&fit=crop",
     "isGhee": True, "isSugarFree": False, "isVrat": False,
     "variants": [{"weight": "250g", "price": 210, "originalPrice": 250},
                  {"weight": "500g", "price": 390, "originalPrice": 450},
                  {"weight": "1kg", "price": 750, "originalPrice": 860}]},
    {"id": 9, "name": "Sugar-Free Anjeer Dry Fruit Barfi", "hindiName": "अंजीर बर्फी", "category": "dryfruit",
     "badge": "Zero Added Sugar", "badgeColor": "bg-emerald-700", "rating": 4.9, "reviews": 930,
     "description": "Naturally sweet Turkish figs blended with roasted California almonds, pistachios.",
     "ingredients": "Turkish Dried Figs, Almonds, Cashews, Pistachios.", "shelfLife": "60 Days",
     "image": "https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?q=80&w=700&auto=format&fit=crop",
     "isGhee": False, "isSugarFree": True, "isVrat": True,
     "variants": [{"weight": "250g", "price": 380, "originalPrice": 420},
                  {"weight": "500g", "price": 720, "originalPrice": 799},
                  {"weight": "1kg", "price": 1390, "originalPrice": 1550}]},
    {"id": 10, "name": "Mathura Style Khoya Peda", "hindiName": "मथुरा पेड़ा", "category": "chenna",
     "badge": "Traditional", "badgeColor": "bg-amber-600", "rating": 4.7, "reviews": 640,
     "description": "Caramelized brown khoya pedas prepared according to Braj Mathura style.",
     "ingredients": "Cow Milk Khoya, Boora Sugar, Cardamom, Ghee.", "shelfLife": "20 Days",
     "image": "https://images.unsplash.com/photo-1541832676-9b763b0239ab?q=80&w=700&auto=format&fit=crop",
     "isGhee": True, "isSugarFree": False, "isVrat": True,
     "variants": [{"weight": "250g", "price": 180, "originalPrice": 210},
                  {"weight": "500g", "price": 340, "originalPrice": 390}]},
    {"id": 11, "name": "Kaju Pistachio Roll", "hindiName": "काजू पिस्ता रोल", "category": "kaju",
     "badge": "Premium Gift", "badgeColor": "bg-purple-700", "rating": 4.9, "reviews": 510,
     "description": "Cylindrical cashew dough wrapper filled with rich emerald green pistachio core.",
     "ingredients": "Cashews, Pistachios, Sugar, Cardamom.", "shelfLife": "30 Days",
     "image": "https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?q=80&w=700&auto=format&fit=crop",
     "isGhee": False, "isSugarFree": False, "isVrat": True,
     "variants": [{"weight": "250g", "price": 340, "originalPrice": 380},
                  {"weight": "500g", "price": 650, "originalPrice": 730},
                  {"weight": "1kg", "price": 1250, "originalPrice": 1400}]},
    {"id": 12, "name": "Royal Mithai Thali Gift Box", "hindiName": "शाही मिठाई थाली", "category": "hampers",
     "badge": "Festive Box", "badgeColor": "bg-red-800", "rating": 5.0, "reviews": 1350,
     "description": "Curated royal presentation tray containing Kaju Katli, Besan Laddu, Dodha Burfi and Almonds.",
     "ingredients": "Assorted Cashew, Pure Ghee, Pistachio, Almonds.", "shelfLife": "30 Days",
     "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?q=80&w=700&auto=format&fit=crop",
     "isGhee": True, "isSugarFree": False, "isVrat": False,
     "variants": [{"weight": "900g Royal Hamper", "price": 1150, "originalPrice": 1399},
                  {"weight": "1.5kg Deluxe Gold Hamper", "price": 1850, "originalPrice": 2200}]},
]

# ================= HTML TEMPLATE (Embedded) =================
HTML_PAGE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bikanervala Sweets | Pure Desi Ghee Mithai</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: { extend: {
        colors: {
          royal: {900:'#580812',800:'#7B111F',700:'#9B1D2C',100:'#FDF4F4'},
          gold: {400:'#F3C043',500:'#DCA524',600:'#B88210'},
          cream: '#FCF8F2', cardbg: '#FFFDF9'
        },
        fontFamily: { serif: ['Cinzel','Georgia','serif'], sans: ['Inter','system-ui','sans-serif'] }
      }}
    }
  </script>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
  <style>
    ::-webkit-scrollbar{width:6px;height:6px}
    ::-webkit-scrollbar-thumb{background:#DCA524;border-radius:4px}
    .gold-gradient-text{background:linear-gradient(135deg,#FFE28A,#DCA524,#9B6700);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
    .royal-gradient{background:linear-gradient(135deg,#7B111F,#4D060E)}
    .veg-symbol{width:15px;height:15px;border:1.5px solid #16a34a;display:inline-flex;align-items:center;justify-content:center;border-radius:3px;background:#fff}
    .veg-dot{width:7px;height:7px;background:#16a34a;border-radius:50%}
    .bg-rangoli{background-color:#FAF5EE;background-image:radial-gradient(#dca524 0.65px,transparent 0.65px);background-size:26px 26px}
  </style>
</head>
<body class="bg-rangoli text-neutral-800 font-sans antialiased">

  <!-- ANNOUNCEMENT BAR -->
  <div class="bg-royal-900 text-amber-200 text-xs py-2 px-4 border-b border-gold-500/30">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-2">
      <div class="flex items-center gap-2">
        <span class="bg-gold-500 text-royal-900 text-[10px] font-bold px-2 py-0.5 rounded-full uppercase">Festive</span>
        <span>✨ Free delivery above ₹999 | Use code <strong class="text-white underline cursor-pointer" onclick="quickApplyCoupon('DIWALI25')">DIWALI25</strong> for 15% OFF!</span>
      </div>
      <div class="flex items-center gap-4 text-[11px]">
        <button onclick="openModal('pincodeModal')" class="hover:text-gold-400 flex items-center gap-1"><i data-lucide="map-pin" class="w-3.5 h-3.5 text-gold-400"></i><span id="currentPincodeLabel">Deliver to: 110001</span></button>
        <span class="opacity-40">|</span>
        <button onclick="openModal('trackOrderModal')" class="hover:text-gold-400 flex items-center gap-1"><i data-lucide="truck" class="w-3.5 h-3.5"></i> Track</button>
      </div>
    </div>
  </div>

  <!-- HEADER -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md shadow-md border-b border-amber-100">
    <div class="max-w-7xl mx-auto px-4 py-3.5 flex items-center justify-between gap-4">
      <a href="#" class="flex items-center gap-3">
        <div class="w-11 h-11 rounded-full royal-gradient flex items-center justify-center border-2 border-gold-500 shadow-md">
          <span class="font-serif font-black text-xl text-gold-400">B</span>
        </div>
        <div class="flex flex-col">
          <div class="flex items-center gap-1.5">
            <span class="font-serif font-extrabold text-2xl text-royal-900">BIKANERVALA</span>
            <span class="text-[10px] bg-red-100 text-royal-800 font-bold px-1.5 py-0.5 rounded border border-red-200">1905</span>
          </div>
          <span class="text-[10px] tracking-widest text-gold-600 uppercase">Sweets • Savouries • Delights</span>
        </div>
      </a>

      <div class="relative flex-1 max-w-md hidden md:block">
        <input type="text" id="searchInput" placeholder="Search Kaju Katli, Gulab Jamun..." class="w-full pl-10 pr-10 py-2.5 bg-cream border border-amber-200 rounded-full text-sm focus:outline-none focus:ring-2 focus:ring-gold-500" oninput="handleSearch(this.value)"/>
        <i data-lucide="search" class="w-4 h-4 text-neutral-400 absolute left-3.5 top-3"></i>
        <button id="clearSearchBtn" onclick="clearSearch()" class="hidden absolute right-3.5 top-2.5 text-neutral-400"><i data-lucide="x" class="w-4 h-4"></i></button>
        <div id="searchDropdown" class="hidden absolute left-0 right-0 top-12 bg-white rounded-2xl shadow-2xl border border-amber-200 p-3 z-50 max-h-80 overflow-y-auto"></div>
      </div>

      <div class="flex items-center gap-3 sm:gap-5">
        <div class="hidden lg:flex items-center gap-1.5 text-xs font-semibold text-emerald-800 bg-emerald-50 px-3 py-1.5 rounded-full border border-emerald-200">
          <div class="veg-symbol"><div class="veg-dot"></div></div><span>Pure Desi Ghee</span>
        </div>
        <button onclick="openWishlistDrawer()" class="relative p-2 text-royal-900 hover:text-gold-600">
          <i data-lucide="heart" class="w-6 h-6"></i>
          <span id="wishlistCountBadge" class="hidden absolute -top-1 -right-1 bg-royal-700 text-white text-[10px] font-bold w-5 h-5 rounded-full flex items-center justify-center border-2 border-white">0</span>
        </button>
        <button onclick="toggleCartDrawer(true)" class="relative flex items-center gap-2 bg-royal-900 hover:bg-royal-800 text-amber-200 px-3.5 py-2 rounded-full font-medium text-sm">
          <div class="relative">
            <i data-lucide="shopping-bag" class="w-5 h-5"></i>
            <span id="cartCountBadge" class="absolute -top-2 -right-2 bg-gold-500 text-royal-900 text-[10px] font-extrabold w-4 h-4 rounded-full flex items-center justify-center">0</span>
          </div>
          <span class="hidden sm:inline font-bold" id="cartTotalHeader">₹0</span>
        </button>
      </div>
    </div>

    <nav class="bg-royal-900 text-white overflow-x-auto text-xs font-medium border-t border-gold-500/20">
      <div class="max-w-7xl mx-auto px-4 flex items-center gap-6 whitespace-nowrap py-2.5">
        <button onclick="setCategoryFilter('all')" class="text-amber-300 font-bold hover:text-amber-200">All Sweets</button>
        <button onclick="setCategoryFilter('kaju')" class="text-neutral-200 hover:text-amber-300">Kaju Delights</button>
        <button onclick="setCategoryFilter('ghee')" class="text-neutral-200 hover:text-amber-300">Desi Ghee</button>
        <button onclick="setCategoryFilter('chenna')" class="text-neutral-200 hover:text-amber-300">Bengali</button>
        <button onclick="setCategoryFilter('laddus')" class="text-neutral-200 hover:text-amber-300">Laddus</button>
        <button onclick="setCategoryFilter('dryfruit')" class="text-neutral-200 hover:text-amber-300">Sugar Free</button>
        <button onclick="setCategoryFilter('hampers')" class="text-neutral-200 hover:text-amber-300">Hampers</button>
      </div>
    </nav>
  </header>

  <!-- HERO -->
  <section class="relative bg-royal-900 text-white border-b-4 border-gold-500">
    <div class="max-w-7xl mx-auto px-4 py-10 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        <div class="lg:col-span-7 space-y-4">
          <div class="inline-flex items-center gap-2 bg-gold-500/20 text-gold-300 border border-gold-500/40 px-3.5 py-1 rounded-full text-xs font-semibold">
            <i data-lucide="crown" class="w-3.5 h-3.5 text-gold-400"></i> Heritage Since 1905
          </div>
          <h1 class="font-serif text-3xl sm:text-5xl font-extrabold leading-tight">
            Pure Desi Ghee <br/><span class="gold-gradient-text">Authentic Indian Mithai</span>
          </h1>
          <p class="text-neutral-200 text-sm max-w-xl">Handcrafted by master halwais with 100% pure cow ghee, premium Kashmiri saffron, and top-grade dry fruits.</p>
        </div>
        <div class="lg:col-span-5">
          <div class="relative mx-auto max-w-sm rounded-2xl overflow-hidden shadow-2xl border-2 border-gold-500/50">
            <img src="https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?q=80&w=800&auto=format&fit=crop" alt="Sweets" class="w-full h-72 object-cover"/>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- MAIN -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 py-8">
    <div class="flex flex-col lg:flex-row gap-8 items-start">

      <!-- FILTER SIDEBAR -->
      <aside class="w-full lg:w-72 bg-white rounded-2xl p-5 shadow-sm border border-amber-200/80 shrink-0">
        <div class="flex items-center justify-between pb-3 border-b border-amber-100">
          <h2 class="font-serif font-bold text-royal-900">Filter Sweets</h2>
          <button onclick="resetAllFilters()" class="text-xs text-gold-600 font-semibold underline">Reset All</button>
        </div>

        <div class="py-4 border-b border-amber-100">
          <h3 class="text-xs font-bold uppercase text-neutral-500 mb-2.5">Category</h3>
          <div class="space-y-1.5 text-sm">
            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="catFilter" value="all" checked onchange="setCategoryFilter('all')" class="text-royal-800"><span>All Sweets</span></label>
            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="catFilter" value="kaju" onchange="setCategoryFilter('kaju')" class="text-royal-800"><span>Kaju Sweets</span></label>
            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="catFilter" value="ghee" onchange="setCategoryFilter('ghee')" class="text-royal-800"><span>Pure Desi Ghee</span></label>
            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="catFilter" value="chenna" onchange="setCategoryFilter('chenna')" class="text-royal-800"><span>Bengali Chenna</span></label>
            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="catFilter" value="laddus" onchange="setCategoryFilter('laddus')" class="text-royal-800"><span>Laddus & Halwa</span></label>
            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="catFilter" value="dryfruit" onchange="setCategoryFilter('dryfruit')" class="text-royal-800"><span>Dry Fruit / Sugar Free</span></label>
            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="catFilter" value="hampers" onchange="setCategoryFilter('hampers')" class="text-royal-800"><span>Festive Hampers</span></label>
          </div>
        </div>

        <div class="py-4 border-b border-amber-100">
          <h3 class="text-xs font-bold uppercase text-neutral-500 mb-2.5">Highlights</h3>
          <div class="space-y-2 text-sm">
            <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" id="tagGhee" onchange="applyFilters()" class="rounded"><span>Pure Cow Ghee</span></label>
            <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" id="tagBestseller" onchange="applyFilters()" class="rounded"><span>Bestseller</span></label>
            <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" id="tagSugarFree" onchange="applyFilters()" class="rounded"><span>Sugar Free</span></label>
            <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" id="tagVrat" onchange="applyFilters()" class="rounded"><span>Vrat Friendly</span></label>
          </div>
        </div>

        <div class="py-4">
          <div class="flex items-center justify-between mb-2">
            <h3 class="text-xs font-bold uppercase text-neutral-500">Max Budget</h3>
            <span class="text-sm font-bold text-royal-900" id="priceRangeDisplay">₹2000</span>
          </div>
          <input type="range" id="priceRange" min="200" max="2000" step="50" value="2000" class="w-full accent-royal-800" oninput="updatePriceSlider(this.value)"/>
        </div>
      </aside>

      <!-- CATALOG -->
      <section class="flex-1 w-full">
        <div class="bg-white rounded-2xl p-4 shadow-sm border border-amber-200/80 mb-6 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div>
            <h2 class="font-serif font-bold text-xl text-royal-900">
              <span id="catalogCategoryTitle">Traditional Sweets Collection</span>
              <span class="text-xs font-normal text-neutral-500" id="productCountLabel">(12 items)</span>
            </h2>
          </div>
          <select id="sortSelect" onchange="applyFilters()" class="text-xs bg-cream border border-amber-200 rounded-xl px-3 py-2 text-royal-900">
            <option value="featured">Featured</option>
            <option value="price-asc">Price: Low to High</option>
            <option value="price-desc">Price: High to Low</option>
            <option value="rating">Highest Rating</option>
            <option value="name-asc">A - Z</option>
          </select>
        </div>

        <div id="productsGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"></div>

        <div id="emptyCatalogState" class="hidden text-center py-16 bg-white rounded-2xl border border-dashed border-amber-300 p-8">
          <h3 class="font-serif font-bold text-lg text-royal-900">No sweets matched your criteria</h3>
          <button onclick="resetAllFilters()" class="mt-4 bg-royal-800 text-amber-200 text-xs font-bold px-4 py-2 rounded-full">Show All</button>
        </div>
      </section>
    </div>
  </main>

  <!-- FOOTER -->
  <footer class="bg-royal-900 text-amber-100 pt-10 pb-8 border-t-4 border-gold-500">
    <div class="max-w-7xl mx-auto px-4 text-center text-xs">
      <p class="font-serif font-bold text-xl text-white mb-2">BIKANERVALA</p>
      <p class="text-amber-200/70">© 2026 Bikanervala Sweets. All rights reserved.</p>
    </div>
  </footer>

  <!-- CART DRAWER -->
  <div id="cartDrawerBackdrop" class="fixed inset-0 bg-neutral-900/60 z-50 hidden opacity-0 transition-opacity" onclick="toggleCartDrawer(false)"></div>
  <aside id="cartDrawer" class="fixed top-0 right-0 h-full w-full max-w-md bg-white z-50 shadow-2xl flex flex-col transform translate-x-full transition-transform duration-300">
    <div class="p-4 bg-royal-900 text-white flex items-center justify-between border-b border-gold-500/40">
      <div class="flex items-center gap-2">
        <i data-lucide="shopping-bag" class="w-5 h-5 text-gold-400"></i>
        <h3 class="font-serif font-bold">Your Mithai Box</h3>
        <span id="drawerItemCountPill" class="bg-gold-500 text-royal-900 text-xs font-black px-2 py-0.5 rounded-full">0</span>
      </div>
      <button onclick="toggleCartDrawer(false)"><i data-lucide="x" class="w-5 h-5"></i></button>
    </div>

    <div class="bg-amber-50 p-3 border-b border-amber-200">
      <div class="flex justify-between text-xs font-semibold text-royal-900 mb-1.5">
        <span id="freeShippingText">Add ₹999 for FREE Delivery</span>
        <span id="freeShippingPercent" class="text-gold-600 font-bold">0%</span>
      </div>
      <div class="w-full bg-amber-200 rounded-full h-2"><div id="freeShippingBar" class="bg-emerald-600 h-full rounded-full transition-all" style="width:0%"></div></div>
    </div>

    <div id="cartItemsList" class="flex-1 overflow-y-auto p-4 space-y-3.5 divide-y divide-amber-100"></div>

    <div id="emptyCartView" class="hidden flex-1 flex-col items-center justify-center p-6 text-center">
      <i data-lucide="package-open" class="w-12 h-12 text-gold-500 mb-2"></i>
      <h4 class="font-serif font-bold text-royal-900">Your Cart is Empty</h4>
      <p class="text-xs text-neutral-500 mt-1 mb-4">Add some Kaju Katli or warm Gulab Jamuns.</p>
      <button onclick="toggleCartDrawer(false)" class="bg-royal-800 text-amber-200 text-xs font-bold px-5 py-2.5 rounded-full">Explore Sweets</button>
    </div>

    <div id="cartFooterSection" class="p-4 bg-cream border-t border-amber-200 space-y-3">
      <div class="flex gap-2">
        <input type="text" id="couponInput" placeholder="Coupon (DIWALI25)" class="flex-1 text-xs uppercase px-3 py-2 bg-white border border-amber-300 rounded-lg"/>
        <button onclick="applyCouponCode()" class="bg-royal-800 text-amber-200 text-xs font-bold px-3 py-2 rounded-lg">Apply</button>
      </div>
      <div id="couponAppliedMessage" class="hidden text-[11px] text-emerald-700 font-semibold flex items-center justify-between">
        <span id="couponTextLabel"></span>
        <button onclick="removeCoupon()" class="text-rose-600 underline">Remove</button>
      </div>

      <div class="space-y-1 text-xs text-neutral-600 pt-2 border-t border-amber-200/60">
        <div class="flex justify-between"><span>Subtotal</span><span id="cartSubtotal" class="font-semibold">₹0</span></div>
        <div class="flex justify-between text-emerald-700"><span>Discount</span><span id="cartDiscount">-₹0</span></div>
        <div class="flex justify-between"><span>Delivery</span><span id="cartDeliveryCharge" class="font-semibold">₹60</span></div>
        <div class="flex justify-between text-base font-extrabold text-royal-900 pt-1 border-t border-amber-200"><span>Total</span><span id="cartGrandTotal">₹0</span></div>
      </div>

      <button onclick="openCheckoutModal()" class="w-full bg-royal-800 text-amber-200 font-bold py-3 rounded-xl shadow-lg flex items-center justify-center gap-2 text-sm">
        <span>Proceed to Checkout</span><i data-lucide="arrow-right" class="w-4 h-4"></i>
      </button>
    </div>
  </aside>

  <!-- WISHLIST DRAWER -->
  <div id="wishlistDrawerBackdrop" class="fixed inset-0 bg-neutral-900/60 z-50 hidden opacity-0 transition-opacity" onclick="toggleWishlistDrawer(false)"></div>
  <aside id="wishlistDrawer" class="fixed top-0 right-0 h-full w-full max-w-sm bg-white z-50 shadow-2xl flex flex-col transform translate-x-full transition-transform duration-300">
    <div class="p-4 bg-royal-900 text-white flex items-center justify-between">
      <h3 class="font-serif font-bold">Saved Favourites</h3>
      <button onclick="toggleWishlistDrawer(false)"><i data-lucide="x" class="w-5 h-5"></i></button>
    </div>
    <div id="wishlistItemsList" class="flex-1 overflow-y-auto p-4 space-y-3"></div>
  </aside>

  <!-- QUICK VIEW MODAL -->
  <div id="quickViewModal" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
    <div class="bg-white rounded-3xl max-w-3xl w-full overflow-hidden shadow-2xl border border-amber-200">
      <div class="relative" id="quickViewContent"></div>
    </div>
  </div>

  <!-- PINCODE MODAL -->
  <div id="pincodeModal" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
    <div class="bg-white rounded-2xl max-w-sm w-full p-6 shadow-2xl">
      <div class="flex justify-between items-center mb-3">
        <h3 class="font-serif font-bold text-royal-900">Select Pincode</h3>
        <button onclick="closeModal('pincodeModal')"><i data-lucide="x" class="w-4 h-4"></i></button>
      </div>
      <div class="flex gap-2">
        <input type="text" id="pincodeInput" maxlength="6" placeholder="110001" class="w-full text-sm p-2.5 border border-amber-300 rounded-xl text-center font-bold"/>
        <button onclick="verifyPincode()" class="bg-royal-800 text-amber-200 font-bold text-xs px-4 rounded-xl">Check</button>
      </div>
      <div id="pincodeStatus" class="mt-3 text-xs"></div>
    </div>
  </div>

  <!-- TRACK ORDER MODAL -->
  <div id="trackOrderModal" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
    <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl">
      <div class="flex justify-between items-center mb-3">
        <h3 class="font-serif font-bold text-royal-900">Live Order Tracker</h3>
        <button onclick="closeModal('trackOrderModal')"><i data-lucide="x" class="w-4 h-4"></i></button>
      </div>
      <div class="flex gap-2">
        <input type="text" value="BIK-94021" class="w-full text-xs p-2.5 border border-amber-300 rounded-xl uppercase"/>
        <button onclick="openToast('Tracking refreshed!')" class="bg-royal-800 text-amber-200 font-bold text-xs px-4 rounded-xl">Track</button>
      </div>
    </div>
  </div>

  <!-- CHECKOUT MODAL -->
  <div id="checkoutModal" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm overflow-y-auto">
    <div class="bg-white rounded-3xl max-w-2xl w-full p-6 shadow-2xl my-8">
      <div class="flex justify-between items-center pb-4 border-b border-amber-100">
        <h3 class="font-serif font-bold text-lg text-royal-900">Express Checkout</h3>
        <button onclick="closeModal('checkoutModal')"><i data-lucide="x" class="w-5 h-5"></i></button>
      </div>
      <form onsubmit="handleOrderSubmission(event)" class="mt-4 space-y-4">
        <div>
          <h4 class="text-xs font-bold uppercase text-royal-900 mb-2">Delivery Address</h4>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
            <input type="text" required placeholder="Full Name" value="Aarav Sharma" class="p-2.5 border border-amber-200 rounded-lg"/>
            <input type="tel" required placeholder="Mobile" value="9811223344" class="p-2.5 border border-amber-200 rounded-lg"/>
            <input type="text" required placeholder="Address" value="Flat 402, Royal Palms" class="sm:col-span-2 p-2.5 border border-amber-200 rounded-lg"/>
            <input type="text" required placeholder="City" value="New Delhi" class="p-2.5 border border-amber-200 rounded-lg"/>
            <input type="text" required placeholder="Pincode" value="110001" class="p-2.5 border border-amber-200 rounded-lg"/>
          </div>
        </div>
        <div>
          <h4 class="text-xs font-bold uppercase text-royal-900 mb-2">Payment Method</h4>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-xs">
            <label class="border-2 border-amber-300 bg-amber-50/50 p-3 rounded-xl flex items-center gap-2 cursor-pointer">
              <input type="radio" name="paymethod" checked class="text-royal-800"/>
              <span class="font-bold text-royal-900">UPI</span>
            </label>
            <label class="border border-amber-200 p-3 rounded-xl flex items-center gap-2 cursor-pointer">
              <input type="radio" name="paymethod" class="text-royal-800"/>
              <span class="font-bold text-royal-900">Card</span>
            </label>
            <label class="border border-amber-200 p-3 rounded-xl flex items-center gap-2 cursor-pointer">
              <input type="radio" name="paymethod" class="text-royal-800"/>
              <span class="font-bold text-royal-900">COD</span>
            </label>
          </div>
        </div>
        <div class="bg-cream p-3 rounded-xl border border-amber-200 flex justify-between items-center text-xs">
          <span class="text-neutral-500">Total Payable:</span>
          <span class="text-base font-black text-royal-900" id="checkoutFinalAmount">₹0</span>
        </div>
        <button type="submit" class="w-full bg-royal-800 text-amber-200 font-bold py-3.5 rounded-xl text-sm shadow-xl flex items-center justify-center gap-2">
          <i data-lucide="lock" class="w-4 h-4"></i> Place Order
        </button>
      </form>
    </div>
  </div>

  <!-- ORDER SUCCESS MODAL -->
  <div id="orderSuccessModal" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
    <div class="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl border-2 border-gold-500 text-center">
      <div class="w-16 h-16 bg-emerald-100 text-emerald-700 rounded-full flex items-center justify-center mx-auto mb-3">
        <i data-lucide="check-circle" class="w-9 h-9"></i>
      </div>
      <h3 class="font-serif font-extrabold text-2xl text-royal-900">Mithai Mubarak!</h3>
      <p class="text-xs text-neutral-600 mt-1">Your order has been received.</p>
      <div class="my-4 bg-cream p-3 rounded-2xl border border-amber-200 text-xs text-left space-y-1.5">
        <div class="flex justify-between"><span class="text-neutral-500">Order ID:</span><span class="font-bold text-royal-900" id="successOrderId">BIK-84920</span></div>
        <div class="flex justify-between pt-1 border-t border-amber-200 font-bold text-royal-900"><span>Amount Paid:</span><span id="successOrderAmount">₹0</span></div>
      </div>
      <button onclick="closeModal('orderSuccessModal')" class="w-full bg-royal-800 text-amber-200 font-bold py-2.5 rounded-xl text-xs">Continue Shopping</button>
    </div>
  </div>

  <!-- TOASTS -->
  <div id="toastContainer" class="fixed bottom-5 right-5 z-50 flex flex-col gap-2 pointer-events-none"></div>

  <!-- ================= JAVASCRIPT ================= -->
  <script>
    /* ====== PRODUCTS FROM BACKEND ====== */
    const SWEETS_DATABASE = {{ products|tojson }};
    let cart = {{ cart|tojson }};
    let wishlist = {{ wishlist|tojson }};
    let currentCategory = 'all';
    let searchQuery = '';
    let maxPrice = 2000;
    let selectedVariantsMap = {};
    let appliedCoupon = null;

    SWEETS_DATABASE.forEach(item => { selectedVariantsMap[item.id] = 0; });

    /* ====== RENDER CATALOG ====== */
    function renderCatalog() {
      const grid = document.getElementById('productsGrid');
      const emptyState = document.getElementById('emptyCatalogState');
      const sortVal = document.getElementById('sortSelect').value;
      const tagGhee = document.getElementById('tagGhee').checked;
      const tagBestseller = document.getElementById('tagBestseller').checked;
      const tagSugarFree = document.getElementById('tagSugarFree').checked;
      const tagVrat = document.getElementById('tagVrat').checked;

      let filtered = SWEETS_DATABASE.filter(item => {
        if (currentCategory !== 'all' && item.category !== currentCategory) return false;
        if (searchQuery.trim() !== '') {
          const q = searchQuery.toLowerCase();
          if (!item.name.toLowerCase().includes(q) && !item.hindiName.includes(searchQuery) && !item.description.toLowerCase().includes(q)) return false;
        }
        const activeVariant = item.variants[selectedVariantsMap[item.id] || 0];
        if (activeVariant.price > maxPrice) return false;
        if (tagGhee && !item.isGhee) return false;
        if (tagBestseller && item.badge !== 'Bestseller') return false;
        if (tagSugarFree && !item.isSugarFree) return false;
        if (tagVrat && !item.isVrat) return false;
        return true;
      });

      if (sortVal === 'price-asc') filtered.sort((a,b) => a.variants[selectedVariantsMap[a.id]||0].price - b.variants[selectedVariantsMap[b.id]||0].price);
      else if (sortVal === 'price-desc') filtered.sort((a,b) => b.variants[selectedVariantsMap[b.id]||0].price - a.variants[selectedVariantsMap[a.id]||0].price);
      else if (sortVal === 'rating') filtered.sort((a,b) => b.rating - a.rating);
      else if (sortVal === 'name-asc') filtered.sort((a,b) => a.name.localeCompare(b.name));

      document.getElementById('productCountLabel').innerText = `(${filtered.length} items)`;

      if (filtered.length === 0) {
        grid.innerHTML = '';
        emptyState.classList.remove('hidden');
        return;
      }
      emptyState.classList.add('hidden');

      grid.innerHTML = filtered.map(item => {
        const selectedIdx = selectedVariantsMap[item.id] || 0;
        const currentVariant = item.variants[selectedIdx];
        const isWishlisted = wishlist.includes(item.id);
        const cartQty = getCartItemQuantity(item.id, currentVariant.weight);

        return `
          <div class="bg-cardbg rounded-2xl overflow-hidden border border-amber-200/90 shadow-sm hover:shadow-xl transition-all flex flex-col group relative">
            <div class="relative overflow-hidden bg-amber-50 h-52">
              <img src="${item.image}" alt="${item.name}" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
              <div class="absolute top-3 left-3 flex flex-col gap-1">
                <span class="${item.badgeColor} text-white text-[10px] font-bold px-2.5 py-0.5 rounded-full uppercase">${item.badge}</span>
                ${item.isGhee ? '<span class="bg-amber-100/90 text-royal-900 border border-amber-300 text-[10px] font-bold px-2 py-0.5 rounded">Pure Ghee</span>' : ''}
              </div>
              <div class="absolute top-3 right-3 flex flex-col gap-2 items-center">
                <div class="veg-symbol bg-white shadow-sm"><div class="veg-dot"></div></div>
                <button onclick="toggleWishlist(${item.id})" class="w-8 h-8 rounded-full bg-white/90 flex items-center justify-center shadow-md ${isWishlisted ? 'text-rose-600' : 'text-neutral-500'}">
                  <i data-lucide="heart" class="w-4 h-4 ${isWishlisted ? 'fill-rose-600' : ''}"></i>
                </button>
              </div>
              <div class="absolute bottom-3 left-3 right-3 opacity-0 group-hover:opacity-100 transition-all">
                <button onclick="quickView(${item.id})" class="w-full bg-white/95 text-royal-900 text-xs font-bold py-2 rounded-xl shadow-lg hover:bg-gold-500">
                  Quick View
                </button>
              </div>
            </div>

            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between text-xs mb-1.5">
                  <span class="text-[11px] font-semibold text-gold-700 font-serif">${item.hindiName}</span>
                  <div class="flex items-center gap-1 bg-amber-50 px-2 py-0.5 rounded border border-amber-200/60">
                    <span class="text-amber-500 text-xs">★</span>
                    <span class="font-bold text-royal-900 text-[11px]">${item.rating}</span>
                  </div>
                </div>
                <h3 class="font-serif font-bold text-base text-royal-900 leading-snug">${item.name}</h3>
                <p class="text-xs text-neutral-500 mt-1 line-clamp-2">${item.description}</p>

                <div class="mt-3">
                  <span class="text-[10px] uppercase font-bold text-neutral-400 block mb-1">Select Weight:</span>
                  <div class="flex flex-wrap gap-1.5">
                    ${item.variants.map((v, idx) => `
                      <button onclick="setVariant(${item.id}, ${idx})" class="text-xs px-2.5 py-1 rounded-lg border font-medium ${selectedIdx === idx ? 'bg-royal-900 text-amber-200 border-royal-900 font-bold' : 'bg-white text-neutral-700 border-amber-200'}">${v.weight}</button>
                    `).join('')}
                  </div>
                </div>
              </div>

              <div class="pt-4 mt-3 border-t border-amber-100 flex items-center justify-between gap-2">
                <div>
                  <div class="flex items-baseline gap-1.5">
                    <span class="font-serif font-black text-lg text-royal-900">₹${currentVariant.price}</span>
                    <span class="text-xs text-neutral-400 line-through">₹${currentVariant.originalPrice}</span>
                  </div>
                </div>
                <div>
                  ${cartQty === 0 ? `
                    <button onclick="addToCart(${item.id}, ${selectedIdx})" class="bg-royal-800 hover:bg-royal-700 text-amber-200 px-3.5 py-2 rounded-xl text-xs font-bold flex items-center gap-1.5">
                      <i data-lucide="plus" class="w-3.5 h-3.5"></i> Add
                    </button>
                  ` : `
                    <div class="flex items-center bg-royal-900 text-amber-200 rounded-xl text-xs font-bold">
                      <button onclick="updateCartItemQty(${item.id}, '${currentVariant.weight}', -1)" class="px-2.5 py-1.5">-</button>
                      <span class="px-2 text-white font-black">${cartQty}</span>
                      <button onclick="updateCartItemQty(${item.id}, '${currentVariant.weight}', 1)" class="px-2.5 py-1.5">+</button>
                    </div>
                  `}
                </div>
              </div>
            </div>
          </div>
        `;
      }).join('');
      lucide.createIcons();
    }

    function setVariant(productId, variantIdx) {
      selectedVariantsMap[productId] = variantIdx;
      renderCatalog();
    }

    /* ====== CART ====== */
    async function addToCart(productId, variantIndex = null) {
      const sweet = SWEETS_DATABASE.find(s => s.id === productId);
      if (!sweet) return;
      const vIdx = (variantIndex !== null) ? variantIndex : (selectedVariantsMap[productId] || 0);
      const variant = sweet.variants[vIdx];

      const res = await fetch('/api/cart/add', {
        method: 'POST', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({id: sweet.id, name: sweet.name, hindiName: sweet.hindiName, image: sweet.image, weight: variant.weight, price: variant.price, quantity: 1})
      });
      const data = await res.json();
      cart = data.cart;
      openToast(`Added "${sweet.name} (${variant.weight})" to cart!`);
      updateCartUI();
      renderCatalog();
    }

    async function updateCartItemQty(productId, weight, change) {
      const res = await fetch('/api/cart/update', {
        method: 'POST', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({id: productId, weight: weight, change: change})
      });
      const data = await res.json();
      cart = data.cart;
      if (data.removed) openToast('Item removed from cart');
      updateCartUI();
      renderCatalog();
    }

    async function removeCartLine(index) {
      const res = await fetch('/api/cart/remove', {
        method: 'POST', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({index: index})
      });
      const data = await res.json();
      cart = data.cart;
      openToast('Item removed');
      updateCartUI();
      renderCatalog();
    }

    function getCartItemQuantity(productId, weight) {
      const item = cart.find(c => c.id === productId && c.weight === weight);
      return item ? item.quantity : 0;
    }

    function updateCartUI() {
      const listEl = document.getElementById('cartItemsList');
      const emptyView = document.getElementById('emptyCartView');
      const footerSection = document.getElementById('cartFooterSection');

      const totalItems = cart.reduce((acc, curr) => acc + curr.quantity, 0);
      const subtotal = cart.reduce((acc, curr) => acc + (curr.price * curr.quantity), 0);

      document.getElementById('cartCountBadge').innerText = totalItems;
      document.getElementById('drawerItemCountPill').innerText = totalItems;
      document.getElementById('cartTotalHeader').innerText = `₹${subtotal}`;

      if (cart.length === 0) {
        listEl.innerHTML = '';
        emptyView.classList.remove('hidden');
        emptyView.classList.add('flex');
        footerSection.classList.add('hidden');
      } else {
        emptyView.classList.add('hidden');
        emptyView.classList.remove('flex');
        footerSection.classList.remove('hidden');

        listEl.innerHTML = cart.map((item, index) => `
          <div class="flex items-center gap-3 pt-3 first:pt-0">
            <img src="${item.image}" class="w-16 h-16 rounded-xl object-cover border border-amber-200"/>
            <div class="flex-1 min-w-0">
              <h4 class="text-xs font-bold text-royal-900 truncate">${item.name}</h4>
              <span class="text-[11px] text-gold-700 font-semibold block">${item.weight} • ₹${item.price}</span>
              <div class="flex items-center gap-2 mt-1.5">
                <div class="flex items-center bg-cream border border-amber-300 rounded-lg text-xs font-bold">
                  <button onclick="updateCartItemQty(${item.id}, '${item.weight}', -1)" class="px-2 py-0.5 text-royal-900">-</button>
                  <span class="px-2 text-royal-900 font-extrabold text-[11px]">${item.quantity}</span>
                  <button onclick="updateCartItemQty(${item.id}, '${item.weight}', 1)" class="px-2 py-0.5 text-royal-900">+</button>
                </div>
                <span class="text-xs font-extrabold text-royal-900">₹${item.price * item.quantity}</span>
              </div>
            </div>
            <button onclick="removeCartLine(${index})" class="text-neutral-400 hover:text-rose-600"><i data-lucide="trash-2" class="w-4 h-4"></i></button>
          </div>
        `).join('');
      }

      const goal = 999;
      const percent = Math.min(100, Math.round((subtotal / goal) * 100));
      document.getElementById('freeShippingBar').style.width = `${percent}%`;
      document.getElementById('freeShippingPercent').innerText = `${percent}%`;
      let deliveryFee = 60;
      if (subtotal >= goal || subtotal === 0) {
        deliveryFee = 0;
        document.getElementById('freeShippingText').innerText = subtotal === 0 ? "Add ₹999 for FREE Delivery" : "🎉 Free Delivery Unlocked!";
      } else {
        document.getElementById('freeShippingText').innerText = `Add ₹${goal - subtotal} more for FREE Delivery`;
      }

      let discount = 0;
      if (appliedCoupon && subtotal > 0) discount = Math.round(subtotal * (appliedCoupon.discountPercent / 100));
      const grandTotal = Math.max(0, subtotal - discount + deliveryFee);

      document.getElementById('cartSubtotal').innerText = `₹${subtotal}`;
      document.getElementById('cartDiscount').innerText = `-₹${discount}`;
      document.getElementById('cartDeliveryCharge').innerText = deliveryFee === 0 ? 'FREE' : `₹${deliveryFee}`;
      document.getElementById('cartGrandTotal').innerText = `₹${grandTotal}`;
      document.getElementById('checkoutFinalAmount').innerText = `₹${grandTotal}`;
      lucide.createIcons();
    }

    function toggleCartDrawer(open) {
      const drawer = document.getElementById('cartDrawer');
      const backdrop = document.getElementById('cartDrawerBackdrop');
      if (open) {
        backdrop.classList.remove('hidden');
        setTimeout(() => backdrop.classList.remove('opacity-0'), 10);
        drawer.classList.remove('translate-x-full');
      } else {
        drawer.classList.add('translate-x-full');
        backdrop.classList.add('opacity-0');
        setTimeout(() => backdrop.classList.add('hidden'), 300);
      }
    }

    /* ====== COUPON ====== */
    function applyCouponCode() {
      const code = document.getElementById('couponInput').value.trim().toUpperCase();
      if (code === 'DIWALI25') {
        appliedCoupon = { code: 'DIWALI25', discountPercent: 15 };
        document.getElementById('couponAppliedMessage').classList.remove('hidden');
        document.getElementById('couponTextLabel').innerText = 'DIWALI25 Applied (15% off)';
        openToast('15% coupon applied!');
      } else if (code === 'SWEET10') {
        appliedCoupon = { code: 'SWEET10', discountPercent: 10 };
        document.getElementById('couponAppliedMessage').classList.remove('hidden');
        document.getElementById('couponTextLabel').innerText = 'SWEET10 Applied (10% off)';
        openToast('10% coupon applied!');
      } else {
        openToast('Invalid code. Try DIWALI25 or SWEET10');
      }
      updateCartUI();
    }

    function quickApplyCoupon(code) {
      document.getElementById('couponInput').value = code;
      applyCouponCode();
      toggleCartDrawer(true);
    }

    function removeCoupon() {
      appliedCoupon = null;
      document.getElementById('couponInput').value = '';
      document.getElementById('couponAppliedMessage').classList.add('hidden');
      openToast('Coupon removed');
      updateCartUI();
    }

    /* ====== WISHLIST ====== */
    async function toggleWishlist(productId) {
      const res = await fetch('/api/wishlist/toggle', {
        method: 'POST', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({id: productId})
      });
      const data = await res.json();
      wishlist = data.wishlist;
      const sweet = SWEETS_DATABASE.find(s => s.id === productId);
      openToast(data.added ? `Added ${sweet.name} to Wishlist ❤️` : `Removed from Wishlist`);
      updateWishlistBadge();
      renderCatalog();
      renderWishlistDrawer();
    }

    function updateWishlistBadge() {
      const badge = document.getElementById('wishlistCountBadge');
      badge.innerText = wishlist.length;
      badge.classList.toggle('hidden', wishlist.length === 0);
    }

    function openWishlistDrawer() {
      renderWishlistDrawer();
      const drawer = document.getElementById('wishlistDrawer');
      const backdrop = document.getElementById('wishlistDrawerBackdrop');
      backdrop.classList.remove('hidden');
      setTimeout(() => backdrop.classList.remove('opacity-0'), 10);
      drawer.classList.remove('translate-x-full');
    }

    function toggleWishlistDrawer(open) {
      const drawer = document.getElementById('wishlistDrawer');
      const backdrop = document.getElementById('wishlistDrawerBackdrop');
      if (open) {
        backdrop.classList.remove('hidden');
        setTimeout(() => backdrop.classList.remove('opacity-0'), 10);
        drawer.classList.remove('translate-x-full');
      } else {
        drawer.classList.add('translate-x-full');
        backdrop.classList.add('opacity-0');
        setTimeout(() => backdrop.classList.add('hidden'), 300);
      }
    }

    function renderWishlistDrawer() {
      const container = document.getElementById('wishlistItemsList');
      if (wishlist.length === 0) {
        container.innerHTML = `<div class="text-center py-12"><i data-lucide="heart" class="w-10 h-10 text-neutral-300 mx-auto mb-2"></i><p class="text-xs text-neutral-500">No favourites yet!</p></div>`;
        lucide.createIcons();
        return;
      }
      const items = SWEETS_DATABASE.filter(s => wishlist.includes(s.id));
      container.innerHTML = items.map(item => `
        <div class="flex items-center gap-3 p-2 bg-cream rounded-xl border border-amber-200">
          <img src="${item.image}" class="w-14 h-14 rounded-lg object-cover"/>
          <div class="flex-1 min-w-0">
            <h4 class="text-xs font-bold text-royal-900 truncate">${item.name}</h4>
            <span class="text-xs text-gold-700 font-extrabold">From ₹${item.variants[0].price}</span>
          </div>
          <div class="flex flex-col gap-1">
            <button onclick="addToCart(${item.id}, 0)" class="bg-royal-800 text-amber-200 text-[10px] font-bold px-2.5 py-1 rounded-md">Add</button>
            <button onclick="toggleWishlist(${item.id})" class="text-[10px] text-neutral-400 hover:text-rose-600">Remove</button>
          </div>
        </div>
      `).join('');
      lucide.createIcons();
    }

    /* ====== QUICK VIEW ====== */
    function quickView(productId) {
      const item = SWEETS_DATABASE.find(s => s.id === productId);
      if (!item) return;
      const activeIdx = selectedVariantsMap[productId] || 0;
      const activeVariant = item.variants[activeIdx];

      document.getElementById('quickViewContent').innerHTML = `
        <button onclick="closeModal('quickViewModal')" class="absolute top-4 right-4 z-10 w-8 h-8 rounded-full bg-white/90 flex items-center justify-center shadow"><i data-lucide="x" class="w-5 h-5"></i></button>
        <div class="grid grid-cols-1 md:grid-cols-2">
          <div class="h-64 md:h-full bg-amber-50"><img src="${item.image}" class="w-full h-full object-cover"/></div>
          <div class="p-6 flex flex-col justify-between">
            <div>
              <span class="font-serif font-bold text-gold-700 text-xs">${item.hindiName}</span>
              <h2 class="font-serif font-bold text-2xl text-royal-900">${item.name}</h2>
              <div class="flex items-center gap-2 mt-1 text-xs"><span class="text-amber-500 font-bold">★ ${item.rating}</span><span class="text-neutral-400">(${item.reviews} reviews)</span></div>
              <p class="text-xs text-neutral-600 mt-3">${item.description}</p>
              <div class="mt-4 bg-cream p-3 rounded-xl border border-amber-200 text-xs space-y-1">
                <div><strong>Ingredients:</strong> ${item.ingredients}</div>
                <div><strong>Shelf Life:</strong> ${item.shelfLife}</div>
              </div>
              <div class="mt-4">
                <label class="block text-xs font-bold text-neutral-700 mb-1.5">Weights:</label>
                <div class="flex gap-2">
                  ${item.variants.map((v, i) => `<button onclick="setVariant(${item.id}, ${i}); quickView(${item.id});" class="text-xs px-3 py-1.5 rounded-lg border font-medium ${activeIdx === i ? 'bg-royal-900 text-amber-200 border-royal-900 font-bold' : 'border-amber-200 text-neutral-700'}">${v.weight}</button>`).join('')}
                </div>
              </div>
            </div>
            <div class="pt-6 mt-6 border-t border-amber-100 flex items-center justify-between gap-4">
              <div>
                <span class="text-xs text-neutral-400 block">Price</span>
                <div class="flex items-baseline gap-2">
                  <span class="font-serif font-black text-2xl text-royal-900">₹${activeVariant.price}</span>
                  <span class="text-xs text-neutral-400 line-through">₹${activeVariant.originalPrice}</span>
                </div>
              </div>
              <div class="flex gap-2">
                <button onclick="addToCart(${item.id}, ${activeIdx}); closeModal('quickViewModal');" class="bg-royal-800 text-amber-200 font-bold text-xs px-5 py-3 rounded-xl">Add to Box</button>
              </div>
            </div>
          </div>
        </div>
      `;
      openModal('quickViewModal');
      lucide.createIcons();
    }

    /* ====== FILTERS ====== */
    function setCategoryFilter(cat) {
      currentCategory = cat;
      const radio = document.querySelector(`input[name="catFilter"][value="${cat}"]`);
      if (radio) radio.checked = true;
      const titles = {all:'Traditional Sweets Collection',kaju:'Kaju Delights',ghee:'Pure Desi Ghee Classics',chenna:'Bengali & Chenna Treats',laddus:'Laddus & Halwa',dryfruit:'Dry Fruit & Sugar Free',hampers:'Festive Hampers'};
      document.getElementById('catalogCategoryTitle').innerText = titles[cat] || 'Sweets';
      renderCatalog();
    }
    function updatePriceSlider(val) {
      maxPrice = parseInt(val, 10);
      document.getElementById('priceRangeDisplay').innerText = `₹${maxPrice}`;
      renderCatalog();
    }
    function applyFilters() { renderCatalog(); }
    function resetAllFilters() {
      currentCategory = 'all'; searchQuery = ''; maxPrice = 2000;
      document.getElementById('searchInput').value = '';
      document.getElementById('priceRange').value = 2000;
      document.getElementById('priceRangeDisplay').innerText = '₹2000';
      ['tagGhee','tagBestseller','tagSugarFree','tagVrat'].forEach(id => document.getElementById(id).checked = false);
      document.getElementById('sortSelect').value = 'featured';
      document.querySelector('input[name="catFilter"][value="all"]').checked = true;
      document.getElementById('catalogCategoryTitle').innerText = 'Traditional Sweets Collection';
      renderCatalog();
      openToast('Filters reset');
    }

    /* ====== SEARCH ====== */
    function handleSearch(val) {
      searchQuery = val;
      const clearBtn = document.getElementById('clearSearchBtn');
      const dropdown = document.getElementById('searchDropdown');
      if (val.trim().length > 0) {
        clearBtn.classList.remove('hidden');
        const matches = SWEETS_DATABASE.filter(s => s.name.toLowerCase().includes(val.toLowerCase()) || s.hindiName.includes(val)).slice(0, 4);
        if (matches.length > 0) {
          dropdown.classList.remove('hidden');
          dropdown.innerHTML = matches.map(m => `
            <div onclick="selectSearchSuggestion('${m.name}')" class="flex items-center gap-3 p-2 hover:bg-cream rounded-xl cursor-pointer">
              <img src="${m.image}" class="w-10 h-10 rounded-lg object-cover"/>
              <div class="flex-1 min-w-0"><p class="text-xs font-bold text-royal-900">${m.name}</p><p class="text-[10px] text-neutral-500">From ₹${m.variants[0].price}</p></div>
            </div>
          `).join('');
        } else dropdown.classList.add('hidden');
      } else {
        clearBtn.classList.add('hidden');
        dropdown.classList.add('hidden');
      }
      renderCatalog();
    }
    function selectSearchSuggestion(name) {
      document.getElementById('searchInput').value = name;
      searchQuery = name;
      document.getElementById('searchDropdown').classList.add('hidden');
      renderCatalog();
    }
    function clearSearch() {
      document.getElementById('searchInput').value = '';
      searchQuery = '';
      document.getElementById('clearSearchBtn').classList.add('hidden');
      document.getElementById('searchDropdown').classList.add('hidden');
      renderCatalog();
    }

    /* ====== CHECKOUT ====== */
    function openCheckoutModal() {
      if (cart.length === 0) { openToast('Cart is empty!'); return; }
      toggleCartDrawer(false);
      openModal('checkoutModal');
    }

    async function handleOrderSubmission(e) {
      e.preventDefault();
      const res = await fetch('/api/checkout', {method: 'POST'});
      const data = await res.json();
      closeModal('checkoutModal');
      document.getElementById('successOrderId').innerText = data.order_id;
      document.getElementById('successOrderAmount').innerText = '₹' + data.total;
      confetti({particleCount: 90, spread: 80, origin: {y: 0.6}, colors: ['#DCA524','#7B111F','#16a34a','#F59E0B']});
      cart = [];
      updateCartUI();
      renderCatalog();
      openModal('orderSuccessModal');
    }

    /* ====== UTILITIES ====== */
    function openModal(id) { document.getElementById(id).classList.remove('hidden'); lucide.createIcons(); }
    function closeModal(id) { document.getElementById(id).classList.add('hidden'); }

    function verifyPincode() {
      const pin = document.getElementById('pincodeInput').value.trim();
      const status = document.getElementById('pincodeStatus');
      if (pin.length !== 6 || isNaN(pin)) {
        status.innerHTML = `<span class="text-rose-600 font-bold">Enter valid 6-digit pincode.</span>`;
        return;
      }
      status.innerHTML = `<div class="p-2.5 bg-emerald-50 border border-emerald-200 rounded-lg text-emerald-800 font-medium">✓ Pincode ${pin} eligible for express delivery!</div>`;
      document.getElementById('currentPincodeLabel').innerText = `Deliver to: ${pin}`;
      setTimeout(() => { closeModal('pincodeModal'); openToast(`Pincode set: ${pin}`); }, 1200);
    }

    function openToast(message) {
      const container = document.getElementById('toastContainer');
      const toast = document.createElement('div');
      toast.className = "bg-royal-900 text-amber-200 border border-gold-500/60 shadow-2xl px-4 py-3 rounded-2xl text-xs font-semibold flex items-center gap-2 transform transition-all duration-300 translate-y-5 opacity-0";
      toast.innerHTML = `<div class="veg-symbol"><div class="veg-dot"></div></div><span>${message}</span>`;
      container.appendChild(toast);
      setTimeout(() => toast.classList.remove('translate-y-5', 'opacity-0'), 10);
      setTimeout(() => { toast.classList.add('opacity-0', 'translate-y-2'); setTimeout(() => toast.remove(), 300); }, 3500);
    }

    /* ====== STARTUP ====== */
    window.addEventListener('DOMContentLoaded', () => {
      renderCatalog();
      updateCartUI();
      updateWishlistBadge();
      lucide.createIcons();
    });
  </script>
</body>
</html>
"""

# ================= ROUTES =================
@app.route('/')
def index():
    cart = session.get('cart', [])
    wishlist = session.get('wishlist', [])
    return render_template_string(HTML_PAGE, products=SWEETS_DATABASE, cart=cart, wishlist=wishlist)

@app.route('/api/cart/add', methods=['POST'])
def api_cart_add():
    data = request.json
    cart = session.get('cart', [])
    for item in cart:
        if item['id'] == data['id'] and item['weight'] == data['weight']:
            item['quantity'] += 1
            session['cart'] = cart
            return jsonify({'cart': cart})
    cart.append(data)
    session['cart'] = cart
    return jsonify({'cart': cart})

@app.route('/api/cart/update', methods=['POST'])
def api_cart_update():
    data = request.json
    cart = session.get('cart', [])
    removed = False
    for i, item in enumerate(cart):
        if item['id'] == data['id'] and item['weight'] == data['weight']:
            item['quantity'] += data['change']
            if item['quantity'] <= 0:
                cart.pop(i)
                removed = True
            break
    session['cart'] = cart
    return jsonify({'cart': cart, 'removed': removed})

@app.route('/api/cart/remove', methods=['POST'])
def api_cart_remove():
    data = request.json
    cart = session.get('cart', [])
    if 0 <= data['index'] < len(cart):
        cart.pop(data['index'])
    session['cart'] = cart
    return jsonify({'cart': cart})

@app.route('/api/wishlist/toggle', methods=['POST'])
def api_wishlist_toggle():
    data = request.json
    wishlist = session.get('wishlist', [])
    if data['id'] in wishlist:
        wishlist.remove(data['id'])
        added = False
    else:
        wishlist.append(data['id'])
        added = True
    session['wishlist'] = wishlist
    return jsonify({'wishlist': wishlist, 'added': added})

@app.route('/api/checkout', methods=['POST'])
def api_checkout():
    cart = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart)
    delivery = 0 if total >= 999 else 60
    grand_total = total + delivery
    order_id = 'BIK-' + str(random.randint(10000, 99999))
    session['cart'] = []
    return jsonify({'order_id': order_id, 'total': grand_total})

# ================= RUN =================
if __name__ == '__main__':
    print("\n" + "="*50)
    print("🍬 BIKANERVALA WEBSITE STARTED!")
    print("="*50)
    print("📱 Same phone:  http://127.0.0.1:8080")
    print("💻 Same WiFi:   http://<phone-IP>:8080")
    print("="*50 + "\n")
    app.run(host='0.0.0.0', port=8080, debug=False)
