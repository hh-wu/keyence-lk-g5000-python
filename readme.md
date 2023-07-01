
# LK-G5000 Measurement Fetcher

This Python script is designed to get measurements from a Keyence LK-G5000 Laser Sensor. 

## Prerequisites

Before running this script, please make sure that the following Python libraries are installed:

- `cpppo`

You can install them using pip:

```sh
pip install cpppo
```

## How to Use

### Initialize the connection

Firstly, initialize the connection to the sensor by calling the `init_lk_g5000_connection` function with the IP address of the sensor as the argument:

```python
host = '192.168.6.2'  # replace with your sensor's IP address
conn = init_lk_g5000_connection(host=host)
```

### Get measurements

You can then get measurements by calling the `get_lk_g5000_measurement` function with the connection as the argument:

```python
measurement = get_lk_g5000_measurement(conn)
```

This will return the measurement from the sensor in millimeters.

### Example

Here is an example of using this script to get measurements from the sensor:

```python
if __name__ == '__main__':
    host = '192.168.6.2'  # replace with your sensor's IP address
    conn = init_lk_g5000_connection(host=host)
    for i in range(10):
        print(get_lk_g5000_measurement(conn))
        time.sleep(0.01)
```

This will print out 10 measurements from the sensor, with a delay of 10 milliseconds between each measurement.

## Notes

This script is specifically designed for the Keyence LK-G5000 Laser Sensor and may not work correctly with other models or brands of sensors. Always make sure to test the script in a safe and controlled environment before using it in a production setting.

