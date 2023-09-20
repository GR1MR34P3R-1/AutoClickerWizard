# AutoClickWizard

An easy-to-use Python-based auto-clicker program with a graphical user interface (GUI).

![License](https://img.shields.io/badge/License-MIT-red.svg)
![Python Version](https://img.shields.io/badge/Python-3.8-red)

## Table of Contents

- [Auto-Clicker](#auto-clicker)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Hotkeys](#hotkeys)
  - [AutoClickWizard Future Updates](#AutoClickWizard-Future-Updates)
  - [License](#license)
 
## About

Welcome to the AutoClickWizard — your trusted Python companion for automating repetitive clicking tasks effortlessly. Say goodbye to the monotony of repetitive actions and hello to streamlined efficiency.

### Key Highlights:

- Intuitive User Experience: Our user-friendly GUI ensures a hassle-free experience, even for beginners.

- Tailored Clicking: Customize your automation with adjustable click intervals and precise click coordinates, putting you in control of the process.

- Effortless Automation: Whether you're looking to simplify gaming tasks or expedite repetitive actions on your computer, this tool is your time-saving ally.

Unleash the power of automation and reclaim your time with the Auto-Clicker. Get ready to click smarter, not harder!

## Features

- **Intuitive GUI**: A user-friendly graphical user interface makes it easy for users to configure auto-clicking settings.

- **Customizable Clicking**: Set the click interval (in seconds) and specify the number of clicks you want to perform, giving you full control over the automation process.

- **Custom Coordinates**: Enable custom coordinates to click precisely where you want on the screen. Specify X and Y values to automate clicks in specific locations.

- **Fail-Safe Mechanism**: A built-in fail-safe mechanism monitors cursor position and triggers an emergency stop if the cursor approaches screen edges, ensuring safe and reliable auto-clicking.

- **Mouse Cursor Return**: If the mouse cursor moves during auto-clicking, the program automatically returns it to its original position, maintaining precision and accuracy.

- **Hotkeys**: Utilize convenient hotkeys for quick and easy control. Start auto-clicking with the `;` key, stop it with the `,` key, and trigger an immediate emergency stop with the `Esc` key.

- **Event Logging**: The program logs events and errors, helping with troubleshooting and providing a record of auto-clicking activities.

These features make the Auto-Clicker a versatile and user-friendly tool for automating repetitive clicking tasks. Whether you need to streamline tasks in a game or automate actions on your computer, this program offers customization, safety, and convenience.

## Getting Started

Follow these steps to get the Auto-Clicker up and running on your system.

### Prerequisites

Make sure you have the following prerequisites installed:

- Python 3.x
- Required Python libraries (specified in `requirements.txt`)

### Installation

1. Clone this repository:

  ```bash
  git clone https://github.com/GR1MR34P3R-1/AutoClickWizard.git
  ```
2. Navigate to the project directory:
  ```
  cd ACW-AutoClickWizard
  ```
3. Install dependencies:
  ```
  pip install -r requirements.txt
  ```
## Usage

1. Launch the Auto-Clicker GUI by running:
  ```
  python main.py
  ```

2. Configure your auto-clicking preferences:
- Set the click interval (in seconds).
- Specify the number of clicks.
- Optionally, enable custom coordinates and enter X and Y values.

3. Click the "Start" button or use the hotkey ";" to begin auto-clicking.

4. To stop auto-clicking, press the "," key or click the "Stop" button.

5. In case of an emergency, press the "Esc" key to immediately stop auto-clicking.

## Hotkeys
- Start auto-clicking: ;
Stop auto-clicking: ,
Panic button (emergency stop): Esc
Documentation
Visit the Auto-Clicker Documentation for detailed usage instructions and examples.

## AutoClickWizard Future Updates

As the main developer behind AutoClickWizard, I am committed to enhancing and expanding its functionality to provide you with an improved user experience. Here are some exciting features and improvements I plan to implement in future updates:

### Click Point Recording

In an upcoming update, we will introduce the ability to record and save specific click points on your screen. This feature will make it easier to automate tasks that involve interacting with specific elements or locations. Here's what you can expect:

- **Record Click Points**: Simply click anywhere on your screen to record the coordinates of the click.
- **Save and Name Click Sets**: You can save the recorded click points and give them meaningful names for easy reference.
- **Edit and Delete**: Optionally, you'll be able to edit or delete recorded click points as needed.
- **Execute Recorded Clicks**: Run the saved click point sets to automate your tasks efficiently.

### Persistent UI

- **System Tray Icon**: I will introduce a system tray (or taskbar) icon will allow you to minimize the main window while keeping the program running in the background.
- **Access from System Tray**: By clicking the system tray icon, users will be able to swiftly access and interact with the program's UI. Furthermore, a "Persistent Window" mode will be implemented to ensure your UI remains prominently visible regardless of other open windows or tasks.

## License
- This program is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.

## Have a Great Day! 🌟
- 🌟 Have fun exploring the capabilities of AutoClickWizard. If you have any questions or need assistance, don't hesitate to reach out just open a issue ticket. 😊
