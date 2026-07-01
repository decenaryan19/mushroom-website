#!/usr/bin/env python3
"""Resize and compress images for PageSpeed."""
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    import subprocess
    subprocess.check_call(["pip", "install", "pillow", "-q"])
    from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "images"

SPECS = {
    "logo.webp": (128, 128, 85),
    "hero-1.webp": (1920, 1080, 78),
    "hero-2.webp": (1920, 1080, 78),
    "product.webp": (800, 800, 80),
    "product-main.webp": (800, 800, 80),
    "recipe-grill.webp": (640, 400, 78),
    "recipe-roast.webp": (640, 400, 78),
    "recipe-stir-fry.webp": (640, 400, 78),
    "gallery-1.webp": (480, 540, 75),
    "gallery-2.webp": (480, 540, 75),
    "gallery-3.webp": (480, 540, 75),
    "gallery-4.webp": (480, 540, 75),
    "gallery-5.webp": (480, 540, 75),
    "gallery-6.webp": (480, 540, 75),
    "gallery-7.webp": (480, 540, 75),
    "gallery-8.webp": (480, 540, 75),
    "article-1.webp": (640, 360, 78),
    "article-2.webp": (640, 360, 78),
    "article-3.webp": (640, 360, 78),
    "article-4.webp": (640, 360, 78),
    "article-5.webp": (640, 360, 78),
    "article-6.webp": (640, 360, 78),
    "article-7.webp": (640, 360, 78),
    "article-8.webp": (640, 360, 78),
    "article-9.webp": (640, 360, 78),
    "article-10.webp": (640, 360, 78),
    "article-11.webp": (640, 360, 78),
    "contact-values-card.webp": (700, 400, 80),
    "contact-business-card.webp": (700, 400, 80),
}

PNG_FALLBACK = {
    "logo.webp": "logo.png",
    "hero-1.webp": "hero-1.png",
    "hero-2.webp": "hero-2.png",
    "product.webp": "product.png",
    "product-main.webp": "product.png",
    "recipe-grill.webp": "recipe-grill.png",
    "recipe-roast.webp": "recipe-roast.png",
    "recipe-stir-fry.webp": "recipe-stir-fry.png",
    "gallery-1.webp": "gallery-1.png",
    "gallery-2.webp": "gallery-2.png",
    "gallery-3.webp": "gallery-3.png",
    "gallery-4.webp": "gallery-4.png",
    "gallery-5.webp": "gallery-5.png",
    "gallery-6.webp": "gallery-6.png",
    "gallery-7.webp": "gallery-7.png",
    "gallery-8.webp": "gallery-8.png",
    "article-1.webp": "article-1.png",
    "article-2.webp": "article-2.png",
    "article-3.webp": "article-3.png",
    "article-4.webp": "article-4.png",
    "article-5.webp": "article-5.png",
    "article-6.webp": "article-6.png",
    "article-7.webp": "article-7.png",
    "article-8.webp": "article-8.png",
    "article-9.webp": "article-9.png",
    "article-10.webp": "article-10.png",
    "article-11.webp": "article-11.png",
    "contact-values-card.webp": "contact-values-card.png",
    "contact-business-card.webp": "contact-business-card.png",
}


def optimize(name, max_w, max_h, quality):
    dest = IMG / name
    src = IMG / PNG_FALLBACK.get(name, name)
    if not src.exists():
        print(f"SKIP {name} (no source)")
        return
    img = Image.open(src)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    img.save(dest, "WEBP", quality=quality, method=6)
    print(f"{name}: {dest.stat().st_size // 1024} KB ({img.size[0]}x{img.size[1]})")


for fname, (w, h, q) in SPECS.items():
    optimize(fname, w, h, q)

# Mobile hero variants
for hero, src_name in [("hero-1-mobile.webp", "hero-1.png"), ("hero-2-mobile.webp", "hero-2.png")]:
    src = IMG / src_name
    if src.exists():
        img = Image.open(src).convert("RGB")
        img.thumbnail((828, 600), Image.Resampling.LANCZOS)
        dest = IMG / hero
        img.save(dest, "WEBP", quality=72, method=6)
        print(f"{hero}: {dest.stat().st_size // 1024} KB")

print("Done.")
