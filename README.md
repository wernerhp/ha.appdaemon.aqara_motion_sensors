[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

<a href="https://www.buymeacoffee.com/wernerhp" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

# Aqara Motion Sensors

## Introduction
An AppDaemon app to reset Xiaomi Aqara motion sensors after a given timeout.

[This hardware motion sensor hack](https://livebywant.tistory.com/13?category=703455) allows motion to be detected every 5 seconds, however it still takes 300 seconds to reset the state to off.
This app will motions sensor state to off after a given timeout, e.g. 5 seconds.  Together your Xiaomi Aqara motion sensors can toggle state on or off every 5 seconds.

## Installation
Download the `aqara` directory from inside the `apps` directory to your local `apps` directory, then configure the `aqara` module in `apps.yaml`.

## App configuration
```yaml
aqara:
  module: aqara
  class: Aqara
  timeout: 5
  motion_sensors:
    - binary_sensor.bathroom_motion_sensor
    - binary_sensor.bedroom_motion_sensor
    - binary_sensor.kitchen_motion_sensor
    - binary_sensor.lounge_motion_sensor
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | | The module name of the app.
`class` | False | string | | The name of the Class.
`timeout` | True | int | 5 | Timeout after which motion sensor state is set to off.
`motion_sensors` | False | list | | A list of motion sensor entity_ids.