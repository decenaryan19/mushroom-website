#!/usr/bin/env python3
"""Generate optimized subpages with shared layout."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"

HEAD = """  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#1f4d0a">
  <style>
    *,*::before,*::after{{box-sizing:border-box}}body{{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:#fffdee;color:#2b2b2b}}img,svg{{display:block;max-width:100%;height:auto}}a{{color:inherit;text-decoration:none}}.container{{width:min(100% - 1.875rem,1250px);margin-inline:auto}}.site-header{{position:sticky;top:0;z-index:50;background:#fffdee;box-shadow:0 1px 2px rgba(0,0,0,.06)}}.site-header__inner{{display:flex;align-items:center;justify-content:space-between;min-height:70px;gap:1rem}}.site-logo{{display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;width:70px;height:70px}}.site-logo img{{width:100%;height:100%;object-fit:contain}}.site-nav{{display:none;align-items:center;gap:1.35rem;font-size:.72rem;font-weight:700;text-transform:uppercase}}.site-nav a{{color:#000;line-height:25px;padding:.35rem 0}}.site-nav a.is-active{{background:#1f4d0a;color:#fff;padding:.35rem .8rem}}.site-header__actions{{display:flex;align-items:center;gap:.5rem}}.icon-btn{{display:inline-flex;align-items:center;justify-content:center;min-width:48px;min-height:48px;border:0;background:transparent;color:#374151}}.icon-btn svg{{width:20px;height:20px}}.mobile-nav{{display:none}}.banner{{display:flex;align-items:center;justify-content:center;min-height:80px;padding:.75rem 1rem;background:#dc7e32}}.banner h1,.banner h2{{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:clamp(1.25rem,2.5vw,2rem);font-weight:700;line-height:1.2;text-transform:uppercase;color:#fff}}@media (min-width:768px){{.site-nav{{display:flex}}#mobile-menu-btn{{display:none}}}}@media (min-width:850px){{.site-header__inner{{min-height:90px}}.site-logo{{width:90px;height:90px}}}}
  </style>
  <link rel="stylesheet" href="../css/styles.min.css">"""

HEADER = """
  <header class="site-header">
    <div class="container site-header__inner">
      <a href="../index.html" class="site-logo" aria-label="Suwannee Bell Farms — Home">
        <img src="../images/logo-90.webp" srcset="../images/logo-44.webp 44w, ../images/logo-90.webp 90w" sizes="(min-width: 850px) 90px, 70px" alt="Suwannee Bell Farms logo" width="44" height="44" decoding="async">
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
  <script src="../js/script.min.js" defer></script>"""


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
    ("article-1.webp", "Grilled mushroom skewers on a wooden board", "Shiitake Mushrooms as a Meat Alternative", "article-meat-alternative.html"),
    ("article-2.webp", "Hands holding freshly harvested shiitake mushrooms", "The History of Shiitake Mushrooms", "article-history.html"),
    ("article-3.webp", "Nutritious vegan bowl with shiitake mushrooms", "A Delicious and Nutritious Vegan Choice", "article-vegan-choice.html"),
    ("article-4.webp", "Fresh shiitake mushrooms on a wooden table", "Best Way to Eat Shiitake Mushrooms Raw", None),
    ("article-5.webp", "Sun dried shiitake mushrooms in a glass jar", "Sun Dried Shiitake Mushrooms for Convenience Flavor and Nutrition", None),
    ("article-6.webp", "Wild mushrooms growing on a mossy log", "Why It Is Beneficial to Support Sustainable Forests", None),
    ("article-7.webp", "Freshly harvested shiitake mushrooms", "Why You Should Buy Fresh Locally Sourced and Sustainable Organic Shiitake Mushrooms", None),
    ("article-8.webp", "Shiitake mushroom growing on an oak log", "Organic Oak Log Forest Grown Shiitake Mushrooms are a Delicious and Nutritious Treat", None),
    ("article-9.webp", "Oak log rows in a forest mushroom farm", "Why Shiitake Mushrooms Are Best Grown on Oak Logs In a Forest", None),
    ("article-10.webp", "Fresh shiitake mushrooms on a dark wooden surface", "Shiitake mushrooms", None),
    ("article-11.webp", "Chef plating gourmet mushroom dishes", "Why Chefs Buy from Us", None),
]

article_cards = ""
for img, alt, title, link in ARTICLES:
    if link:
        article_cards += f"""
          <article class="media-card">
            <a href="{link}" style="display: block; color: inherit; text-decoration: none;">
              <div class="media-card__image">
                <img src="../images/{img}" alt="{alt}" width="640" height="360" loading="lazy" decoding="async">
              </div>
              <div class="media-card__body">
                <h2 class="media-card__title">{title}</h2>
              </div>
            </a>
          </article>"""
    else:
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
    "recipe-grill.html": layout(
        "",
        "How to Grill Shiitake Mushrooms | Suwannee Bell Farms",
        "Learn how to grill organic oak log shiitake mushrooms to perfection with this simple, delicious recipe from Suwannee Bell Farms.",
        """
    <div class="banner banner--terracotta">
      <h1>How to Grill Shiitake Mushrooms</h1>
    </div>
    <section class="section">
      <div class="container">
        <div class="grid-2">
          <div class="grid-2__media">
            <div class="product-image-wrap" style="max-width: 100%; margin: 0;">
              <img src="../images/recipe-grill.webp" alt="Grilled shiitake mushrooms" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 100%;" width="533" height="400" loading="lazy" decoding="async">
            </div>
          </div>
          <div class="grid-2__text">
            <div class="prose" style="font-size: 0.95rem; line-height: 1.6; color: #333; gap: 1.25rem;">
              <p>Shiitake mushrooms are a delicious and nutritious ingredient that can be grilled to perfection. They have a meaty texture and a rich, earthy flavor that is enhanced by grilling. Grilled shiitake mushrooms are a great addition to any barbecue or summer meal.</p>
              
              <h2 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--forest); margin-top: 1rem; margin-bottom: 0.5rem;">Ingredients</h2>
              <ul class="about-list" style="list-style: none; padding-left: 0; margin-bottom: 1.5rem;">
                <li>1 pound shiitake mushrooms, stems removed</li>
                <li>1 tablespoon olive oil</li>
                <li>1/2 teaspoon salt</li>
                <li>1/4 teaspoon black pepper</li>
              </ul>
              
              <h2 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--forest); margin-top: 1rem; margin-bottom: 0.5rem;">Instructions</h2>
              <ol style="padding-left: 1.25rem; margin-bottom: 0; display: grid; gap: 0.5rem;">
                <li>Preheat your grill to medium-high heat.</li>
                <li>Brush the shiitake mushrooms with olive oil and season with salt and pepper.</li>
                <li>Grill the shiitake mushrooms for 2-3 minutes per side, or until they are tender and slightly charred.</li>
                <li>Serve immediately with your favorite dipping sauce, such as soy sauce, chimichurri, or barbecue sauce.</li>
              </ol>
            </div>
          </div>
        </div>
      </div>
    </section>""",
    ),
    "recipe-roast.html": layout(
        "",
        "How to Roast Shiitake Mushrooms | Suwannee Bell Farms",
        "Learn how to roast organic oak log shiitake mushrooms to perfection with this simple, delicious recipe from Suwannee Bell Farms.",
        """
    <div class="banner banner--terracotta">
      <h1>How to Roast Shiitake Mushrooms</h1>
    </div>
    <section class="section">
      <div class="container">
        <div class="grid-2">
          <div class="grid-2__media">
            <div class="product-image-wrap" style="max-width: 100%; margin: 0;">
              <img src="../images/recipe-roast.webp" alt="Roasted shiitake mushrooms" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 100%;" width="533" height="400" loading="lazy" decoding="async">
            </div>
          </div>
          <div class="grid-2__text">
            <div class="prose" style="font-size: 0.95rem; line-height: 1.6; color: #333; gap: 1.25rem;">
              <p>Shiitake mushrooms are a delicious and nutritious ingredient that can be roasted to perfection. They have a meaty texture and a rich, earthy flavor that is enhanced by roasting. Roasted shiitake mushrooms are a great addition to any meal, and they are especially popular among vegans and vegetarians as a meat alternative.</p>
              
              <h2 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--forest); margin-top: 1rem; margin-bottom: 0.5rem;">Ingredients</h2>
              <ul class="about-list" style="list-style: none; padding-left: 0; margin-bottom: 1.5rem;">
                <li>1 pound shiitake mushrooms, stems removed and sliced</li>
                <li>1 tablespoon olive oil</li>
                <li>1/2 teaspoon salt</li>
                <li>1/4 teaspoon black pepper</li>
              </ul>
              
              <h2 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--forest); margin-top: 1rem; margin-bottom: 0.5rem;">Instructions</h2>
              <ol style="padding-left: 1.25rem; margin-bottom: 0; display: grid; gap: 0.5rem;">
                <li>Preheat your oven to 400 degrees Fahrenheit.</li>
                <li>Toss the shiitake mushrooms with olive oil, salt, and pepper.</li>
                <li>Spread the shiitake mushrooms in a single layer on a baking sheet.</li>
                <li>Roast the shiitake mushrooms for 20-25 minutes, or until they are tender and slightly browned.</li>
                <li>Serve immediately with your favorite dipping sauce, such as soy sauce, chimichurri, or barbecue sauce.</li>
              </ol>
            </div>
          </div>
        </div>
      </div>
    </section>""",
    ),
    "recipe-stir-fry.html": layout(
        "",
        "How to Stir-Fry Shiitake Mushrooms | Suwannee Bell Farms",
        "Learn how to stir-fry organic oak log shiitake mushrooms to perfection with this simple, delicious recipe from Suwannee Bell Farms.",
        """
    <div class="banner banner--terracotta">
      <h1>How to Stir-Fry Shiitake Mushrooms</h1>
    </div>
    <section class="section">
      <div class="container">
        <div class="grid-2">
          <div class="grid-2__media">
            <div class="product-image-wrap" style="max-width: 100%; margin: 0;">
              <img src="../images/recipe-stir-fry.webp" alt="Stir-fried shiitake mushrooms" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 100%;" width="486" height="364" loading="lazy" decoding="async">
            </div>
          </div>
          <div class="grid-2__text">
            <div class="prose" style="font-size: 0.95rem; line-height: 1.6; color: #333; gap: 1.25rem;">
              <p>Shiitake mushrooms are a delicious and nutritious ingredient that can be used in a variety of dishes. They are especially well-suited for stir-frying, as their meaty texture and rich flavor hold up well to high-heat cooking.</p>
              
              <h2 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--forest); margin-top: 1rem; margin-bottom: 0.5rem;">Ingredients</h2>
              <ul class="about-list" style="list-style: none; padding-left: 0; margin-bottom: 1.5rem;">
                <li>1 pound shiitake mushrooms, stems removed and sliced</li>
                <li>1 tablespoon olive oil</li>
                <li>1/2 teaspoon salt</li>
                <li>1/4 teaspoon black pepper</li>
                <li>1/4 cup chopped garlic</li>
                <li>1/4 cup chopped ginger</li>
                <li>1 green onion, chopped</li>
                <li>1/4 cup soy sauce</li>
                <li>1/4 cup water</li>
              </ul>
              
              <h2 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--forest); margin-top: 1rem; margin-bottom: 0.5rem;">Instructions</h2>
              <ol style="padding-left: 1.25rem; margin-bottom: 0; display: grid; gap: 0.5rem;">
                <li>Heat the olive oil in a large skillet or wok over medium-high heat.</li>
                <li>Add the shiitake mushrooms, salt, and pepper and cook, stirring frequently, until the mushrooms are softened and browned, about 5 minutes.</li>
                <li>Add the garlic, ginger, and green onion and cook for 1 minute more.</li>
                <li>Add the soy sauce and water and cook for another minute, or until the sauce has thickened slightly.</li>
                <li>Serve immediately with rice or noodles.</li>
              </ol>
            </div>
          </div>
        </div>
      </div>
    </section>""",
    ),
    "article-meat-alternative.html": layout(
        "articles",
        "Shiitake Mushrooms as a Meat Alternative | Suwannee Bell Farms",
        "Discover why organic oak log shiitake mushrooms make an excellent, healthy, and delicious meat alternative for vegans and vegetarians.",
        """
    <div class="banner banner--forest">
      <h1>Shiitake Mushrooms as a Meat Alternative</h1>
    </div>
    <section class="section">
      <div class="container">
        <div class="grid-2">
          <div class="grid-2__media">
            <div class="product-image-wrap" style="max-width: 100%; margin: 0;">
              <img src="../images/article-1.webp" alt="Grilled mushroom skewers" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 100%;" width="523" height="392" loading="lazy" decoding="async">
            </div>
          </div>
          <div class="grid-2__text">
            <div class="prose" style="font-size: 0.95rem; line-height: 1.6; color: #333; gap: 1.25rem;">
              <p>Shiitake mushrooms are a popular meat alternative for vegans and vegetarians. They have a meaty texture and a rich, earthy flavor. Shiitake mushrooms are also a good source of protein, fiber, and other nutrients.</p>
              
              <h2 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--forest); margin-top: 1rem; margin-bottom: 0.5rem;">Why are shiitake mushrooms a good meat alternative?</h2>
              <ul class="about-list" style="list-style: none; padding-left: 0; margin-bottom: 1.5rem; display: grid; gap: 0.75rem;">
                <li><strong>Meaty texture:</strong> Shiitake mushrooms are firm and chewy, which makes them a good substitute for meat in many dishes.</li>
                <li><strong>Rich, earthy flavor:</strong> Shiitake mushrooms have a complex flavor that can add depth to many dishes.</li>
                <li><strong>Good source of protein:</strong> Shiitake mushrooms contain about 4 grams of protein per cup. This makes them a good source of protein for people who are not eating meat.</li>
                <li><strong>Good source of fiber:</strong> Shiitake mushrooms contain about 3 grams of fiber per cup. This makes them a good source of fiber for people who are trying to increase their fiber intake.</li>
                <li><strong>Low in calories:</strong> Shiitake mushrooms are very low in calories. One cup of shiitake mushrooms contains only about 30 calories.</li>
                <li><strong>Versatility:</strong> Shiitake mushrooms can be used in place of meat in a variety of dishes. They can be stir-fried, grilled, roasted, or sautéed. Shiitake mushrooms can also be added to soups, stews, and pasta dishes.</li>
              </ul>
              
              <h2 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--forest); margin-top: 1rem; margin-bottom: 0.5rem;">Tips for using shiitake mushrooms as a meat alternative:</h2>
              <ul class="about-list" style="list-style: none; padding-left: 0; margin-bottom: 0; display: grid; gap: 0.75rem;">
                <li><strong>Choose the right mushrooms:</strong> When choosing shiitake mushrooms, look for mushrooms that have firm, fleshy caps and stems that are not too woody. Avoid mushrooms that are slimy or have brown spots.</li>
                <li><strong>Slice the mushrooms thinly:</strong> This will help the mushrooms to cook evenly.</li>
                <li><strong>Season the mushrooms well:</strong> Shiitake mushrooms have a mild flavor, so it is important to season them well. You can use salt, pepper, garlic powder, onion powder, or other herbs and spices to season your shiitake mushrooms.</li>
                <li><strong>Cook the mushrooms until they are browned and tender:</strong> Shiitake mushrooms should be cooked until they are browned and tender. This will help to develop the flavor of the mushrooms.</li>
              </ul>
              <p style="margin-top: 1rem;">If you are looking for a delicious and nutritious meat alternative, be sure to try shiitake mushrooms!</p>
            </div>
          </div>
        </div>
      </div>
    </section>""",
    ),
    "article-history.html": layout(
        "articles",
        "The History of Shiitake Mushrooms | Suwannee Bell Farms",
        "Explore the rich 1,000-year history of shiitake mushrooms, from ancient Chinese dynasties to modern sustainable forest farming.",
        """
    <div class="banner banner--forest">
      <h1>The History of Shiitake Mushrooms</h1>
    </div>
    <section class="section">
      <div class="container">
        <div class="grid-2">
          <div class="grid-2__media">
            <div class="product-image-wrap" style="max-width: 100%; margin: 0;">
              <img src="../images/article-2.webp" alt="Hands holding freshly harvested shiitake mushrooms" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 100%;" width="523" height="392" loading="lazy" decoding="async">
            </div>
          </div>
          <div class="grid-2__text">
            <div class="prose" style="font-size: 0.95rem; line-height: 1.6; color: #333; gap: 1.25rem;">
              <p>Shiitake mushrooms are one of the oldest cultivated mushrooms in the world, with a history dating back over 1,000 years. They are native to East Asia and were first cultivated in China during the Song Dynasty (960-1279 AD). Shiitake mushrooms were quickly adopted by other East Asian cultures, including Japan and Korea.</p>
              <p>Shiitake mushrooms were originally cultivated on oak logs, and this method is still used today. However, shiitake mushrooms can also be cultivated on other substrates, such as sawdust and straw. Shiitake mushrooms are now grown all over the world, and they are one of the most popular types of mushrooms consumed today.</p>
              <p>In addition to their culinary uses, shiitake mushrooms have also been used in traditional Chinese medicine for centuries. Shiitake mushrooms are believed to have a number of health benefits, including boosting the immune system, reducing inflammation, and improving heart health.</p>
              
              <h2 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--forest); margin-top: 1rem; margin-bottom: 0.5rem;">Timeline of the history of shiitake mushrooms:</h2>
              <ul class="about-list" style="list-style: none; padding-left: 0; margin-bottom: 1.5rem; display: grid; gap: 0.5rem;">
                <li><strong>1000s AD:</strong> Shiitake mushrooms are first cultivated in China.</li>
                <li><strong>1200s AD:</strong> Shiitake mushrooms are introduced to Japan and Korea.</li>
                <li><strong>1600s AD:</strong> Shiitake mushrooms are introduced to Europe.</li>
                <li><strong>1800s AD:</strong> Shiitake mushrooms are introduced to North America.</li>
                <li><strong>1900s AD:</strong> Shiitake mushrooms become increasingly popular in the West, and commercial production begins.</li>
                <li><strong>2000s AD:</strong> Shiitake mushrooms are now one of the most popular types of mushrooms consumed in the world.</li>
              </ul>
              
              <p>Today, shiitake mushrooms are a popular ingredient in many cuisines around the world. They can be found fresh, dried, or powdered. Shiitake mushrooms are also used in a variety of dietary supplements and health products.</p>
              <p>Enjoy the delicious and nutritious taste of shiitake mushrooms!</p>
            </div>
          </div>
        </div>
      </div>
    </section>""",
    ),
    "article-vegan-choice.html": layout(
        "articles",
        "A Delicious and Nutritious Vegan Choice | Suwannee Bell Farms",
        "Learn why organic oak log shiitake mushrooms are a perfect, nutrient-dense addition to any vegan or plant-based diet.",
        """
    <div class="banner banner--forest">
      <h1>A Delicious and Nutritious Vegan Choice</h1>
    </div>
    <section class="section">
      <div class="container">
        <div class="grid-2">
          <div class="grid-2__media">
            <div class="product-image-wrap" style="max-width: 100%; margin: 0;">
              <img src="../images/article-3.webp" alt="Nutritious vegan bowl with shiitake mushrooms" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 100%;" width="480" height="360" loading="lazy" decoding="async">
            </div>
          </div>
          <div class="grid-2__text">
            <div class="prose" style="font-size: 0.95rem; line-height: 1.6; color: #333; gap: 1.25rem;">
              <p>Shiitake mushrooms are a delicious and nutritious vegan food that can be enjoyed in a variety of ways. They are also a good source of protein, fiber, vitamins, and minerals.</p>
              
              <h2 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--forest); margin-top: 1rem; margin-bottom: 0.5rem;">Why are shiitake mushrooms good for vegans?</h2>
              <p>Shiitake mushrooms are a good source of plant-based protein, which is essential for vegans. They are also a good source of fiber, which can help to keep you feeling full and satisfied. Shiitake mushrooms also contain a variety of vitamins and minerals, including vitamins B and D, as well as copper and selenium.</p>
              
              <h2 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--forest); margin-top: 1rem; margin-bottom: 0.5rem;">How can vegans enjoy shiitake mushrooms?</h2>
              <p>Shiitake mushrooms can be enjoyed in a variety of ways. They can be cooked, grilled, roasted, or eaten raw. Shiitake mushrooms can also be dried and used in powder form in sauces, marinades, and other recipes.</p>
              
              <h2 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--forest); margin-top: 1rem; margin-bottom: 0.5rem;">Here are a few ideas for vegan recipes using shiitake mushrooms:</h2>
              <ul class="about-list" style="list-style: none; padding-left: 0; margin-bottom: 1.5rem; display: grid; gap: 0.5rem;">
                <li>Stir-fried shiitake mushrooms with tofu and vegetables</li>
                <li>Shiitake mushroom and vegan cheese soup</li>
                <li>Shiitake mushroom and vegan sausage burgers</li>
                <li>Shiitake mushroom risotto</li>
                <li>Shiitake mushroom tacos</li>
              </ul>
              
              <h2 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--forest); margin-top: 1rem; margin-bottom: 0.5rem;">Where to buy shiitake mushrooms</h2>
              <p>Shiitake mushrooms can be found at most grocery stores. They can also be purchased from online retailers. When choosing shiitake mushrooms, look for mushrooms that have firm, fleshy caps and stems that are not too woody. Avoid mushrooms that are slimy or have brown spots.</p>
              
              <h2 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--forest); margin-top: 1rem; margin-bottom: 0.5rem;">How to store shiitake mushrooms</h2>
              <p>Shiitake mushrooms can be stored in the refrigerator for up to a week. To store, place the mushrooms in a perforated plastic bag or container.</p>
            </div>
          </div>
        </div>
      </div>
    </section>""",
    ),
}

# product.html is maintained manually — do not add it to pages{} or it will
# overwrite the full WooCommerce-style product page with a short stub.

for name, html in pages.items():
    (PAGES / name).write_text(html, encoding="utf-8")
    print(f"Wrote {name}")
