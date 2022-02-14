from tkinter import Tk, Entry, Button, Label, Frame, Canvas, BOTH
from math import sin, cos, pi, sqrt
from numpy import arange
import wheelbuild


class Draw(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Spoke Calculator")
        self.pack(fill=BOTH, expand=1)

        # define coordinates of hub and spoke holes
        flange_diameter = 55
        effective_rim_diameter = 590
        spoke_count = 24
        cross = 2

        # define the angle in degrees of each hole in the hub/rim
        spokes_drive = arange(-180.0 / spoke_count, -360, -720.0 / spoke_count)
        spokes_nondrive = arange(180.0 / spoke_count, 360, 720.0 / spoke_count)

        # convert angle to 2 dimensional coordinates based on rim and hub flange diameter
        hub_coords_drive = []
        hub_coords_nondrive = []
        rim_coords_drive = []
        rim_coords_nondrive = []
        for i in range(len(spokes_drive)):
            hub_coords_drive.append([flange_diameter / 2 * sin(spokes_drive[i]
                                    * pi/180), flange_diameter / 2 * cos(spokes_drive[i] * pi / 180)])
            rim_coords_drive.append([effective_rim_diameter / 2 * sin(
                spokes_drive[i] * pi / 180), effective_rim_diameter / 2 * cos(spokes_drive[i] * pi / 180)])
        for i in range(len(spokes_nondrive)):
            hub_coords_nondrive.append([flange_diameter / 2 * sin(
                spokes_nondrive[i] * pi / 180), flange_diameter / 2 * cos(spokes_nondrive[i] * pi / 180)])
            rim_coords_nondrive.append([effective_rim_diameter / 2 * sin(
                spokes_nondrive[i] * pi / 180), effective_rim_diameter / 2 * cos(spokes_nondrive[i] * pi / 180)])

        # canvas dimensions
        global canvas_x
        global canvas_y
        canvas_x = 900
        canvas_y = 750
        center = [canvas_x / 2, canvas_y / 2]
        oval_size = 2  # radius of hub spoke holes in the drawing

        # draw the spoke holes in the hub
        # driveside spoke holes are in black and nondriveside are in red
        canvas = Canvas(self)
        for i in range(len(spokes_drive)):
            x = hub_coords_drive[i][0]
            y = hub_coords_drive[i][1]
            canvas.create_oval(center[0] + x - oval_size, center[1] - y - oval_size,
                               center[0] + x + oval_size, center[1] - y + oval_size, fill="black")
        for i in range(len(spokes_nondrive)):
            x = hub_coords_nondrive[i][0]
            y = hub_coords_nondrive[i][1]
            canvas.create_oval(center[0] + x - oval_size, center[1] - y - oval_size,
                               center[0] + x + oval_size, center[1] - y + oval_size, fill="red")

        # draw the rim and hub circles
        canvas.create_oval(center[0] - effective_rim_diameter / 2, center[1] - effective_rim_diameter / 2,
                           center[0] + effective_rim_diameter / 2, center[1] + effective_rim_diameter / 2, width=3)
        canvas.create_oval(center[0] - flange_diameter / 2 - 5, center[1] - flange_diameter / 2 - 5,
                           center[0] + flange_diameter / 2 + 5, center[1] + flange_diameter / 2 + 5, width=2)

        # draw each spoke
        for i in range(len(spokes_drive)):
            if i % 2 == 0:
                canvas.create_line(center[0] + hub_coords_drive[(i + cross) % len(spokes_drive)][0], center[1]-hub_coords_drive[(i + cross) % len(spokes_drive)][1],
                                   center[0] + rim_coords_drive[i][0],
                                   center[1] - rim_coords_drive[i][1], width=2)
            else:
                canvas.create_line(center[0] + hub_coords_drive[(i - cross) % len(spokes_drive)][0], center[1]-hub_coords_drive[(i - cross) % len(spokes_drive)][1],
                                   center[0] + rim_coords_drive[i][0],
                                   center[1] - rim_coords_drive[i][1], width=2)
        for i in range(len(spokes_nondrive)):
            if i % 2 == 0:
                canvas.create_line(center[0] + hub_coords_nondrive[(i + cross) % len(spokes_nondrive)][0], center[1] - hub_coords_nondrive[(i + cross) % len(spokes_nondrive)][1],
                                   center[0] + rim_coords_nondrive[i][0],
                                   center[1] - rim_coords_nondrive[i][1], width=2, fill="#ed5353")
            else:
                canvas.create_line(center[0] + hub_coords_nondrive[(i - cross) % len(spokes_nondrive)][0], center[1] - hub_coords_nondrive[(i - cross) % len(spokes_nondrive)][1],
                                   center[0] + rim_coords_nondrive[i][0],
                                   center[1] - rim_coords_nondrive[i][1], width=2, fill="#ed5353")

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    draw = Draw()
    root.geometry(str(canvas_x) + "x" + str(canvas_y))
    root.mainloop()


if __name__ == "__main__":
    main()
