# Backend and Remote Access

## Always-on host

A Raspberry Pi named `energy-monitor-pi` runs the monitoring services continuously in Docker. The core services are:

- MQTT broker for ESP32 telemetry
- Telegraf for ingestion and field mapping
- InfluxDB for time-series retention
- Grafana for dashboards and historical queries

The ESP32 publishes a new measurement set every 10 seconds. The system continues collecting data on the local network during an internet outage, provided the ESP32, Wi-Fi router, and Raspberry Pi remain powered.

## Dashboard

Grafana panels display line voltage, frequency, CT current, real power, reactive power, apparent power, power factor, total energy, and time trends. Low-current power-factor and reactive-power values should be interpreted cautiously because noise is significant relative to the measured signal.

![Grafana overview with live electrical measurements and per-channel real-power trends](assets/grafana-overview.png)

![Grafana channel-current, power-factor, reactive-power, and apparent-power panels](assets/grafana-channel-telemetry.png)

These views also serve as the visible query layer over the measurements retained in InfluxDB: Grafana reads the historical series and renders synchronized per-channel trends over the selected time window.

## Remote access

Tailscale provides encrypted private-network access to the Raspberry Pi and Grafana without publishing Grafana directly to the internet. Authorized devices can reach the dashboard using the Pi hostname while Tailscale is connected.

## Remote OTA workflow

The final main-CT calibration was deployed remotely. The development computer created an SSH tunnel to `energy-monitor-pi`, forwarding the ESPHome OTA port from the home-network ESP32. ESPHome then uploaded firmware through the local end of that tunnel.

Only the OTA port was forwarded during that operation. Consequently, firmware upload succeeded even though ESPHome's subsequent attempt to attach to API logs on port 6053 was refused. The `OTA successful` and `Successfully uploaded program` messages confirmed deployment.

## Security practices

- Wi-Fi and MQTT credentials live only in the ignored `secrets.yaml` file.
- `secrets.example.yaml` documents the required keys without real values.
- The public configuration does not contain the MQTT broker's private address.
- Grafana is reached through the private Tailscale network rather than public port forwarding.
- Repository scans should be performed before every public push.
