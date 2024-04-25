import time

class TrafficLight:
  """
  Represents a traffic light with states (red, yellow, green) and durations.
  """
  def __init__(self, red_duration, yellow_duration, green_duration):
    self.red_duration = red_duration
    self.yellow_duration = yellow_duration
    self.green_duration = green_duration
    self.current_state = "red"

  def change_state(self, new_state):
    """
    Changes the traffic light state and prints a message.
    """
    print(f"Traffic light changing to {new_state}.")
    self.current_state = new_state

  def run(self):
    """
    Simulates the traffic light cycle by changing states and waiting for durations.
    """
    while True:
      # Red light
      self.change_state("red")
      time.sleep(self.red_duration)

      # Yellow light
      self.change_state("yellow")
      time.sleep(self.yellow_duration)

      # Green light
      self.change_state("green")
      time.sleep(self.green_duration)

def create_traffic_light(red_duration=3, yellow_duration=2, green_duration=4):
  """
  Creates a TrafficLight object with default or custom durations.
  """
  return TrafficLight(red_duration, yellow_duration, green_duration)

def main():
  """
  Sets up and runs the traffic light simulation.
  """
  # Create a traffic light with custom durations (optional)
  # traffic_light = create_traffic_light(red_duration=5, yellow_duration=1, green_duration=3)

  traffic_light = create_traffic_light()  # Use default durations
  traffic_light.run()

if __name__ == "__main__":
  main()
