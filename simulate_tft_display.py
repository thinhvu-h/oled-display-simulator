import matplotlib.pyplot as plt
import numpy as np

class TFTSimulation:
    def __init__(self, width, height, display_size_inch):
        self.width = width
        self.height = height
        self.display_size_inch = display_size_inch
        self.dpi = int(np.sqrt(width**2 + height**2) / display_size_inch)
        self.fig, self.ax = plt.subplots(figsize=(display_size_inch, display_size_inch), dpi=self.dpi)
        self.ax.set_xlim(0, width)
        self.ax.set_ylim(0, height)
        self.ax.invert_yaxis()  # Invert Y-axis to simulate TFT behavior
        self.ax.axis("off")
        self.ax.set_aspect('equal')

         # Set background to black
        self.ax.add_patch(plt.Rectangle((0, 0), width, height, color='black'))


    def draw_line(self, x1, y1, x2, y2, color='white', linewidth=0.3):
        self.ax.plot([x1, x2], [y1, y2], color=color, linewidth=linewidth)

    def draw_rect(self, x, y, w, h, color='white', linewidth=0.3, fill=False):
        if fill:
            self.ax.add_patch(plt.Rectangle((x, y), w, h, color=color))
        else:
            self.ax.add_patch(plt.Rectangle((x, y), w, h, fill=False, edgecolor=color, linewidth=linewidth))

    def draw_text(self, x, y, text, fontsize=10, color='white'):
        self.ax.text(x, y, text, fontsize=fontsize, color=color, verticalalignment='top')

    def display(self):
        plt.show()


class TFTSimulationWithBorder(TFTSimulation):
    def __init__(self, width, height, display_size_inch, border_thickness=5):
        super().__init__(width, height, display_size_inch)
        self.border_thickness = border_thickness

    def draw_border(self, color='black'):
        self.ax.add_patch(plt.Rectangle(
            (-self.border_thickness, -self.border_thickness), 
            self.width + 2 * self.border_thickness, 
            self.height + 2 * self.border_thickness, 
            fill=False, edgecolor=color, linewidth=self.border_thickness
        ))


# Initialize a 240x240 TFT display simulation with 1.14 inches
# tft_sim = TFTSimulation(240, 240, 1.3)

# Example drawings
# tft_sim.draw_line(10, 10, 230, 10, color='red', linewidth=2)  # Horizontal red line
# tft_sim.draw_rect(50, 50, 100, 80, color='blue', linewidth=2)  # Rectangle
# tft_sim.draw_rect(50, 150, 100, 80, color='green', fill=True)  # Filled rectangle
# tft_sim.draw_text(120, 120, "Hello, TFT!", fontsize=12, color='purple')  # Text

# Display the simulated screen
# tft_sim.display()


# Initialize a 240x240 TFT display simulation with 1.14 inches and a border
# tft_sim_border = TFTSimulationWithBorder(240, 240, 1.14, border_thickness=10)

# # Draw border
# tft_sim_border.draw_border(color='black')

# # Display text inside the screen
# tft_sim_border.draw_text(120, 20, "Display Inside", fontsize=12, color='blue')

# # Draw a small rectangle and text on it
# tft_sim_border.draw_rect(80, 100, 80, 40, color='green', linewidth=2, fill=True)
# tft_sim_border.draw_text(120, 120, "Button", fontsize=10, color='white')

# Display the simulated screen
# tft_sim_border.display()

# Adjusting font size and fitting text inside a rectangle

# Initialize a new TFT display simulation
tft_sim_adjusted = TFTSimulationWithBorder(240, 240, 1.3, border_thickness=5)

# Draw border
tft_sim_adjusted.draw_border(color='black')

# Draw a Coin name
tft_sim_adjusted.draw_text(10, 10, "Bitcoin", fontsize=6, color='white')

# Draw a yellow square
rect_x, rect_y, rect_w, rect_h = 10, 30, 50, 50
tft_sim_adjusted.draw_rect(rect_x, rect_y, rect_w, rect_h, color='yellow', linewidth=0.3, fill=False)

# Draw a blue rectangle
rect_x, rect_y, rect_w, rect_h = 75, 50, 50, 30
tft_sim_adjusted.draw_rect(rect_x, rect_y, rect_w, rect_h, color='blue', linewidth=0.3, fill=True)

# Center text inside the rectangle
tft_sim_adjusted.draw_text(80, 55, "update:", fontsize=3, color='white')
tft_sim_adjusted.draw_text(80, 65, "19:52", fontsize=3, color='white')

tft_sim_adjusted.draw_text(140, 30, "PRICE '(usd)':", fontsize=3, color='white')
tft_sim_adjusted.draw_text(145, 45, "100.99", fontsize=3, color='white')
tft_sim_adjusted.draw_text(140, 60, "CHANGE:", fontsize=3, color='white')
tft_sim_adjusted.draw_text(145, 75, "30%", fontsize=3, color='white')

x_coor = 10
x_offset = 210
y_coor = 100
y_offset = 100

x_chart_coor = 35
x_chart_offset = 190
y_chart_coor = 120
y_chart_offset = 100
spacing = 10

# Calculate number of columns and rows
num_columns = x_chart_offset // spacing
num_rows = y_chart_offset // spacing

# draw chart column
for x in range(num_columns+1): # +1 to include the last line
  tft_sim_adjusted.draw_line(x_chart_coor+(x*spacing), y_chart_coor, x_chart_coor+(x*spacing), y_chart_coor+y_chart_offset, color='grey')

# draw chart row
for x in range(num_rows): # +1 to include the last line
  tft_sim_adjusted.draw_line(x_chart_coor, y_chart_coor + (x*spacing), x_chart_coor+x_chart_offset, y_chart_coor + (x*spacing), color='grey')

# draw chart outline
tft_sim_adjusted.draw_line(x_chart_coor,
                           y_chart_coor,
                           x_chart_coor,
                           y_chart_coor + y_chart_offset,
                           color='white')
tft_sim_adjusted.draw_line(x_chart_coor,
                           y_chart_coor + y_chart_offset,
                           x_chart_coor + x_chart_offset,
                           y_chart_coor + y_chart_offset,
                           color='white')

tft_sim_adjusted.draw_text(x_chart_coor, 95, "LAST 12 READINGS", fontsize=4, color='white')
tft_sim_adjusted.draw_text(x_coor, 110, "MAX", fontsize=3, color='orange')
tft_sim_adjusted.draw_text(x_coor, 220, "MIN", fontsize=3, color='orange')

# Display the simulated screen
tft_sim_adjusted.display()

