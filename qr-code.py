
import qrcode
import os
import re
import shutil
import subprocess
from PIL import Image, ImageDraw, ImageFont


# Android Internal Storage
SAVE_DIR = "/storage/emulated/0/Pictures/QR_CODE"

# Gradient colors
GREEN = (0, 200, 115)
CYAN = (0, 185, 180)
BLUE = (0, 155, 225)

WHITE = (255, 255, 255)

MODULE_SIZE = 12
BORDER = 4

RESET = "\033[0m"
BLUE_TEXT = "\033[38;2;0;155;225m"
YELLOW_TEXT = "\033[93m"
GREEN_TEXT = "\033[92m"


# ==========================================
# GRADIENT TEXT
# ==========================================

def get_gradient_color(position):

    if position <= 0.5:
        ratio = position * 2
        start, end = GREEN, CYAN
    else:
        ratio = (position - 0.5) * 2
        start, end = CYAN, BLUE

    return tuple(
        int(start[i] * (1 - ratio) + end[i] * ratio)
        for i in range(3)
    )


def gradient_text(text):

    result = ""
    width = max(len(text) - 1, 1)

    for i, char in enumerate(text):

        r, g, b = get_gradient_color(i / width)

        result += f"\033[38;2;{r};{g};{b}m{char}"

    return result + RESET


# ==========================================
# BAZIGARR QR GENERATOR BANNER
# ==========================================

def print_qr_banner():

    terminal_width = shutil.get_terminal_size((80, 24)).columns

    print()

    figlet = shutil.which("figlet")

    if not figlet:
        print("⚠️ FIGLET not installed!")
        print("Install using: pkg install figlet\n")
        return

    for word in ["QR CODE", "GENERATOR"]:

        try:

            output = subprocess.run(
                [
                    figlet,
                    "-f", "big",
                    "-w", str(terminal_width),
                    word
                ],
                capture_output=True,
                text=True,
                check=True
            )

            for line in output.stdout.rstrip("\n").splitlines():
                print(gradient_text(line))

        except subprocess.CalledProcessError:
            print("⚠️ FIGLET banner error!")
            return

    name = " BaziGarr "
    remaining = max(0, terminal_width - len(name))

    left = remaining // 2
    right = remaining - left

    divider = "═" * left + name + "═" * right

    print(gradient_text(divider))
    print()


# ==========================================
# QR COLOR FUNCTION
# ==========================================

def get_color(x, y, width, height):

    t = (x + y) / max(1, width + height - 2)

    if t < 0.5:
        ratio = t * 2
        start, end = GREEN, CYAN
    else:
        ratio = (t - 0.5) * 2
        start, end = CYAN, BLUE

    return tuple(
        int(start[i] * (1 - ratio) + end[i] * ratio)
        for i in range(3)
    )


# ==========================================
# FINDER PATTERN
# ==========================================

def is_finder(x, y, width, height):

    return (
        (BORDER <= x < BORDER + 7 and
         BORDER <= y < BORDER + 7)

        or

        (width - BORDER - 7 <= x < width - BORDER and
         BORDER <= y < BORDER + 7)

        or

        (BORDER <= x < BORDER + 7 and
         height - BORDER - 7 <= y < height - BORDER)
    )


# ==========================================
# TERMINAL QR DISPLAY
# ==========================================

def print_terminal_qr(matrix, filename):

    print("\n📱 QR GENERATED BOSS:\n")

    height = len(matrix)
    width = len(matrix[0])

    for y in range(0, height, 2):

        for x in range(width):

            if matrix[y][x]:
                top = get_color(x, y, width, height)
            else:
                top = WHITE

            if y + 1 < height and matrix[y + 1][x]:
                bottom = get_color(x, y + 1, width, height)
            else:
                bottom = WHITE

            r1, g1, b1 = top
            r2, g2, b2 = bottom

            print(
                f"\033[38;2;{r1};{g1};{b1}m"
                f"\033[48;2;{r2};{g2};{b2}m▀",
                end=""
            )

        print(RESET)

    print(RESET)

    # ======================================
    # FILENAME CENTERED UNDER TERMINAL QR
    # ======================================

    filename_width = len(filename)

    left_padding = max(
        0,
        (width - filename_width) // 2
    )

    centered_filename = (" " * left_padding) + filename

    print(gradient_text(centered_filename))
    print()


# ==========================================
# CREATE QR IMAGE
# ==========================================

def create_qr_image(matrix, filename):

    height = len(matrix)
    width = len(matrix[0])

    size = MODULE_SIZE

    qr_img = Image.new(
        "RGB",
        (width * size, height * size),
        WHITE
    )

    draw = ImageDraw.Draw(qr_img)

    for y in range(height):

        for x in range(width):

            if not matrix[y][x]:
                continue

            px = x * size
            py = y * size

            color = get_color(x, y, width, height)

            if is_finder(x, y, width, height):

                draw.rectangle(
                    (
                        px,
                        py,
                        px + size - 1,
                        py + size - 1
                    ),
                    fill=color
                )

            else:

                radius = size * 0.40

                draw.ellipse(
                    (
                        px + size / 2 - radius,
                        py + size / 2 - radius,
                        px + size / 2 + radius,
                        py + size / 2 + radius
                    ),
                    fill=color
                )

    # ======================================
    # FILENAME PERFECTLY CENTERED BELOW QR
    # WITH GREEN-CYAN-BLUE GRADIENT
    # ======================================

    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 24)
    except OSError:
        font = ImageFont.load_default()

    label = filename

    text_box = draw.textbbox(
        (0, 0),
        label,
        font=font
    )

    text_width = text_box[2] - text_box[0]
    text_height = text_box[3] - text_box[1]

    padding_top = 25
    padding_bottom = 25
    side_padding = 20

    final_width = max(
        qr_img.width,
        text_width + side_padding * 2
    )

    final_height = (
        qr_img.height
        + padding_top
        + text_height
        + padding_bottom
    )

    final_img = Image.new(
        "RGB",
        (final_width, final_height),
        WHITE
    )

    qr_x = (final_width - qr_img.width) // 2

    final_img.paste(
        qr_img,
        (qr_x, 0)
    )

    draw = ImageDraw.Draw(final_img)

    # CENTER FILENAME
    text_x = (final_width - text_width) // 2 - text_box[0]

    text_y = (
        qr_img.height
        + padding_top
        - text_box[1]
    )

    # DRAW EACH CHARACTER WITH GRADIENT
    for i, char in enumerate(label):

        r, g, b = get_gradient_color(
            i / max(len(label) - 1, 1)
        )

        char_width = draw.textlength(
            label[:i],
            font=font
        )

        draw.text(
            (text_x + char_width, text_y),
            char,
            fill=(r, g, b),
            font=font
        )

    return final_img


# ==========================================
# GENERATE QR
# ==========================================

def generate_qr(link, filename):

    if not re.match(r"^https?://", link, re.IGNORECASE):
        link = "https://" + link

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=MODULE_SIZE,
        border=BORDER
    )

    qr.add_data(link)
    qr.make(fit=True)

    matrix = qr.get_matrix()

    print_terminal_qr(matrix, filename)

    img = create_qr_image(matrix, filename)

    return img, link


# ==========================================
# SAVE QR IMAGE
# ==========================================

def save_qr_image(img, filename):

    os.makedirs(SAVE_DIR, exist_ok=True)

    filename = os.path.basename(filename)
    filename = re.sub(r'[<>:"/\\|?*]', "_", filename)

    if not filename.lower().endswith(".png"):
        filename += ".png"

    filepath = os.path.join(SAVE_DIR, filename)

    img.save(filepath, format="PNG")

    return filepath


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    print_qr_banner()

    print("Type 'exit' to close.\n")

    while True:

        link = input(
            f"{YELLOW_TEXT}🔗 Enter Link/URL: {RESET}"
        ).strip()

        if link.lower() in ["exit", "quit"]:
            print("\n👋 Bye bhai! Baad mein Milte hain")
            break

        if not link:
            print("⚠️ Link is empty. Try again.\n")
            continue

        name = input(
            f"📝{YELLOW_TEXT}Enter Name of the QR-Image: {RESET}"
        ).strip()

        if not name:
            name = "my_qr"

        try:

            img, final_link = generate_qr(link, name)

            print("\n" + gradient_text("✅ QR CODE GENERATED!"))

            print(f"📄Filename: {YELLOW_TEXT}{name}{RESET}")

            print(
                f"🔗URL: {YELLOW_TEXT}{final_link}{RESET}"
            )

            while True:

                save_choice = input(
                    "\n" + gradient_text(
                        "💾 SAVE THIS IMAGE? (y/n): "
                    )
                ).strip().lower()

                if save_choice in ["y", "yes"]:

                    filepath = save_qr_image(
                        img,
                        name
                    )

                    print("\n" + gradient_text(
                        "✅ IMAGE SAVED SUCCESSFULLY!"
                    ))

                    print(
                        f"{GREEN_TEXT}📄 File: "
                        f"{os.path.basename(filepath)}{RESET}"
                    )

                    print(
                        f"{GREEN_TEXT}📁 Path: "
                        f"{filepath}{RESET}"
                    )

                    print(
                        f"{GREEN_TEXT}"
                        "📁 Image is saved in Internal Storage."
                        f"{RESET}"
                    )

                    break

                elif save_choice in ["n", "no"]:

                    print(f"🚫{GREEN_TEXT} IMAGE NOT SAVED!{RESET}")
                    print(f"📱{GREEN_TEXT} QR was displayed only in terminal.{RESET}")

                    break

                else:

                    print("⚠️ Please enter Y or N.")

        except Exception as e:

            print(f"\n❌ Error: {e}\n")
            continue

        # ==================================
        # BAZIGARR QR MENU
        # ==================================

        while True:

            print("\n" + gradient_text("=" * 40))
            print(gradient_text("       BAZIGARR QR MENU"))
            print(gradient_text("=" * 40))

            print(gradient_text("1. Next Link 🔗"))
            print(gradient_text("2. Exit ❌"))

            choice = input(
                "\n" + gradient_text("👉 Enter your choice: ")
            ).strip()

            if choice == "1":

                print("\n" + gradient_text(
                    "🔄 Ready for next QR code!"
                ))

                print(gradient_text("-" * 40 + "\n"))
                break

            elif choice == "2":

                print("\n" + gradient_text(
                    "👋 BAZIGARR QR GENERATOR SYESTEM ID CLOSED!"
                ))

                print(f"{YELLOW_TEXT}Bye,BaziGarr Bhai! See you Soon{RESET} ❤️")
                return

            else:

                print("\n" + gradient_text(
                    "⚠️ Invalid choice! Enter 1 or 2."
                ))


if __name__ == "__main__":
    main()
