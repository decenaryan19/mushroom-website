#!/usr/bin/env python3
"""Generate optimized subpages with shared layout."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"

HEAD = """  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#3d7a3d">
  <link rel="preload" href="../css/styles.css" as="style">
  <link rel="stylesheet" href="../css/styles.css">"""

HEADER = """
  <header class="site-header">
    <div class="container site-header__inner">
      <a href="../index.html" class="site-logo" aria-label="Suwannee Bell Farms — Home">
        <img src="../images/logo.webp" alt="Suwannee Bell Farms logo" width="52" height="52" decoding="async">
      </a>
      <nav class="site-nav" aria-label="Main navigation">
        <a href="../index.html"{home_active}>HOME</a>
        <a href="product.html"{product_active}>PRODUCT</a>
        <a href="articles.html"{articles_active}>ARTICLES</a>
        <a href="about.html"{about_active}>ABOUT</a>
        <a href="sample.html"{sample_active}>REQUEST FREE SAMPLE</a>
        <a href="contact.html"{contact_active}>CONTACT</a>
      </nav>
      <div class="site-header__actions">
        <button type="button" class="icon-btn" aria-label="Search">
          <svg aria-hidden="true" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        </button>
        <button type="button" id="mobile-menu-btn" class="icon-btn" aria-label="Open menu" aria-expanded="false">
          <svg aria-hidden="true" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
        </button>
      </div>
    </div>
    <nav id="mobile-menu" class="mobile-nav" aria-label="Mobile navigation">
      <div class="mobile-nav__inner">
        <a href="../index.html"{home_m_active}>HOME</a>
        <a href="product.html"{product_m_active}>PRODUCT</a>
        <a href="articles.html"{articles_m_active}>ARTICLES</a>
        <a href="about.html"{about_m_active}>ABOUT</a>
        <a href="sample.html"{sample_m_active}>REQUEST FREE SAMPLE</a>
        <a href="contact.html"{contact_m_active}>CONTACT</a>
      </div>
    </nav>
  </header>"""

FOOTER = """
  <footer class="site-footer">
    <div class="container site-footer__main">
      <div class="footer-grid">
        <div>
          <h4 class="footer-heading">Quick Links</h4>
          <ul class="footer-links">
            <li><a href="../index.html" class="footer-link">Home</a></li>
            <li><a href="product.html" class="footer-link">Product</a></li>
            <li><a href="about.html" class="footer-link">About</a></li>
            <li><a href="contact.html" class="footer-link">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Useful Info</h4>
          <ul class="footer-links">
            <li><a href="sample.html" class="footer-link">FAQ</a></li>
            <li><a href="articles.html" class="footer-link">Articles</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Contact Us</h4>
          <ul class="footer-links">
            <li>Phone: <a href="tel:+13525594295" class="footer-link">(352) 559-4295</a></li>
            <li>Email: <a href="mailto:sales@suwanneebellfarms.com" class="footer-link">sales@suwanneebellfarms.com</a></li>
            <li>Web: <a href="https://suwanneebellfarms.com" class="footer-link">suwanneebellfarms.com</a></li>
            <li>1509 SW 22 Ct. Bell, Florida 32619</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="site-footer__bar">
      <div class="container footer-bar-inner">
        <p class="footer-copy">Copyright 2026 &copy; Suwannee Bell Farms LLC</p>
        <div class="payment-badges" aria-label="Accepted payment methods">
          <span class="payment-badge">VISA</span>
          <span class="payment-badge">MC</span>
          <span class="payment-badge">AMEX</span>
          <span class="payment-badge">PayPal</span>
        </div>
        <button type="button" id="back-to-top" class="back-to-top" aria-label="Back to top">
          <svg aria-hidden="true" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7"/></svg>
        </button>
      </div>
    </div>
  </footer>
  <script src="../js/script.js" defer></script>"""


def active(page, name):
    return ' class="is-active"' if page == name else ""


def layout(page, title, description, main):
    nav = {
        "home_active": active(page, "home"),
        "product_active": active(page, "product"),
        "articles_active": active(page, "articles"),
        "about_active": active(page, "about"),
        "sample_active": active(page, "sample"),
        "contact_active": active(page, "contact"),
        "home_m_active": active(page, "home"),
        "product_m_active": active(page, "product"),
        "articles_m_active": active(page, "articles"),
        "about_m_active": active(page, "about"),
        "sample_m_active": active(page, "sample"),
        "contact_m_active": active(page, "contact"),
    }
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD.format(title=title, description=description)}
</head>
<body>
{HEADER.format(**nav)}
  <main>
{main}
  </main>
{FOOTER}
</body>
</html>
"""


ARTICLES = [
    ("article-1.webp", "Grilled mushroom skewers on a wooden board", "Shiitake Mushrooms as a Meat Alternative"),
    ("article-2.webp", "Hands holding freshly harvested shiitake mushrooms", "The History of Shiitake Mushrooms"),
    ("article-3.webp", "Nutritious vegan bowl with shiitake mushrooms", "A Delicious and Nutritious Vegan Choice"),
    ("article-4.webp", "Fresh shiitake mushrooms on a wooden table", "Best Way to Eat Shiitake Mushrooms Raw"),
    ("article-5.webp", "Sun dried shiitake mushrooms in a glass jar", "Sun Dried Shiitake Mushrooms for Convenience Flavor and Nutrition"),
    ("article-6.webp", "Wild mushrooms growing on a mossy log", "Why It Is Beneficial to Support Sustainable Forests"),
    ("article-7.webp", "Freshly harvested shiitake mushrooms", "Why You Should Buy Fresh Locally Sourced and Sustainable Organic Shiitake Mushrooms"),
    ("article-8.webp", "Shiitake mushroom growing on an oak log", "Organic Oak Log Forest Grown Shiitake Mushrooms are a Delicious and Nutritious Treat"),
    ("article-9.webp", "Oak log rows in a forest mushroom farm", "Why Shiitake Mushrooms Are Best Grown on Oak Logs In a Forest"),
    ("article-10.webp", "Fresh shiitake mushrooms on a dark wooden surface", "Shiitake mushrooms"),
    ("article-11.webp", "Chef plating gourmet mushroom dishes", "Why Chefs Buy from Us"),
]

article_cards = ""
for img, alt, title in ARTICLES:
    article_cards += f"""
          <article class="media-card">
            <div class="media-card__image">
              <img src="../images/{img}" alt="{alt}" width="640" height="360" loading="lazy" decoding="async">
            </div>
            <div class="media-card__body">
              <h2 class="media-card__title">{title}</h2>
            </div>
          </article>"""

pages = {
    "about.html": layout(
        "about",
        "About Us | Suwannee Bell Farms",
        "Learn about Suwannee Bell Farms — a family-owned organic oak log shiitake mushroom micro-farm in Bell, Florida.",
        """
    <div class="banner banner--forest">
      <h1>About Us</h1>
    </div>
    <section class="section">
      <div class="container container--narrow">
        <div class="about-card">
          <img src="../images/logo.webp" alt="" class="about-watermark" width="280" height="280" aria-hidden="true" loading="lazy" decoding="async">
          <div class="about-content">
            <p>Suwannee Bell Farms LLC is a family-owned micro-farm located in Bell, Florida, specializing in the cultivation of premium organic oak log shiitake mushrooms. Nestled in the heart of the Suwannee Valley, our farm combines traditional Japanese log-growing techniques with the natural beauty and resources of North Florida's temperate forests.</p>
            <p>Founded on a passion for sustainable agriculture and exceptional food, we grow our shiitake mushrooms on sustainably harvested oak logs placed in our forest shade house. This time-honored method produces mushrooms with a rich, meaty texture, deep umami flavor, and distinctive cracked cap pattern that connoisseurs prize.</p>
            <div>
              <h2>Our mission objectives are to:</h2>
              <ul class="about-list">
                <li>Deliver the highest quality organic oak log shiitake mushrooms to our customers</li>
                <li>Partner with chefs and restaurants to elevate their culinary offerings</li>
                <li>Tailor our growing seasons to meet the needs of our culinary partners</li>
                <li>Understand and respond to the unique requirements of each chef we serve</li>
                <li>Support and inspire culinary creativity through exceptional ingredients</li>
              </ul>
            </div>
            <div>
              <h2>Our value commitments:</h2>
              <p><strong>Environment:</strong> We practice regenerative, organic farming methods that work in harmony with the forest ecosystem.</p>
              <p><strong>Community:</strong> We are committed to strengthening local food systems and building relationships with our neighbors, chefs, and customers.</p>
              <p><strong>Spiritual:</strong> Our work is rooted in a deep appreciation for the wisdom of the forest and a Christian connection to the land.</p>
            </div>
          </div>
        </div>
      </div>
    </section>""",
    ),
    "contact.html": layout(
        "contact",
        "Contact Us | Suwannee Bell Farms",
        "Contact Suwannee Bell Farms — Robert Ledek, Farmer. Phone (352) 559-4295. Bell, Florida.",
        """
    <div class="banner banner--forest">
      <h1>Contact Us</h1>
    </div>
    <section class="section">
      <div class="container">
        <div class="contact-cards">
          <img src="../images/contact-values-card.webp" alt="Suwannee Bell Farms values — Fresh, Local, Organic, Sustainable" width="685" height="400" loading="lazy" decoding="async">
          <img src="../images/contact-business-card.webp" alt="Robert Ledek, Farmer — Suwannee Bell Farms contact card" width="685" height="400" loading="lazy" decoding="async">
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <a id="map-facade" class="map-facade" href="https://maps.google.com/maps?q=1509+SW+22+Ct,+Bell,+FL+32619" target="_blank" rel="noopener noreferrer" aria-label="Open Suwannee Bell Farms location in Google Maps">
          <img src="../images/gallery-3.webp" alt="Map preview — 1509 SW 22 Ct, Bell, Florida 32619" width="800" height="480" loading="lazy" decoding="async">
          <span class="map-facade__cta btn btn--forest">Open in Google Maps</span>
        </a>
      </div>
    </section>""",
    ),
    "sample.html": layout(
        "sample",
        "Request Free Sample | Suwannee Bell Farms",
        "Request a free sample of organic oak log shiitake mushrooms from Suwannee Bell Farms.",
        """
    <div class="banner">
      <h1>Request Your Free Shiitake Sample Today!</h1>
    </div>
    <section class="section sample-page">
      <div class="container container--narrow">
        <div class="sample-intro">
          <p>Experience the rich, earthy flavors of our premium organic oak log shiitake mushrooms — hand-harvested at peak maturity from our forest farm in Bell, Florida.</p>
          <div>
            <h2>What you'll receive:</h2>
            <ul class="about-list">
              <li>A generous portion of our organic oak log forest grown shiitake mushrooms</li>
              <li>Freshly harvested and shipped within 24 hours</li>
              <li>Information about our growing methods and farm practices</li>
              <li>Recipe suggestions from our culinary partners</li>
            </ul>
          </div>
          <div>
            <h2>Why choose our shiitake mushrooms?</h2>
            <ul class="about-list">
              <li>Certified organic, grown on sustainably harvested oak logs</li>
              <li>Distinctive cracked cap pattern indicating premium quality</li>
              <li>Rich umami flavor and meaty texture</li>
              <li>Hand-selected at peak maturity for maximum flavor and nutrition</li>
            </ul>
          </div>
        </div>
        <form id="sample-form" class="form-grid">
          <div>
            <label for="company-name" class="form-label">Company Name</label>
            <input type="text" id="company-name" name="company" class="form-input" required>
          </div>
          <div>
            <label for="sample-email" class="form-label">Email Address</label>
            <input type="email" id="sample-email" name="email" class="form-input" required>
          </div>
          <div>
            <label for="business-phone" class="form-label">Business Phone</label>
            <input type="tel" id="business-phone" name="phone" class="form-input" required>
          </div>
          <div>
            <label for="sample-address" class="form-label">Address</label>
            <textarea id="sample-address" name="address" rows="4" class="form-input form-textarea" required></textarea>
          </div>
          <button type="submit" class="btn btn--forest">Submit</button>
        </form>
        <p class="sample-note">Limited quantities available, so don't miss out!</p>
      </div>
    </section>""",
    ),
    "articles.html": layout(
        "articles",
        "Articles | Suwannee Bell Farms",
        "Read articles about shiitake mushrooms, sustainable forest farming, recipes, and nutrition.",
        f"""
    <div class="banner">
      <h1>Articles</h1>
    </div>
    <section class="section articles-page">
      <div class="container">
        <div class="card-grid card-grid--3">{article_cards}
        </div>
      </div>
    </section>""",
    ),
    "product.html": layout(
        "product",
        "Fresh Organic Oak Log Shiitake Mushrooms | Suwannee Bell Farms",
        "Shop fresh organic oak log forest grown shiitake mushrooms from Suwannee Bell Farms.",
        """
    <section class="section section--white">
      <div class="container">
        <div class="product-layout">
          <div class="product-page-image">
            <img id="product-main-image" src="../images/product.webp" alt="Fresh organic shiitake mushrooms in a white bowl" width="600" height="800" loading="eager" decoding="async">
            <button type="button" id="expand-image-btn" class="product-expand-btn" aria-label="Expand image">
              <svg aria-hidden="true" width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"/></svg>
            </button>
          </div>
          <div>
            <h1 class="section-title">Fresh Organic Oak Log Shiitake Mushrooms: A Taste of the Forest</h1>
            <p class="product-price">$25.00 – $250.00</p>
            <p style="color:var(--terracotta);margin-bottom:1.5rem;">Experience the rich, earthy flavor of our premium shiitake mushrooms, cultivated on sustainably harvested oak logs in the heart of the forest.</p>
            <form id="product-form" class="form-grid">
              <div>
                <label for="package-select" class="form-label">Packages</label>
                <select id="package-select" class="product-select">
                  <option value="">Choose an option</option>
                  <option value="half-pound">Half Pound — $25.00</option>
                  <option value="one-pound">One Pound — $45.00</option>
                  <option value="two-pound">Two Pounds — $85.00</option>
                  <option value="five-pound">Five Pounds — $200.00</option>
                  <option value="ten-pound">Ten Pounds — $250.00</option>
                </select>
              </div>
              <div style="display:flex;flex-wrap:wrap;gap:1rem;align-items:center;">
                <div class="qty-row">
                  <button type="button" id="qty-minus" class="qty-btn" aria-label="Decrease quantity">−</button>
                  <input type="number" id="qty-input" value="1" min="1" max="99" class="qty-input" aria-label="Quantity">
                  <button type="button" id="qty-plus" class="qty-btn" aria-label="Increase quantity">+</button>
                </div>
                <button type="submit" class="btn btn--terracotta">Buy Now</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
    <section class="section section--white">
      <div class="container">
        <div class="product-tabs" role="tablist">
          <button type="button" class="product-tab is-active" role="tab" aria-selected="true" data-tab="description">Description</button>
          <button type="button" class="product-tab" role="tab" aria-selected="false" data-tab="additional">Additional Information</button>
          <button type="button" class="product-tab" role="tab" aria-selected="false" data-tab="reviews">Reviews (0)</button>
        </div>
        <div id="tab-description" class="product-tab-panel is-active" role="tabpanel">
          <h2 class="section-title" style="font-size:1.25rem;">Fresh Organic Oak Log Shiitake Mushrooms</h2>
          <div class="prose">
            <p>Our shiitake mushrooms are grown using the traditional Japanese method of log cultivation — a time-honored practice that produces mushrooms of exceptional quality, flavor, and nutritional value.</p>
            <p>Shiitake mushrooms (Lentinula edodes) have been prized for centuries in Asian cuisine for their rich, savory umami flavor and meaty texture.</p>
          </div>
        </div>
        <div id="tab-additional" class="product-tab-panel" role="tabpanel" hidden>
          <table class="product-info-table">
            <tbody>
              <tr><th>Weight</th><td>0.5 lb, 1 lb, 2 lb, 5 lb, 10 lb</td></tr>
              <tr><th>Ingredients</th><td>100% Organic Shiitake Mushrooms (Lentinula edodes)</td></tr>
              <tr><th>Growing Method</th><td>Oak log forest cultivation</td></tr>
              <tr><th>Origin</th><td>Suwannee Valley, Florida, USA</td></tr>
            </tbody>
          </table>
        </div>
        <div id="tab-reviews" class="product-tab-panel" role="tabpanel" hidden>
          <p style="color:var(--text-muted);padding:1.5rem 0;">There are no reviews yet. Be the first to review our shiitake mushrooms.</p>
        </div>
      </div>
    </section>
    <div id="image-lightbox" class="image-lightbox" role="dialog" aria-label="Product image preview" hidden>
      <button type="button" id="lightbox-close" class="lightbox-close" aria-label="Close preview">&times;</button>
      <img src="../images/product.webp" alt="Fresh organic shiitake mushrooms enlarged view" width="600" height="800">
    </div>""",
    ),
}

for name, html in pages.items():
    (PAGES / name).write_text(html, encoding="utf-8")
    print(f"Wrote {name}")
