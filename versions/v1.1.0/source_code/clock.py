import tkinter as tk
from datetime import datetime

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock App")
        self.root.geometry("400x250")  # Tăng kích thước để thêm giao diện stopwatch
        
        # Biến trạng thái
        self.mode = "Clock"  # Chế độ mặc định là Clock
        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0
        
        # Frame cho Clock
        self.clock_frame = tk.Frame(root)
        self.clock_frame.pack(pady=20)
        
        # Label hiển thị thời gian Clock
        self.time_label = tk.Label(self.clock_frame, text="00:00:00:000", font=("Arial", 36))
        self.time_label.pack()
        
        # Frame cho Stopwatch
        self.stopwatch_frame = tk.Frame(root)
        self.stopwatch_frame.pack(pady=10)
        
        # Label hiển thị thời gian Stopwatch
        self.stopwatch_label = tk.Label(self.stopwatch_frame, text="00:00:00:000", font=("Arial", 24))
        self.stopwatch_label.pack()
        
        # Frame cho nút chuyển đổi và điều khiển
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        
        # Nút chuyển đổi chế độ
        self.switch_button = tk.Button(self.button_frame, text="Switch to Stopwatch", command=self.switch_mode)
        self.switch_button.pack(side=tk.LEFT, padx=5)
        
        # Nút điều khiển Stopwatch (mặc định ẩn)
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_stopwatch, state=tk.DISABLED)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop_stopwatch, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_stopwatch, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
        # Bắt đầu cập nhật thời gian Clock
        self.update_clock()
    
    def update_clock(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        milliseconds = str(datetime.now().microsecond // 1000).zfill(3)
        self.time_label.config(text=f"{current_time}:{milliseconds}")
        self.root.after(100, self.update_clock)
    
    def switch_mode(self):
        if self.mode == "Clock":
            self.mode = "Stopwatch"
            self.switch_button.config(text="Switch to Clock")
            self.time_label.pack_forget()  # Ẩn Clock
            self.stopwatch_label.pack()    # Hiển thị Stopwatch
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)
        else:
            self.mode = "Clock"
            self.switch_button.config(text="Switch to Stopwatch")
            self.stopwatch_label.pack_forget()  # Ẩn Stopwatch
            self.time_label.pack()              # Hiển thị Clock
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.DISABLED)
    
    def start_stopwatch(self):
        if not self.is_running:
            self.is_running = True
            if self.start_time is None:
                self.start_time = datetime.now()
            self.update_stopwatch()
    
    def stop_stopwatch(self):
        if self.is_running:
            self.is_running = False
            self.elapsed_time += int((datetime.now() - self.start_time).total_seconds() * 1000)
    
    def reset_stopwatch(self):
        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00:000")
    
    def update_stopwatch(self):
        if self.is_running:
            current_time = datetime.now() - self.start_time
            elapsed_ms = int(current_time.total_seconds() * 1000) + self.elapsed_time
            hours, remainder = divmod(elapsed_ms // 1000, 3600)
            minutes, seconds = divmod(remainder, 60)
            milliseconds = elapsed_ms % 1000
            self.stopwatch_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:03d}")
            self.root.after(100, self.update_stopwatch)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()