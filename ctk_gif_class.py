#=====================imports
import customtkinter as ctkinter
from PIL import Image


class CTkGIFLabel(ctkinter.CTkLabel):
    def __init__(self, master, gif_path, **kwargs):
        # Extract frames using Pillow
        self._gif = Image.open(gif_path)
        self._frames = []
        for i in range(self._gif.n_frames):
            self._gif.seek(i)
            # Create CTkImage for each frame
            self._frames.append(ctkinter.CTkImage(self._gif.copy(), size=(100, 100)))  # Size can be dynamic
        #----inherit:
        super().__init__(master, image=self._frames[0], **kwargs)
        self._frame_index = 0
        self.initiate_animation()

    #-----------------Animation_fun
    def initiate_animation(self):
        # Cycle through frames
        self._frame_index = (self._frame_index + 1) % len(self._frames)
        self.configure(image=self._frames[self._frame_index])
        # Update based on GIF frame duration (e.g., 100ms)
        self.after(100, self.initiate_animation)
