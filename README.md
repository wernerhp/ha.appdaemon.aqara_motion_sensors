# Aqara Motion Sensors

## Introduction
An AppDaemon app to reset Xiaomi Aqara motion sensors after a given timeout.

[This hardware motion sensor hack](https://livebywant.tistory.com/13?category=703455) allows motion to be detected every 5 seconds, however it still takes 300 seconds to reset the state to off.
This app will motions sensor state to off after a given timeout, e.g. 5 seconds.  Together your Xiaomi Aqara motion sensors can toggle state on or off every 5 seconds.

## HACS Installation
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)
1. Make sure you have the option "Enable AppDaemon apps discovery & tracking". This is located in: Configuration -> Integrations -> HACS (options).
2. Restart HA
3. Go to HACS -> Automation -> search for "Aqara Motion Sensors" and install it.
4. Follow app configuration section.  

<a href="https://www.buymeacoffee.com/wernerhp" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

> ℹ️ NOTE: If you also ControllerX, then you might have naming conflicts within HACS.  To get around this you can rename either of the two integrations to e.g. `aqaramotion` in the `custom_components` folder and do the same in your `apps.yaml`.

## Manual Installation
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

## Configuration Guide
- [Как настроить? \ How to configure it?](https://github.com/wernerhp/appdaemon_aqara_motion_sensors/issues/8#issue-784614244)
