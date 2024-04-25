import unittest
from traffic_light_sim import TrafficLight, create_traffic_light

class TestTrafficLightSim(unittest.TestCase):

  def test_traffic_light_init(self):
    """
    Tests that TrafficLight objects are created with expected attributes.
    """
    light = TrafficLight(2, 1, 3)
    self.assertEqual(light.red_duration, 2)
    self.assertEqual(light.yellow_duration, 1)
    self.assertEqual(light.green_duration, 3)
    self.assertEqual(light.current_state, "red")

  def test_change_state(self):
    """
    Tests that change_state() updates the current state and prints a message.
    """
    with self.capture_output() as output:
      light = TrafficLight(1, 1, 1)
      light.change_state("yellow")
    self.assertEqual(light.current_state, "yellow")
    self.assertIn("Traffic light changing to yellow.", output.getvalue())

  def test_create_traffic_light(self):
    """
    Tests that create_traffic_light() creates a TrafficLight object with default or custom durations.
    """
    default_light = create_traffic_light()
    self.assertEqual(default_light.red_duration, 3)  # Check default values
    self.assertEqual(default_light.yellow_duration, 2)
    self.assertEqual(default_light.green_duration, 4)

    custom_light = create_traffic_light(5, 1, 3)
    self.assertEqual(custom_light.red_duration, 5)  # Check custom values
    self.assertEqual(custom_light.yellow_duration, 1)
    self.assertEqual(custom_light.green_duration, 3)

  # Mocked test case for run() - due to time.sleep and infinite loop
  def test_run_mocked(self):
    """
    Mocked test for run() to verify state changes (without actual sleep).
    """
    light = TrafficLight(0, 0, 0)  # Set durations to 0 for quick state changes
    light.change_state = self.spy(light, "change_state")  # Mock change_state method

    light.run()

    # Verify state changes were called in the expected order
    invocations = light.change_state.mock_calls
    self.assertEqual(invocations[0][1][0], "red")
    self.assertEqual(invocations[1][1][0], "yellow")
    self.assertEqual(invocations[2][1][0], "green")

if __name__ == '__main__':
  unittest.main()
