# APD Module Interface Application User Guide

## Introduction

Welcome to the APD Module Interface Application! This guide will help you get started with the installation, setup, and usage of the application.

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)
4. [COM Port Selection Section](#com-port-selection-section)
5. [Temperature Gauge Chart](#temperature-gauge-chart)
6. [Set Configuration Section](#set-configuration-section)
7. [Send Configuration Section](#send-configuration-section)
8. [High Voltage Reading Progress Bar](#high-voltage-reading-progress-bar)
9. [Terminal Section](#terminal-section)
10. [Temperature and Voltage Graphs](#temperature-and-voltage-graphs)
11. [Contact](#contact)
12. [Conclusion](#conclusion)

## Installation

### For Standart User
- Open APD Module Interface.exe file.

  
### For Developers
#### Prerequisites

- Python 3.8+
- Required Python packages (listed in `requirements.txt`)

#### Steps

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

![Interface Screenshot](https://github.com/user-attachments/assets/478cb85e-2019-4896-8cb3-56d9bfededfd)



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
   

4. **Select the COM Port:**
    - Click on the COM Port Selection Dropdown.
    - A list of available COM ports will appear.
    - Select the COM port corresponding to your APD Module (e.g., COM3, COM4, /dev/ttyUSB0).


   ![COM Port Selection Screenshot](https://github.com/user-attachments/assets/9a530894-626b-4bcc-ab17-31a5dda40603)

   


6. **Refresh Connection:**
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
      
![Temperature Gauge Chart](https://github.com/user-attachments/assets/90f795f5-5b63-4e02-92cf-b58b3f420d7a)



3. **Reading the Temperature:**
    - The current temperature is indicated by the position on the gauge.
    - The exact temperature value be displayed numerically under the gauge.

4. **Monitoring Temperature:**
    - Continuously monitor the gauge to ensure the temperature remains within the safe range.
    - The safe range is typically marked in green.
    - The warning and danger ranges are marked in yellow and red, respectively.

### Actions Based on Temperature Readings

- **Safe Range (Blue):**
  - If the temperature is within the blue range, the APD Module is operating normally.

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


### Set Configuration Section

The Set Configuration Section allows users to configure the necessary parameters for the APD Module's map function. These parameters include minimum and maximum voltage, and minimum and maximum temperature. Users can select an existing configuration file, create a new configuration file manually, or add a configuration file from their local PC.

### Steps to Configure the Parameters

1. **Locate the Set Configuration Section:**
    - Open the APD Module Interface Application.
    - The Set Configuration Section is located in the main window, right to the gauge chart.

2. **Understanding the Configuration Parameters:**
    - **Min Voltage:** The minimum voltage value for the map function.
    - **Max Voltage:** The maximum voltage value for the map function.
    - **Min Temperature:** The minimum temperature value for the map function.
    - **Max Temperature:** The maximum temperature value for the map function.

3. **Select File Dropdown:**
    - Click on the dropdown menu to select an existing configuration file.
    - The dropdown will display a list of available `.txt` configuration files.
    - Select the desired configuration file that contains the necessary values.

   ![Select File Dropdown](https://github.com/user-attachments/assets/5526498d-5223-4f6e-8f56-561a4d5fc28a)



5. **Add File Manually Button:**
    - Click on the "Add File Manually" button to create a new configuration file.
    - A dialog window will appear prompting you to enter the necessary values:
      - Min Voltage
      - Max Voltage
      - Min Temperature
      - Max Temperature
    - Enter the values and save the configuration file.
    - 

![Add File Manually Dialog](https://github.com/user-attachments/assets/f21067b3-5a3b-445a-ae41-c870d45219ea)


 
6. **Add File on PC Button:**
    - Click on the "Add File on PC" button to upload an existing `.txt` configuration file from your local computer.
    - A file browser window will appear.
    - Navigate to the location of the `.txt` file on your computer and select it.
    - The selected file will be added to the list of available configuration files.


### Troubleshooting Configuration Issues

- **File Not Listed in Dropdown:**
  - Ensure the configuration file is saved in the correct directory.
  - Refresh the dropdown menu by reopening the application or clicking a refresh button (if available).

- **Error Loading Configuration File:**
  - Verify the format of the `.txt` file to ensure it contains the necessary values in the correct format.
  - Check for any error messages related to file loading and address the issues accordingly.

By following these steps, you can easily configure the necessary parameters for the APD Module's map function, ensuring accurate and reliable operation.

### Example Configuration File

Here is an example of what a configuration `.txt` file might look like:

```txt
110.0
124.4
10.5
35.6
```

### High Voltage Reading Progress Bar

The High Voltage Reading Progress Bar section visualizes the current high voltage value within its specified limits (minimum to maximum). This helps users monitor the voltage level of the APD Module and ensures it stays within safe operational parameters.

### Steps to Visualize High Voltage Reading

1. **Locate the High Voltage Reading Progress Bar Section:**
    - Open the APD Module Interface Application.
    - The High Voltage Reading Progress Bar is typically displayed prominently on the main window, under the set configuration section.

2. **Understanding the Progress Bar Display:**
    - The progress bar visually represents the current high voltage reading.
    - It displays a filled portion representing the current voltage value within the minimum and maximum limits.
    - The minimum and maximum limits are displayed as markers or labels on the progress bar.

![High Voltage Progress Bar](https://github.com/user-attachments/assets/14da9bd1-1f43-4324-b77e-15b3ffb77215)




### Troubleshooting High Voltage Reading Issues

- **Progress Bar Not Updating:**
  - Ensure the application is receiving real-time high voltage readings.
  - Check for any errors or delays in data acquisition from the APD Module.



### Send Configuration Section

The Send Configuration Section allows users to configure and send parameters to the APD Module for operation. This section includes sliders and double spin boxes for setting minimum and maximum voltage, as well as minimum and maximum temperature values. Additionally, it features buttons for sending the configuration to the serial port and starting the data visualization and experiment.

### Steps to Configure and Send Parameters

1. **Locate the Send Configuration Section:**
    - Open the APD Module Interface Application.
    - The Send Configuration Section is located next to the set configuration section.

2. **Configure Parameters with Sliders and Double Spin Boxes:**
    - Adjust the sliders and double spin boxes to set the following parameters:
      - **Min Voltage:** Adjust the slider or enter a value in the spin box for the minimum voltage.
      - **Max Voltage:** Adjust the slider or enter a value in the spin box for the maximum voltage.
      - **Min Temperature:** Adjust the slider or enter a value in the spin box for the minimum temperature.
      - **Max Temperature:** Adjust the slider or enter a value in the spin box for the maximum temperature.

  ![Send Configuration Sliders and Spin Boxes](https://github.com/user-attachments/assets/3ac7b70e-86f2-40cf-98bf-1ee3e060ff3a)




4. **Send Configuration Button:**
    - Click the "Send Configuration" button to send the configured parameters to the serial port.
    - This action configures the APD Module with the selected values for minimum and maximum voltage, as well as minimum and maximum temperature.

5. **Start Process Button:**
    - Click the "Start Process" button to initiate the data visualization and experiment process.
    - Once clicked, this button disables the configure sliders and double spin boxes to prevent further configuration changes during operation.


### Troubleshooting Configuration Issues

- **Slider or Spin Box Not Updating:**
  - Ensure the application is running correctly and responsive.
  - Check for any error messages related to GUI interaction or serial communication.

- **Unable to Send Configuration:**
  - Verify the serial port connection and settings.
  - Check for any errors or warnings related to serial communication and address them accordingly.


## Terminal Section

The Terminal Section allows users to enter specified commands and receive responses from the APD Module system.

### How to Use the Terminal

1. **Command Input:**
   - Enter commands in the text area below. Commands should follow the specified format.

  ![Terminal Section](https://github.com/user-attachments/assets/ea54766a-3f65-49c8-9d0f-338c19eecc52)



2. **Command Format:**
   - Commands should be entered in the following format:
     ```plaintext
     w/CURRENT_VOLTAGE=(number) - Sets desired voltage to number.
     w/MODE=(number) - Sets operating mode to number.
     w/MIN_TEMP=(number) - Sets minimum temperature threshold to number.
     w/MAX_TEMP=(number) - Sets maximum temperature threshold to number.
     w/MIN_HV=(number) - Sets minimum high voltage threshold to number.
     w/MAX_HV=(number) - Sets maximum high voltage threshold to number.
    
     r/OUTPUT_VOLTAGE - Displays output voltage value from system.
     r/DESIRED_VOLTAGE - Displays desired voltage value.
     r/MIN_TEMP - Displays minimum temperature threshold.
     r/MAX_TEMP - Displays maximum temperature threshold.
     r/MIN_HV - Displays minimum high voltage threshold.
     r/MAX_HV - Displays maximum high voltage threshold.
     r/CURRENT_TEMP - Displays current temperature.
     r/MODE - Displays operating mode.
     r/STATUS - Displays system status.
     r/LED_MODE - Displays LED mode.
     r/MANUFACTURER_ID - Displays manufacturer ID.
     r/DUMP - Displays system information dump.

     /clear - Clears the terminal.
     ```

3. **Terminal Buttons**
   -Send Command Button: Sends the written command with serial port.
   -Dump Button: Displays system information dump.
   -Clear Button: Clears the terminal text.

4. **LED Mode Radio Buttons**
   - Allows user to select the LED mode.

5. **Response Display:**
   - Responses to commands will be displayed in the area below the command input.

   ![Response Display](https://github.com/QuarkOptical/Quark-Optical-APD-Module-Interface/assets/174795941/9bc4025f-69e7-4ef3-a134-37d54d5f5448)


### Example Commands

Here are some example commands you can enter:

- To set the desired voltage:
  ```plaintext
  w/CURRENT_VOLTAGE=115.2
  r/MAX_TEMP
   ```



## Temperature and Voltage Graphs

The Temperature and Voltage Graphs section allows users to visualize temperature and voltage values in real-time using `pyqtgraph`. These graphs provide valuable insights into the APD Module's performance and can be customized with various plot options and export modes.

### Visualizing Temperature and Voltage Values

1. **Locate the Temperature and Voltage Graphs Section:**
   - Open the APD Module Interface Application.
   - The Temperature and Voltage Graphs are typically displayed on the main window.

2. **Understanding the Graph Display:**
   - The graphs show real-time temperature and voltage values plotted over time.
   - Each graph includes axes labels and units for clarity.

![Temperature and Voltage Graphs](https://github.com/user-attachments/assets/cc1b83ac-f79f-48dc-acd4-9fbfdf2ed63b)




### Plot Options

`pyqtgraph` offers several plot options to customize the appearance and behavior of the graphs:

1. **Zooming and Panning:**
   - Users can zoom in and out on the graphs using the mouse wheel.
   - Click and drag to pan across different sections of the graph.

2. **Auto-Range:**
   - Right-click on the graph and select "Auto-Range" to automatically adjust the view to fit all data points within the visible area.

3. **Crosshair and Data Points:**
   - Hover over the graph to see a crosshair and data point values, which help in precisely identifying values at specific points on the graph.

### Export Modes

`pyqtgraph` provides various export modes to save and share graph data:

1. **Export as Image:**
   - Right-click on the graph and select "Export" > "Export Image".
   - Choose the desired format (e.g., PNG, JPEG) and save the image of the current graph view.

2. **Export Data:**
   - Right-click on the graph and select "Export" > "Export Data".
   - Save the data points in a file format like CSV for further analysis or reporting.

3. **Copy to Clipboard:**
   - Right-click on the graph and select "Export" > "Copy Image to Clipboard".
   - Paste the copied image into documents, presentations, or other applications.


### Troubleshooting Graph Issues

- **Graph Not Updating:**
  - Ensure the application is receiving real-time data from the APD Module.
  - Check for any errors in the data acquisition or graph plotting functions.

- **Incorrect Data Display:**
  - Verify the correct mapping of data points to the graph.
  - Ensure the units and scales are correctly configured.

### Contact

If you have any questions, need assistance, or would like to provide feedback, please feel free to reach out to us. We are here to help and ensure you have a smooth experience with our APD Module Interface Application.

#### Contact Information

- **Email:** info@quarkoptical.com
- **Phone:** +90 850 309 98 09
- **Address:** Sanayi, Teknopark Blv No:1/4C İç Kapı No:115, 34906 Pendik/İstanbul

For the latest updates and information, visit our [website](http://www.quarkoptical.com) or follow us on social media.


### Conclusion

Thank you for using the APD Module Interface Application. This user guide aims to provide comprehensive instructions to help you effectively utilize the application's features, from configuring the module and monitoring its performance to using the terminal for command-based interactions.

If you have any questions or encounter any issues, please refer to the troubleshooting sections provided in each part of this guide. For further assistance, feel free to contact our support team.

We hope this application enhances your experience and efficiency in working with the APD Module. Your feedback is valuable to us and helps us improve our products and services.

Happy experimenting!

Best regards,  
The Quark Optical Team
