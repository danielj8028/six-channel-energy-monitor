# Installation

## Installed configuration

The completed system uses two SCT-016 split-core sensors for the two incoming service conductors and four SCT-013-000 sensors for selected branch circuits. CT polarity was verified from the sign of real power. The ESP32 and metering board are housed separately from energized conductors, while CT leads route from the panel to the enclosure.

The 9 VAC adapter serves two functions: it powers the measurement assembly and provides the isolated voltage waveform used for phase-sensitive power calculations. If it is disconnected, a CT may still indicate current while voltage, frequency, and real-power calculations become unavailable or invalid.

## Commissioning checks

1. Confirm each split-core CT is fully latched around exactly one insulated conductor.
2. Confirm every CT lead is connected before the monitored conductor is energized, following the CT manufacturer's requirements.
3. Verify approximately 120–123 V and 60 Hz from the voltage-reference channel.
4. Switch known loads on and off and confirm the expected channel responds.
5. Reverse a CT only if a known consuming load produces consistently negative real power.
6. Compare installed main-channel current with a reference clamp meter under stable load.
7. Confirm MQTT ingestion, database writes, and Grafana timestamps before leaving the system unattended.

## Safety boundary

This page records the completed project's commissioning logic; it is not a procedure for working in an energized panel. Opening a main breaker does not de-energize the utility-side service conductors or lugs. Electrical-panel work should be performed only by a qualified person using applicable codes, permits, PPE, test equipment, and manufacturer instructions.

CTs with current-output secondaries can develop hazardous voltage if their secondary is opened while installed on an energized conductor. Sensor datasheets and the metering-board documentation govern the permitted connection sequence.
