#!/usr/bin/env python3
"""Resize, compress, and generate responsive WebP variants for PageSpeed."""
from __future__ import annotations

from pathlib import Path

try:
    from PIL import Image
except ImportError:
    import subprocess

    subprocess.check_call(["pip", "install", "pillow", "-q"])
    from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "images"

# (output name, max width, max height, quality)
PRIMARY = {
    "logo.webp": (88, 88, 82),
    "hero-1.webp": (1280, 720, 58),
    "hero-2.webp": (1280, 720, 58),
    "hero-1-mobile.webp": (640, 360, 55),
    "hero-2-mobile.webp": (640, 360, 55),
    "product.webp": (600, 800, 72),
    "recipe-grill.webp": (533, 367, 68),
    "recipe-roast.webp": (533, 367, 68),
    "recipe-stir-fry.webp": (486, 335, 68),
    "gallery-1.webp": (405, 540, 62),
    "gallery-2.webp": (405, 540, 62),
    "gallery-3.webp": (405, 540, 62),
    "gallery-4.webp": (405, 540, 62),
    "gallery-5.webp": (405, 540, 62),
    "gallery-6.webp": (405, 540, 62),
    "gallery-7.webp": (405, 540, 62),
    "gallery-8.webp": (405, 540, 62),
    "article-1.webp": (523, 360, 68),
    "article-2.webp": (523, 360, 68),
    "article-3.webp": (480, 331, 68),
}

# Smaller variants for responsive srcset (suffix, max width, quality)
RESPONSIVE = {
    "product.webp": [("product-384.webp", 384, 70)],
    "gallery-1.webp": [("gallery-1-335.webp", 335, 52)],
    "gallery-2.webp": [("gallery-2-335.webp", 335, 52)],
    "gallery-3.webp": [("gallery-3-335.webp", 335, 52)],
    "gallery-4.webp": [("gallery-4-335.webp", 335, 52)],
    "gallery-5.webp": [("gallery-5-335.webp", 335, 52)],
    "gallery-6.webp": [("gallery-6-335.webp", 335, 52)],
    "gallery-7.webp": [("gallery-7-335.webp", 335, 52)],
    "gallery-8.webp": [("gallery-8-335.webp", 335, 52)],
    "recipe-grill.webp": [("recipe-grill-400.webp", 400, 66)],
    "recipe-roast.webp": [("recipe-roast-400.webp", 400, 66)],
    "recipe-stir-fry.webp": [("recipe-stir-fry-400.webp", 400, 66)],
    "article-1.webp": [("article-1-400.webp", 400, 66)],
    "article-2.webp": [("article-2-400.webp", 400, 66)],
    "article-3.webp": [("article-3-400.webp", 400, 66)],
}


def open_rgb(path: Path) -> Image.Image:
    img = Image.open(path)
    if img.mode in ("RGBA", "P"):
        return img.convert("RGB")
    if img.mode != "RGB":
        return img.convert("RGB")
    return img


def save_webp(img: Image.Image, dest: Path, quality: int) -> None:
    img.save(dest, "WEBP", quality=quality, method=6)


def fit_within(img: Image.Image, max_w: int, max_h: int) -> Image.Image:
    copy = img.copy()
    copy.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    return copy


def fit_width(img: Image.Image, width: int) -> Image.Image:
    if img.width <= width:
        return img.copy()
    height = max(1, round(img.height * (width / img.width)))
    return img.resize((width, height), Image.Resampling.LANCZOS)


def optimize_primary(name: str, max_w: int, max_h: int, quality: int) -> Image.Image | None:
    src = IMG / name
    if not src.exists():
        print(f"SKIP {name} (missing)")
        return None
    img = fit_within(open_rgb(src), max_w, max_h)
    dest = IMG / name
    save_webp(img, dest, quality)
    print(f"{name}: {dest.stat().st_size // 1024} KB ({img.size[0]}x{img.size[1]})")
    return img


def main() -> None:
  for name, (max_w, max_h, quality) in PRIMARY.items():
    optimized = optimize_primary(name, max_w, max_h, quality)
    if optimized is None:
      continue
    for variant_name, width, variant_q in RESPONSIVE.get(name, []):
      variant = fit_width(optimized, width)
      dest = IMG / variant_name
      save_webp(variant, dest, variant_q)
      print(f"  -> {variant_name}: {dest.stat().st_size // 1024} KB ({variant.size[0]}x{variant.size[1]})")

  print("Done.")


if __name__ == "__main__":
  main()
