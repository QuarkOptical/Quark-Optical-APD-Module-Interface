# APD Module Interface Application User Guide

## Introduction

Welcome to the APD Module Interface Application! This guide will help you get started with the installation, setup, and usage of the application.

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)
4. [Troubleshooting](#troubleshooting)
5. [Contact](#contact)

## Installation

### Prerequisites

- Python 3.8+
- Required Python packages (listed in `requirements.txt`)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/QuarkOptical/Quark-Optical-APD-Module-Interface.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Quark-Optical-APD-Module-Interface
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```


## Configuration

### Connecting the APD Module

Connect the APD Module to your system via the serial port.


### Open the application:

1. 
    ```bash
    python main.py
    ```
2.  run main.py manually


## Usage

![Interface Screenshot](https://github.com/QuarkOptical/Quark-Optical-APD-Module-Interface/assets/174795941/0a425ec3-91f0-410b-b695-099509501fad)


## COM Port Selection Section

The COM Port Selection section allows you to specify the serial port to which your APD Module is connected. This is a crucial step to ensure proper communication between the application and the module.

### Steps to Select a COM Port

1. **Locate the COM Port Selection Dropdown:**
    - Open the APD Module Interface Application.
    - The COM Port Selection Dropdown is located at the top left of the main window.

2. **Identify the Correct COM Port:**
    - Ensure your APD Module is connected to your computer via the USB/Serial cable.
    - Note the COM port number assigned to your device. You can find this in your system’s Device Manager (Windows) or using the `ls /dev/tty.*` command (Mac/Linux).

   ![Device Manager Screenshot](https://github.com/QuarkOptical/Quark-Optical-APD-Module-Interface/assets/174795941/a813c30b-9777-4880-a101-569d6c7902cb)

3. **Select the COM Port:**
    - Click on the COM Port Selection Dropdown.
    - A list of available COM ports will appear.
    - Select the COM port corresponding to your APD Module (e.g., COM3, COM4, /dev/ttyUSB0).

    ![COM Port Selection Screenshot](images/com_port_selection_screenshot.png)

4. **Refresh Connection:**
    -You can refresh the connected ports by clicking the "Refresh" button.


## Temperature Gauge Chart

The Temperature Gauge Chart section provides users with real-time temperature readings from the APD Module. This gauge allows users to monitor the temperature of the module, ensuring it operates within safe and optimal conditions.

### Steps to Use the Temperature Gauge Chart

1. **Locate the Temperature Gauge Chart:**
    - Open the APD Module Interface Application.
    - The Temperature Gauge Chart is prominently displayed on the main window, top left on the main window.

2. **Understand the Gauge Display:**
    - The gauge displays the current temperature of the APD Module.
    - It includes a needle that points to the current temperature value on a circular scale.
    - The scale is color-coded to indicate safe, warning, and danger temperature ranges.
      
![Temperature Gauge Chart](https://github.com/QuarkOptical/Quark-Optical-APD-Module-Interface/assets/174795941/da20d9af-b44f-4bf5-b10b-7a52518b1bbd)

3. **Reading the Temperature:**
    - The current temperature is indicated by the position on the gauge.
    - The exact temperature value be displayed numerically under the gauge.

4. **Monitoring Temperature:**
    - Continuously monitor the gauge to ensure the temperature remains within the safe range.
    - The safe range is typically marked in green.
    - The warning and danger ranges are marked in yellow and red, respectively.

### Actions Based on Temperature Readings

- **Safe Range (Green):**
  - If the temperature is within the green range, the APD Module is operating normally.

- **Warning Range (Yellow):**
  - If the temperature enters the yellow range, consider taking preventive actions to avoid overheating, such as improving ventilation or reducing the module's workload.

- **Danger Range (Red):**
  - If the temperature reaches the red range, immediate action is required. Turn off the APD Module to prevent damage and investigate the cause of the high temperature.

### Troubleshooting Temperature Issues

- **Gauge Not Updating:**
  - Ensure the APD Module is properly connected and the application is running.
  - Check for any error messages related to data acquisition.

- **Unusually High or Low Readings:**
  - Verify the sensor's connection and placement on the APD Module.
  - Ensure the module is not exposed to external temperature extremes.



- **Danger Range Example:**
    ![Danger Range](images/temperature_gauge_danger.png)

By following these guidelines, you can effectively monitor the temperature of your APD Module, ensuring it operates within safe and optimal conditions.

