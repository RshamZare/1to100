# Stopwatch with GUI tkinter
import tkinter as tk
import time

# start_time = time.time()
# end_time = time.time()
# elapsed = end_time - start_time

# print("Welcome to simple Stopwatch!")
# print("Press:")
# print("s = start")
# print("e = end")
# print("q = quit")

# while True:
#     user_input = input("\nEnter your choice(s/e/q): ").lower()

#     if user_input == "s":
#         print("Stopwatch started... press 'e' for lap time/current time")
#         start_time = time.time()

#     elif user_input == "e":
#         end_time = time.time()
#         elapsed = end_time - start_time
#         minutes, seconds = divmod(elapsed, 60)
#         print(f"Elapsed time: {int(minutes)} min {round(seconds, 2)} sec")

#     elif user_input == "q":
#         print("okkii")
#         break

#     else:
#         print("invalid input boi")


import tkinter as tk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.start_time = None
        self.running = False
        self.elapsed_time = 0

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack(pady=20)

        # Buttons
        self.start_btn = tk.Button(root, text="Start", width=10, command=self.start)
        self.start_btn.pack(side="left", padx=10)

        self.stop_btn = tk.Button(root, text="Stop", width=10, command=self.stop)
        self.stop_btn.pack(side="left", padx=10)

        self.reset_btn = tk.Button(root, text="Reset", width=10, command=self.reset)
        self.reset_btn.pack(side="left", padx=10)

        self.update_timer()

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.label.config(text="00:00:00")

    def update_timer(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            mins, secs = divmod(int(self.elapsed_time), 60)
            hours, mins = divmod(mins, 60)
            self.label.config(text=f"{hours:02}:{mins:02}:{secs:02}")
        self.root.after(100, self.update_timer)

# Create and run the app
root = tk.Tk()
app = StopwatchApp(root)
root.mainloop()
