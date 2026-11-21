from PIL import Image, ImageDraw, ImageFont
import random, math

random.seed(42)

W, H = 1024, 1024
img = Image.new("RGB", (W, H), "#0a0a0a")
draw = ImageDraw.Draw(img)

# Langit gradasi
for y in range(H):
    t = y / H
    r = int(20 + t * 60)
    g = int(10 + t * 30)
    b = int(40 + t * 80)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Matahari/pemandang
cx, cy = W * 0.7, H * 0.25
for r in range(180, 40, -10):
    alpha = 255 - r
    color = (255, 180 + random.randint(-20, 20), 50 + random.randint(-20, 20))
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)

gunung = [(0, H), (200, H*0.6), (350, H*0.55), (500, H*0.65), (700, H*0.5), (1024, H)]
draw.polygon(gunung, fill="#050510")
detail_gunung = [(150, H*0.7), (280, H*0.62), (400, H*0.75), (560, H*0.6), (750, H*0.7), (900, H*0.65)]
for x, y in detail_gunung:
    draw.ellipse([x-30, y-30, x+30, y+30], fill="#020210")

rumah = [(W*0.15, H*0.85), (W*0.3, H*0.8), (W*0.35, H*0.9), (W*0.15, H*0.9)]
draw.polygon(rumah, fill="#2a1a10")
drawing = ImageDraw.Draw(img)
drawing.rectangle([W*0.2, H*0.82, W*0.28, H*0.88], fill="#3a2a20")

for i in range(200):
    x = random.randint(0, W)
    y = random.randint(int(H*0.6), H)
    r = random.randint(1, 3)
    color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    draw.ellipse([x-r, y-r, x+r, y+r], fill=color)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 90)
draw.text((W*0.5 - 200, H*0.88), "GTA VI", fill="#ffdd44", font=font)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
draw.text((W*0.5 - 150, H*0.94), "Cover Art Submission", fill="#cccccc", font=font2)

img.save("/tmp/gta6-cover.png")
log "Gambar tersimpan: /tmp/gta6-cover.png"
