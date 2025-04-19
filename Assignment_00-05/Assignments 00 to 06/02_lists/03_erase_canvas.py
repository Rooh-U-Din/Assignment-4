import tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

CELL_SIZE = 40
ERASER_SIZE = 20

class Canvas:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("Eraser Canvas")
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.mouse_x = 0
        self.mouse_y = 0
        self.last_click = (0, 0)
        self.canvas.bind("<Motion>", self._on_mouse_move)
        self.canvas.bind("<Button-1>", self._on_mouse_click)
        self.click_received = False

    def _on_mouse_move(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def _on_mouse_click(self, event):
        self.last_click = (event.x, event.y)
        self.click_received = True

    def wait_for_click(self):
        while not self.click_received:
            self.root.update()
        self.click_received = False

    def get_last_click(self):
        return self.last_click

    def get_mouse_x(self):
        return self.mouse_x

    def get_mouse_y(self):
        return self.mouse_y

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="white")

    def set_color(self, rect, color):
        self.canvas.itemconfig(rect, fill=color)

    def moveto(self, item, x, y):
        bbox = self.canvas.bbox(item)
        if bbox:
            curr_x, curr_y = bbox[0], bbox[1]
            dx = x - curr_x
            dy = y - curr_y
            self.canvas.move(item, dx, dy)

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def update(self):
        self.root.update()


def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.set_color(overlapping_object, 'white')


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
    
    canvas.wait_for_click()
    
    last_click_x, last_click_y = canvas.get_last_click()
    
    eraser = canvas.create_rectangle(
        last_click_x,
        last_click_y,
        last_click_x + ERASER_SIZE,
        last_click_y + ERASER_SIZE,
        'pink'
    )
    
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        erase_objects(canvas, eraser)
        canvas.update()
        time.sleep(0.05)


if __name__ == '__main__':
    main()
