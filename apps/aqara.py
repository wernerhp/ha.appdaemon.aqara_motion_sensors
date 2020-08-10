import json
import time
import hassapi as hass

MODULE = 'aqara'
CLASS = 'Aqara'

CONF_TIMEOUT = 'timeout'
CONF_MOTION_SENSORS = 'motion_sensors'

DEFAULT_TIMEOUT = 5

class Aqara(hass.Hass):

  def initialize(self):
    """Initialize the Aqara app."""
    motion_sensors = self.args.get(CONF_MOTION_SENSORS, [])

    for entity_id in motion_sensors:
      self.listen_event(self.motion_sensor_state_on, "xiaomi_aqara.motion", entity_id=entity_id)

  def motion_sensor_state_on(self, event, data, kwargs):
    """Set motion sensor state to on"""
    entity_id = kwargs.get("entity_id")
    if not entity_id:
      return
    state = self.get_state(entity_id, attribute="all")
    self.set_state(entity_id, state="on", attributes=state.get("attributes", {}))

    timeout = self.args.get(CONF_TIMEOUT, DEFAULT_TIMEOUT)
    self.run_in(self.motion_sensor_state_off, timeout, entity_id=entity_id)

  def motion_sensor_state_off(self, kwargs):
    """Set motion sensor state to off"""
    entity_id = kwargs.get("entity_id")
    if not entity_id:
      return
    state = self.get_state(entity_id, attribute="all")
    self.set_state(entity_id, state="off", attributes=state.get("attributes", {}))
