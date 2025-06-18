import tkinter as tk
from PIL import Image, ImageTk
import os

class ImageSlider:
    def __init__(self, root, image_folder):
        self.root = root
        self.root.title("Image Slider")

        if not os.path.exists(image_folder):
            print(f"❌ Folder not found: {image_folder}")
            return

        self.image_paths = [
            os.path.join(image_folder, img)
            for img in os.listdir(image_folder)
            if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
        ]

        if not self.image_paths:
            print("❌ No images found in the folder.")
            return

        self.index = 0
        self.img_label = tk.Label(root)
        self.img_label.pack()

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="<< Prev", command=self.prev_image).pack(side="left")
        tk.Button(btn_frame, text="Next >>", command=self.next_image).pack(side="right")

        self.load_image(self.index)

        # ✅ Start auto-slide
        self.auto_slide_delay = 2000  # milliseconds (2000 ms = 2 seconds)
        self.start_auto_slide()

    def load_image(self, index):
        img = Image.open(self.image_paths[index])
        img = img.resize((500, 400), Image.Resampling.LANCZOS)
        self.tk_img = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.tk_img)

    def next_image(self):
        self.index = (self.index + 1) % len(self.image_paths)
        self.load_image(self.index)

    def prev_image(self):
        self.index = (self.index - 1) % len(self.image_paths)
        self.load_image(self.index)

    def start_auto_slide(self):
        self.next_image()
        self.root.after(self.auto_slide_delay, self.start_auto_slide)

if __name__ == '__main__':
    root = tk.Tk()
    slider = ImageSlider(root, image_folder="images")
    root.mainloop()

