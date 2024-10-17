import os
import tkinter as tk
from tkinter import messagebox

# Function to clean PUBG Mobile (Gameloop) files and registry entries
def clean_pubg():
    try:
        # Killing processes related to Gameloop
        os.system('taskkill /f /im appmarket.exe')
        os.system('taskkill /f /im androidemulator.exe')
        os.system('taskkill /f /im QMEmulatorService.exe')
        os.system('taskkill /f /im adb.exe')

        # Here you can add your specific registry and file deletion commands
        os.system('reg delete HKCU\\Software\\Tencent /f')
        os.system('reg delete HKLM\\SOFTWARE\\WOW6432Node\\Tencent /f')
        os.system('reg delete HKLM\\SYSTEM\\ControlSet001\\Services\\QMEmulatorService /f')
        os.system('reg delete HKLM\\SYSTEM\\ControlSet001\\Services\\aow_drv /f')

        # Add commands to delete files related to Gameloop
        os.system('del "C:\\Program Files\\txgameassistant" /s /q')
        os.system('del "D:\\Program Files\\txgameassistant" /s /q')
        os.system('del "C:\\Users\\PC MILOUD\\AppData\\Local\\Tencent" /s /q')

        messagebox.showinfo("HEM PUBG Cleaner", "Cleaning completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("HEM PUBG Mobile Cleaner from Morocco")
root.geometry("400x200")

# Add labels and buttons
label = tk.Label(root, text="Welcome to HEM PUBG Cleaner Tool", font=("Helvetica", 14))
label.pack(pady=10)

info_label = tk.Label(root, text="Click the button below to clean Gameloop and PUBG files")
info_label.pack(pady=5)

clean_button = tk.Button(root, text="Clean PUBG", command=clean_pubg, width=20, height=2)
clean_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
