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
  - [Recent Updates](#recent-updates)
  - [Report Issues](#report-issues)
  - [License](#license)
  - [Wrapping Up](#wrapping-up)

## About

Hey there, welcome to AutoClickWizard – your trusty Python-driven auto-clicker. Wave goodbye to the dull grind of repetitive chores and dive into a world of super-smooth efficiency.

## Features

- **Intuitive GUI**: A user-friendly graphical user interface makes it easy to configure auto-clicking settings.

- **Customizable Clicking**: Set the click interval (in seconds) and specify the number of clicks you want to perform, giving you full control over the automation process.

- **Custom Coordinates**: Enable custom coordinates to click precisely where you want on the screen. Specify X and Y values to automate clicks in specific locations.

- **Fail-Safe Mechanism**: A built-in fail-safe mechanism monitors cursor position and triggers an emergency stop if the cursor approaches screen edges, ensuring safe and reliable auto-clicking.

- **Mouse Cursor Return**: If the mouse cursor moves during auto-clicking, the program automatically returns it to its original position, maintaining precision and accuracy.

- **Hotkeys**: Utilize convenient hotkeys for quick and easy control. Start auto-clicking with the `;` key, stop it with the `,` key, and trigger an immediate emergency stop with the `Esc` key.

- **Event Logging**: The program logs events and errors, helping with troubleshooting and providing a record of auto-clicking activities.

## Getting Started

Follow these steps to get AutoClickWizard up and running on your system.

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

  ```bash
  cd ACW-AutoClickWizard
  ```

3. Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

## Usage

1. Launch the Auto-Clicker GUI by running:

  ```bash
  python main.py
  ```

2. Configure your auto-clicking preferences:
- Set the Clicks Per Second (CPS) using the slider (up to 10 CPS).
- Set the Number of Clicks.
- Optionally, enable custom coordinates and enter `X` and `Y` values.

3. Click the "Start" button or use the hotkey `;` to begin auto-clicking.

4. To stop auto-clicking, press the `,` key.

5. In case of an emergency, press the `Esc` key to immediately stop auto-clicking.

## Hotkeys

- Start auto-clicking: `;`
- Stop auto-clicking: `,`
- Panic button (emergency stop): `Esc`

## Recent Updates 
~~**V1.0.0 (9/20/23):**~~

~~- Basic Auto-Clicking: The program allows you to specify a click interval (in seconds) and a number of clicks. It will then perform the specified number of clicks with the given interval.~~

~~- Custom Coordinates: You can enable custom coordinates mode to specify the X and Y coordinates where the clicks should occur.~~

~~- Error Handling: Basic error handling is in place to handle simple input errors.~~

~~- Fail-Safe Mechanism: A simple fail-safe mechanism is implemented to stop auto-clicking if the mouse cursor approaches the screen edges.~~

~~- User Agreement: The program includes a user agreement dialog to inform users of their responsibilities. About Dialog: An "About" dialog provides some information about the program's history and key features.~~

- <ins>**V2.0.0 (9/30/2023):**</ins>

- **Input Validation:** Added input validation for the CPS (Clicks Per Second) and the number of clicks to ensure valid inputs.

- **Custom Coordinates Validation:** Implemented validation for custom X and Y coordinates when in custom mode, ensuring coordinates are within the screen boundaries.

- **Program State Management:** Introduced the `program_running` variable to track whether the auto-clicking program is running, preventing you from starting it when it's already running and handling the "Panic Button" appropriately.

- **Thread Handling:** Added error handling for thread execution when starting auto-clicking, displaying error messages for thread-related issues and terminating the thread if it doesn't stop gracefully.

- **Hotkey Registration Error Handling:** Provided error handling for registering hotkeys to help you understand if hotkeys could not be registered.

- **Global Exception Handler:** Implemented a global exception handler to capture unhandled exceptions and log them, ensuring the program's stability.

- **Fixed Issue:** Addressed and fixed the **"cannot join current thread" issue.**


## VirusTotal Scan Results

The safety and security of AutoClickWizard is our priority. To ensure the programs reliability we have conducted a virus scan using VirusTotal, a recognized online service that analyzes files and URLs for potential threats.

You can check out the results by clicking on this VirusTotal [Scan Link](https://www.virustotal.com/gui/file/b9f9f5bed3552c38f1ab373c4f7cb3e82f59c691bceab3c45406663889dd0cc6/detection).

Please keep in mind that these results are provided by the VirusTotal community and various antivirus engines. We encourage users to review the results for their peace of mind.

If you have any questions or concerns, about the security of AutoClickWizard please don't hesitate to reach out to the [developer](https://github.com/GR1MR34P3R-1/AutoClickerWizard/issues). I will be more, than happy to assist you.


## Report Issues

If you encounter any issues or have suggestions for improvements, please [report them on GitHub](https://github.com/GR1MR34P3R-1/AutoClickerWizard/issues).

You can also check the [existing issues](https://github.com/GR1MR34P3R-1/AutoClickerWizard/issues) to see if your concern has already been addressed.

## License

- This program is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.

## Wrapping Up

Thanks for choosing AutoClickWizard! 🚀 I hope you enjoy its features and find it useful for your tasks. If you have any questions, feedback, or encounter any issues, please don't hesitate to [report them](#issue-reporting) on our GitHub repository.

Have a fantastic day, and happy clicking! 🌟
