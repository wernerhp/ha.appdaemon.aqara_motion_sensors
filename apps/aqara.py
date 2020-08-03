"""
Aqara app for resetting the state of Xiaomi Aqara motion sensors.
"""

import json
import time
import hassapi as hass
import mqttapi as mqtt

MODULE = 'aqara'
CLASS = 'Aqara'

CONF_TIMEOUT = 'timeout'
CONF_MOTION_SENSORS = 'motion_sensors'

DEFAULT_TIMEOUT = 5

class Aqara(hass.Hass):

  def initialize(self):
    """Initialize the Aqara app."""
    motion_sensors = self.args.get(CONF_MOTION_SENSORS, [])

    handles = []
    for entity_id in motion_sensors:
      handle = self.listen_event(self.motion_event, "xiaomi_aqara.motion", entity_id=entity_id)
      handles.append(handle)

  def motion_event(self, event, data, kwargs):	
    """Handle motion event"""
    entity = self.get_state(data.get("entity_id"), attribute='all')
    entity["state"] = "on"
    self.set_state(**entity)

    timeout = self.args.get(CONF_TIMEOUT, DEFAULT_TIMEOUT)
    self.run_in(self.motion_sensor_state_off, timeout, entity=entity)

  def motion_sensor_state_off(self, kwargs):
    """Set motion sensor state to off"""
    entity = kwargs.get("entity")
    if entity is None:
      return
    entity["state"] = "off"
    self.set_state(**entity)
