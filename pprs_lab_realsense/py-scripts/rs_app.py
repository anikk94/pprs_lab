import tkinter as tk
import subprocess
import sys

class App:
    def __init__(self, root):
        self.root = root
        root.title("realsense launcher tk")
        root.geometry("400x800")

        label = tk.Label(root, text="List of Demos",bg="greenyellow")
        label.pack(fill=tk.X)

        button1 = tk.Button(
            text="ascii art preview",
            command=self.launch_ascii_art
            )
        button1.pack(fill=tk.BOTH, expand=True)

        button2 = tk.Button(
            text="colour depth preview",
            command=self.launch_colour_depth
            )
        button2.pack(fill=tk.BOTH, expand=True)

        button3 = tk.Button(
            text="Align and BGR",
            command=self.launch_align_bgr
            )
        button3.pack(fill=tk.BOTH, expand=True)

        button4 = tk.Button(
            text="advance mode",
            command=self.launch_advance_mode
            )
        button4.pack(fill=tk.BOTH, expand=True)

        button5 = tk.Button(
            text="read bag file",
            command=self.launch_read_bag_file
            )
        button5.pack(fill=tk.BOTH, expand=True)

        button6 = tk.Button(
            text="save PLY",
            command=self.launch_save_ply
            )
        button6.pack(fill=tk.BOTH, expand=True)

        button7 = tk.Button(
            text="frame queue management",
            command=self.launch_frame_queue
            )
        button7.pack(fill=tk.BOTH, expand=True)

        button15 = tk.Button(
            text="pointcloud openCV",
            command=self.launch_pc_opencv
            )
        button15.pack(fill=tk.BOTH, expand=True)

        button16 = tk.Button(
            text="pointcloud pyglet",
            command=self.launch_pc_pyglet
            )
        button16.pack(fill=tk.BOTH, expand=True)

    def launch_ascii_art(self):
        try:
            print("[Launcher] realsense_tut_1.py")
            subprocess.Popen([sys.executable, 'realsense_tut_1.py'])
        except Exception as e:
            print(f"exception launching colour preview {e}")
    def launch_colour_depth(self):
        try:
            print("[Launcher] realsense_tut_2.py")
            subprocess.Popen([sys.executable, 'realsense_tut_2.py'])
        except Exception as e:
            print(f"exception launching colour preview {e}")
    def launch_align_bgr(self):
        try:
            print("[Launcher] realsense_tut_3.py")
            subprocess.Popen([sys.executable, 'realsense_tut_3.py'])
        except Exception as e:
            print(f"exception launching colour preview {e}")
        
    def launch_advance_mode(self):
        try:
            print("[Launcher] realsense_tut_4.py")
            subprocess.Popen([sys.executable, 'realsense_tut_4.py'])
        except Exception as e:
            print(f"exception launching colour preview {e}")
        
    def launch_read_bag_file(self):
        try:
            print("[Launcher] realsense_tut_5.py")
            subprocess.Popen([sys.executable, 'realsense_tut_5.py'])
        except Exception as e:
            print(f"exception launching colour preview {e}")
        
    def launch_save_ply(self):
        try:
            print("[Launcher] realsense_tut_6.py")
            subprocess.Popen([sys.executable, 'realsense_tut_6.py'])
        except Exception as e:
            print(f"exception launching colour preview {e}")
    def launch_frame_queue(self):
        try:
            print("[Launcher] realsense_tut_7.py")
            subprocess.Popen([sys.executable, 'realsense_tut_7.py'])
        except Exception as e:
            print(f"exception launching colour preview {e}")
        
    def launch_pc_opencv(self):
        try:
            print("[Launcher] realsense_tut_15.py")
            subprocess.Popen([sys.executable, 'realsense_tut_15.py'])
        except Exception as e:
            print(f"exception launching colour preview {e}")
        
    def launch_pc_pyglet(self):
        try:
            print("[Launcher] realsense_tut_16.py")
            subprocess.Popen([sys.executable, 'realsense_tut_16.py'])
        except Exception as e:
            print(f"exception launching colour preview {e}")
        




if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
        
