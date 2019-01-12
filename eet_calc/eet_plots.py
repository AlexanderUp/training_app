# encoding:utf-8
# plotted graphics for eet

import matplotlib.pyplot as plt
import numpy as np

import sys

try:
    import eet
except ImportError as err:
    print('Can\'t import eet.py')
    print('Error: {}'.format(err))
    sys.exit()
else:
    print('Import successfull!')


# constant humidity
def plot1():
    temperatures = np.arange(-20.0, 40.0, 10.0)
    wind_velocities = np.arange(0.0, 20.5, .5)
    humidity = 70
    fig = plt.figure('Constant humidity')
    fig.add_subplot()
    plt.title('Relative humidity 70%')
    plt.grid(True)
    plt.xlabel('Wind velocity, m/s')
    plt.ylabel('eet, degrees of C')
    for temperature in temperatures:
        res = [round(eet.eet(temperature, wind_velocity, humidity), 1) for wind_velocity in wind_velocities]
        plt.plot(wind_velocities, res, label='{} degrees'.format(temperature))
    plt.legend()
    plt.show()
    return None

# constant temperature
def plot2():
    temperature = 20
    wind_velocities = np.arange(0.0, 20.5, .5)
    humidities = np.arange(0.0, 120.0, 20.0)
    fig = plt.figure('Constant temperature')
    fig.add_subplot()
    plt.title('Ambient temperature 20 degrees of C')
    plt.grid(True)
    plt.xlabel('Wind velocity, m/s')
    plt.ylabel('eet, degrees of C')
    for humidity in humidities:
        res = [round(eet.eet(temperature, wind_velocity, humidity), 1) for wind_velocity in wind_velocities]
        plt.plot(wind_velocities, res, label='humidity {}%'.format(humidity))
    plt.legend()
    plt.show()
    return None

# constant temperature but different formulas used
def plot3():
    temperature = 20
    wind_velocities = np.arange(0.0, 20.5, .5)
    humidity = 70
    fig = plt.figure('Constant temperature but different formulas')
    fig.add_subplot()
    plt.title('Ambient temperature 20 degrees of C')
    plt.grid(True)
    plt.xlabel('Wind velocity, m/s')
    plt.ylabel('eet, degrees of C')
    res = [round(eet.eet(temperature, wind_velocity, humidity), 1) for wind_velocity in wind_velocities]
    res2 = [round(eet.eet2(temperature, wind_velocity, humidity), 1) for wind_velocity in wind_velocities]
    plt.plot(wind_velocities, res, label='eet used')
    plt.plot(wind_velocities, res2, label='eet2 used')
    plt.legend()
    plt.show()

# constant wind
def plot4():
    temperatures = np.arange(-30.0, 45.0, 5.0)
    wind_velocity = 5.0
    humidities = np.arange(0.0, 120.0, 20.0)
    fig = plt.figure('Constant wind')
    fig.add_subplot()
    plt.title('Wind 5.0 m/s')
    plt.grid(True)
    plt.xlabel('ambient temperature, degrees of C')
    plt.ylabel('eet, degrees of C')
    for humidity in humidities:
        res = [round(eet.eet(temperature, wind_velocity, humidity), 1) for temperature in temperatures]
        plt.plot(temperatures, res, label='humidity {}%'.format(humidity))
    plt.legend()
    plt.show()
    return None


if __name__ == '__main__':
    plot1()
    # plot2()
    # plot3()
    # plot4()
