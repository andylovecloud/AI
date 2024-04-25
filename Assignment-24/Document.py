
Traffic Light Simulation in Python
This document explains the code for a Python program that simulates a basic traffic light system. The code utilizes classes and functions to model the traffic light behavior and its cycle.

Components:

TrafficLight Class:

Represents a traffic light with attributes for:
Red light duration (seconds)
Yellow light duration (seconds)
Green light duration (seconds)
Current state (string, initially "red")
Methods:
__init__(self, red_duration, yellow_duration, green_duration): Initializes the object with the provided durations.
change_state(self, new_state): Changes the current state of the traffic light and prints a message indicating the new state.
run(self): Simulates the traffic light cycle by repeatedly changing states and waiting for the corresponding durations using time.sleep().
create_traffic_light Function:

Takes optional arguments for red, yellow, and green durations (default values are used if not provided).
Returns a new TrafficLight object with the specified or default durations.
main Function:

Sets up the simulation by:
Calling create_traffic_light to create a TrafficLight object (optionally with custom durations).
Invoking the run method on the created object to start the traffic light cycle.
Code Flow:

The main function starts the program and creates a TrafficLight object using create_traffic_light.
The TrafficLight object is initialized with default or custom durations based on the arguments passed to create_traffic_light.
The run method of the TrafficLight object is called.
Inside the run method:
The traffic light starts in the "red" state.
The change_state method is called to update the current state to "red" and print a message.
time.sleep pauses the program for the red light duration.
The cycle continues by changing to "yellow", waiting for the yellow light duration, then switching to "green" and waiting for the green light duration.
This loop continues indefinitely, simulating the ongoing traffic light cycle.
Unit Testing:

The code includes unit test cases (not shown in this document) to verify the functionality of different parts like object creation, state changes, and object creation with custom durations. A mocked test is used for run to check state changes without relying on actual sleep durations.

Overall, this code demonstrates the use of classes, functions, and time manipulation in Python to simulate a basic traffic light system.