import os
import pyautogui
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import keyboard
import traceback
import logging  # Added for logging

# Configure the logging
log_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "auto_clicker.log")
logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Default values for the click interval, number of clicks, and mouse return position
default_click_interval = 0.1
default_num_clicks = 0

# Function to handle errors and log them to a file
def handle_error(error_message):
    try:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] Error: {error_message}"
        logging.error(log_message)

        result_label.config(text=f"An error occurred: {error_message}")
    except Exception as e:
        print(f"Error handling error: {e}")

# Function to log events
def log_event(event_message):
    try:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {event_message}"
        logging.info(log_message)
    except Exception as e:
        print(f"Error logging event: {e}")

# Function to perform the auto-clicking
def auto_click():
    global stop_clicking, custom_mode
    try:
        num_clicks_str = num_clicks_entry.get()
        if not num_clicks_str.isdigit():
            raise ValueError("Invalid input for Number of Clicks")

        num_clicks = int(num_clicks_str)
        click_interval = float(click_interval_entry.get())
        original_position = pyautogui.position()

        for _ in range(num_clicks):
            if stop_clicking:
                break

            if custom_mode:  # Only click if in custom mode
                x = int(custom_x_entry.get())
                y = int(custom_y_entry.get())
                pyautogui.click(x, y)
                time.sleep(click_interval)
            else:
                pyautogui.click()
                time.sleep(click_interval)

                current_position = pyautogui.position()
                if current_position != original_position:
                    pyautogui.moveTo(*original_position)

            check_for_fail_safe()  # Check for fail-safe condition

    except Exception as e:
        error_message = str(e)
        handle_error(error_message)
    else:
        result_label.config(text="Auto-clicking completed successfully!")
    finally:
        stop_clicking = False
        start_stop_label.config(text="Stopped")

def check_for_fail_safe():
    screen_width, screen_height = pyautogui.size()
    cursor_x, cursor_y = pyautogui.position()

    # Define a margin to consider cursor near screen edges
    margin = 10

    # Check if cursor is near any of the screen edges
    if (
        cursor_x <= margin
        or cursor_x >= screen_width - margin
        or cursor_y <= margin
        or cursor_y >= screen_height - margin
    ):
        log_event("Fail-safe triggered: Cursor near screen edges")
        stop_auto_clicking()

def start_auto_clicking():
    global stop_clicking
    stop_clicking = False
    start_stop_label.config(text="Running")
    auto_click_thread = threading.Thread(target=auto_click)
    auto_click_thread.start()

def stop_auto_clicking():
    global stop_clicking
    stop_clicking = True

def panic_button():
    global stop_clicking
    stop_clicking = True
    start_stop_label.config(text="Stopped (Panic Button)")

def on_closing():
    if not stop_clicking:
        result = messagebox.askokcancel("Confirm Exit", "Auto-clicking is still running. Are you sure you want to exit?")
        if not result:
            return
    app.destroy()

# Create the main application window
app = tk.Tk()
app.title("Auto-Clicker")
app.protocol("WM_DELETE_WINDOW", on_closing)  # Handle application close event

# Create and configure widgets
click_interval_label = ttk.Label(app, text="Click Interval (seconds):")
click_interval_label.grid(row=0, column=0, padx=10, pady=5)
click_interval_entry = ttk.Entry(app)
click_interval_entry.grid(row=0, column=1, padx=10, pady=5)
click_interval_entry.insert(0, str(default_click_interval))

num_clicks_label = ttk.Label(app, text="Number of Clicks:")
num_clicks_label.grid(row=1, column=0, padx=10, pady=5)
num_clicks_entry = ttk.Entry(app)
num_clicks_entry.grid(row=1, column=1, padx=10, pady=5)
num_clicks_entry.insert(0, str(default_num_clicks))

# Checkbox to enable custom coordinates
custom_coordinates_var = tk.BooleanVar()
custom_coordinates_checkbox = ttk.Checkbutton(app, text="Use Custom Coordinates", variable=custom_coordinates_var)
custom_coordinates_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Entry fields for custom coordinates
custom_x_label = ttk.Label(app, text="Custom X:")
custom_x_label.grid(row=3, column=0, padx=10, pady=5)
custom_x_entry = ttk.Entry(app)
custom_x_entry.grid(row=3, column=1, padx=10, pady=5)

custom_y_label = ttk.Label(app, text="Custom Y:")
custom_y_label.grid(row=4, column=0, padx=10, pady=5)
custom_y_entry = ttk.Entry(app)
custom_y_entry.grid(row=4, column=1, padx=10, pady=5)

start_stop_label = ttk.Label(app, text="Stopped", foreground="red", font=("Arial", 16))
start_stop_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

usage_button = ttk.Button(app, text="How to Use", command=lambda: show_usage_dialog())
usage_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

agreement_button = ttk.Button(app, text="User Agreement", command=lambda: show_agreement_dialog())
agreement_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(app, text="")
result_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

# Global variables to control auto-clicking and custom mode
stop_clicking = True
custom_mode = False

# Set the pyautogui fail-safe to move the mouse to the top-left corner if it gets out of control
pyautogui.FAILSAFE = True

# Start listening for keypress events
keyboard.add_hotkey(';', start_auto_clicking)
keyboard.add_hotkey(',', stop_auto_clicking)
keyboard.add_hotkey('esc', panic_button)

# Function to show usage dialog
def show_usage_dialog():
    usage_text = """
    Usage Instructions:
    
    1. Set the Click Interval (in seconds) and Number of Clicks.
    2. Check the 'Use Custom Coordinates' checkbox if you want to specify custom coordinates.
    3. Enter custom X and Y coordinates if the checkbox is checked.
    4. Press the ';' key to start auto-clicking.
    5. Press the ',' key to stop auto-clicking.
    """
    messagebox.showinfo("How to Use", usage_text)

# Function to show the user agreement dialog
def show_agreement_dialog():
    agreement_text = """
    User Agreement:
    
    By using this software, you agree to the following terms and conditions:
    
    1. This software is provided as-is, without any warranties or guarantees.
    2. The author of this software is not responsible for any damage or loss caused by its use.
    3. You are solely responsible for how you use this software.
    4. Do not use this software for any malicious or harmful purposes.
    
    If you do not agree to these terms, please do not use this software.
    """
    messagebox.showinfo("User Agreement", agreement_text)

# Start the Tkinter main loop
app.mainloop()
