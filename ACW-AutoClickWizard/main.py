import os
import pyautogui
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import keyboard
import traceback
import logging
import sys

# Configure the logging
log_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "auto_clicker.log")
logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Function to handle errors and log them to a file
def handle_error(error_message, context=None):
    try:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] Error: {error_message}"
        if context:
            log_message += f"\nContext: {context}"
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

# Function to validate input
def validate_input(cps_str, num_clicks_str):
    try:
        cps = float(cps_str)
        num_clicks = int(num_clicks_str)
        if cps <= 0:
            raise ValueError("CPS must be greater than 0.")
        if num_clicks <= 0:
            raise ValueError("Number of clicks must be greater than 0.")
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")

# Function to validate custom coordinates
def validate_custom_coordinates(x_str, y_str):
    try:
        x = int(x_str)
        y = int(y_str)
        screen_width, screen_height = pyautogui.size()
        if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
            raise ValueError("Invalid custom coordinates.")
    except ValueError as e:
        raise ValueError(f"Invalid custom coordinates: {e}")

# Function to perform the auto-clicking
def auto_click():
    global stop_clicking, custom_mode
    try:
        num_clicks_str = num_clicks_entry.get()
        cps_str = cps_scale.get()
        validate_input(cps_str, num_clicks_str)
        
        num_clicks = int(num_clicks_str)
        desired_cps = float(cps_str)
        
        # Validate custom coordinates if in custom mode
        if custom_mode:
            custom_x_str = custom_x_entry.get()
            custom_y_str = custom_y_entry.get()
            validate_custom_coordinates(custom_x_str, custom_y_str)
        
        original_position = pyautogui.position()

        for _ in range(num_clicks):
            if stop_clicking:
                break

            if custom_mode:  # Only click if in custom mode
                x = int(custom_x_entry.get())
                y = int(custom_y_entry.get())
                pyautogui.click(x, y)

                # No sleep time needed when trying to achieve high CPS
            else:
                pyautogui.click()

                # No sleep time needed when trying to achieve high CPS

                current_position = pyautogui.position()
                if current_position != original_position:
                    pyautogui.moveTo(*original_position)

            check_for_fail_safe()  # Check for fail-safe condition

    except Exception as e:
        error_message = str(e)
        handle_error(error_message, context="Auto-clicking error")
    else:
        result_label.config(text="Auto-clicking completed successfully!")
    finally:
        stop_clicking = False
        start_stop_label.config(text="Stopped", foreground="red")  # Set text color to red

# Function to check for fail-safe condition
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

# Function to start auto-clicking
def start_auto_clicking():
    global stop_clicking, auto_click_thread, program_running
    if program_running:
        messagebox.showwarning("Warning", "Auto-clicking is already running. Stop it before starting again.")
        return
    
    try:
        cps_str = cps_scale.get()
        num_clicks_str = num_clicks_entry.get()
        validate_input(cps_str, num_clicks_str)
        
        stop_clicking = False
        start_stop_label.config(text="Running", foreground="green")  # Set text color to green
        auto_click_thread = threading.Thread(target=auto_click)
        
        # Add error handling for thread execution
        try:
            auto_click_thread.start()
        except Exception as e:
            handle_error(f"Error starting auto-click thread: {e}")
            messagebox.showerror("Thread Start Error", f"Error starting auto-click thread: {e}")

        # Update the program state
        program_running = True
    except ValueError as e:
        handle_error(str(e), context="Input validation error")
        messagebox.showerror("Input Validation Error", f"Invalid input: {e}")
    except Exception as e:
        handle_error(f"An unexpected error occurred: {e}", context="Start auto-clicking error")
        messagebox.showerror("Start Auto-Clicking Error", f"An unexpected error occurred: {e}")

# Function to stop auto-clicking
def stop_auto_clicking():
    global stop_clicking, auto_click_thread, program_running
    if stop_clicking:
        return
    
    stop_clicking = True
    start_stop_label.config(text="Stopping...", foreground="orange")  # Set text color to orange

    # Check if the auto-click thread is not the current thread before joining
    if auto_click_thread != threading.current_thread():
        # Wait for the auto-clicking thread to finish with a timeout
        timeout_seconds = 5  # Adjust the timeout as needed
        auto_click_thread.join(timeout=timeout_seconds)

        if auto_click_thread.is_alive():
            # Thread didn't stop gracefully, forcefully terminate it
            handle_error("Auto-clicking thread didn't stop gracefully, forcefully terminating...", context="Thread termination")
            auto_click_thread._stop()  # Use thread termination as a last resort

    # Update the program state
    program_running = False

# Function to handle the panic button
def panic_button():
    global stop_clicking, program_running
    stop_clicking = True
    start_stop_label.config(text="Stopped (Panic Button)", foreground="red")  # Set text color to red
    
    # Update the program state
    program_running = False

# Function to handle application closing
def on_closing():
    try:
        if program_running:
            result = messagebox.askokcancel("Confirm Exit", "Auto-clicking is still running. Are you sure you want to exit?")
            if not result:
                return
        app.destroy()
    except Exception as e:
        handle_error(f"Error during application closing: {e}", context="Application closing error")

# Function to enable/disable custom coordinates input fields
def toggle_custom_coordinates():
    global custom_mode
    if program_running:
        messagebox.showwarning("Warning", "Auto-clicking is already running. Stop it before changing custom coordinates mode.")
        custom_coordinates_var.set(custom_mode)  # Reset the checkbox state
        return
    
    try:
        custom_mode = custom_coordinates_var.get()
        if custom_mode:
            custom_x_entry.config(state=tk.NORMAL)
            custom_y_entry.config(state=tk.NORMAL)
        else:
            custom_x_entry.config(state=tk.DISABLED)
            custom_y_entry.config(state=tk.DISABLED)
    except Exception as e:
        handle_error(f"Error toggling custom coordinates mode: {e}")
        messagebox.showerror("Custom Coordinates Toggle Error", f"Error toggling custom coordinates mode: {e}")

# Function to show usage dialog
def show_usage_dialog():
    try:
        usage_text = """
        Usage Instructions:
    
    1. Set the Clicks Per Second (CPS) using the slider (up to 10 CPS).
    2. Set the Number of Clicks.
    3. Check the 'Use Custom Coordinates' checkbox if you want to specify custom coordinates.
    4. Enter custom X and Y coordinates if the checkbox is checked.
    5. Press the ';' key to start auto-clicking.
    6. Press the ',' key to stop auto-clicking.
        """
        messagebox.showinfo("How to Use", usage_text)
    except Exception as e:
        handle_error(f"Error showing usage dialog: {e}")
        messagebox.showerror("Usage Dialog Error", f"Error showing usage dialog: {e}")

# Function to show user agreement dialog
def show_user_agreement():
    try:
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
    except Exception as e:
        handle_error(f"Error showing user agreement dialog: {e}")
        messagebox.showerror("User Agreement Dialog Error", f"Error showing user agreement dialog: {e}")

# Function to show the "About" dialog
def show_about_dialog():
    try:
        about_text = """
        About Auto-Clicker v1.0

    Developed by GR1MR34P3R-1

    Program History:
    Auto-Clicker was created to stress test software projects by automating repetitive clicks. It started as a minimalist terminal-based tool a few months ago and has evolved into a user-friendly GUI application.
        """
        messagebox.showinfo("About Auto-Clicker", about_text)
    except Exception as e:
        handle_error(f"Error showing 'About' dialog: {e}")
        messagebox.showerror("About Dialog Error", f"Error showing 'About' dialog: {e}")

# Global variables to control auto-clicking and custom mode
stop_clicking = True
custom_mode = False
program_running = False  # New state variable for tracking program state

# Global variable for the auto-clicking thread
auto_click_thread = None

# Set the pyautogui fail-safe to move the mouse to the top-left corner if it gets out of control
pyautogui.FAILSAFE = True

# Start listening for keypress events
try:
    keyboard.add_hotkey(';', start_auto_clicking)
    keyboard.add_hotkey(',', stop_auto_clicking)
    keyboard.add_hotkey('esc', panic_button)
except Exception as e:
    handle_error(f"Error registering hotkeys: {e}")
    messagebox.showerror("Hotkey Registration Error", f"Hotkeys could not be registered: {e}")

# Set up a global exception handler to capture unhandled exceptions
def global_exception_handler(exctype, value, traceback_obj):
    error_message = f"Unhandled exception of type {exctype}: {value}"
    handle_error(error_message)
    sys.__excepthook__(exctype, value, traceback_obj)  # Call the default exception handler

sys.excepthook = global_exception_handler

# Create the main application window
app = tk.Tk()
app.title("Auto-Clicker")
app.protocol("WM_DELETE_WINDOW", on_closing)  # Handle application close event

# Create and configure widgets
cps_label = ttk.Label(app, text="Clicks Per Second (CPS):")
cps_label.grid(row=0, column=0, padx=10, pady=5)
cps_scale = ttk.Scale(app, from_=1, to=10, orient="horizontal", length=200)  # Limit the slider to 10 CPS
cps_scale.grid(row=0, column=1, padx=10, pady=5)
cps_value_label = ttk.Label(app, text=f"Selected CPS: {int(cps_scale.get())}")
cps_value_label.grid(row=0, column=2, padx=10, pady=5)

num_clicks_label = ttk.Label(app, text="Number of Clicks:")
num_clicks_label.grid(row=1, column=0, padx=10, pady=5)
num_clicks_entry = ttk.Entry(app)
num_clicks_entry.grid(row=1, column=1, padx=10, pady=5)

# Checkbox to enable custom coordinates
custom_coordinates_var = tk.BooleanVar()
custom_coordinates_checkbox = ttk.Checkbutton(app, text="Use Custom Coordinates", variable=custom_coordinates_var, command=toggle_custom_coordinates)
custom_coordinates_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Entry fields for custom coordinates
custom_x_label = ttk.Label(app, text="Custom X:")
custom_x_label.grid(row=3, column=0, padx=10, pady=5)
custom_x_entry = ttk.Entry(app, state=tk.DISABLED)
custom_x_entry.grid(row=3, column=1, padx=10, pady=5)

custom_y_label = ttk.Label(app, text="Custom Y:")
custom_y_label.grid(row=4, column=0, padx=10, pady=5)
custom_y_entry = ttk.Entry(app, state=tk.DISABLED)
custom_y_entry.grid(row=4, column=1, padx=10, pady=5)

start_stop_label = ttk.Label(app, text="Stopped", foreground="red", font=("Arial", 16))
start_stop_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

usage_button = ttk.Button(app, text="How to Use", command=lambda: show_usage_dialog())
usage_button.grid(row=8, column=0, padx=10, pady=10)

user_agreement_button = ttk.Button(app, text="User Agreement", command=show_user_agreement)
user_agreement_button.grid(row=8, column=1, padx=10, pady=10)

about_button = ttk.Button(app, text="About", command=show_about_dialog)
about_button.grid(row=8, column=2, padx=10, pady=10)

result_label = ttk.Label(app, text="")
result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Function to update the CPS value label
def update_cps_label(value):
    cps_value_label.config(text=f"Selected CPS: {int(value)}")

# Set the update function for the CPS slider
cps_scale.config(command=lambda value: update_cps_label(cps_scale.get()))

# Start the Tkinter main loop
app.mainloop()
