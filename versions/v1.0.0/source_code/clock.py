import tkinter as tk
from datetime import datetime

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock App")
        self.root.geometry("400x200")  # Kích thước cửa sổ
        
        # Label hiển thị thời gian
        self.time_label = tk.Label(root, text="00:00:00:000", font=("Arial", 36))
        self.time_label.pack(pady=20)
        
        # Bắt đầu cập nhật thời gian
        self.update_time()
    
    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        milliseconds = str(datetime.now().microsecond // 1000).zfill(3)  # Chuyển microsecond thành millisecond
        self.time_label.config(text=f"{current_time}:{milliseconds}")
        self.root.after(100, self.update_time)  # Cập nhật mỗi 100ms

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()
