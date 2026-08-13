\# Six-Channel AC Energy Monitor



ESP32-based AC energy monitor using a CircuitSetup six-channel ATM90E32 board and split-core current transformers.



\## Features



\- Six current-measurement channels

\- RMS voltage and current

\- Real power (W)

\- Reactive power (VAR)

\- Apparent power (VA)

\- Power factor

\- 60 Hz line-frequency measurement

\- Total current, total real power, and daily energy

\- Live ESPHome web interface

\- OTA firmware updates



\## Hardware



\- CircuitSetup six-channel energy-meter board

\- 2× ATM90E32 metering ICs

\- ESP32 DevKitC

\- 4× SCT-013-000 100 A/50 mA CTs

\- 2× SCT-016 120 A/40 mA CTs reserved for mains monitoring

\- 9 VAC voltage-reference adapter

\- Clamp meter

\- AC line splitter

\- Tower fan test load



\## Architecture



The CT supplies a scaled current waveform, while the 9 VAC adapter supplies a safe, scaled representation of the AC voltage waveform. The ATM90E32 samples both signals and calculates electrical quantities. The ESP32 reads the metering ICs over SPI and publishes measurements through ESPHome.



\## Calibration



\### Current



The SCT-013-000 was compared with a clamp meter at three tower-fan speeds.



Initial measurements:



| Speed | Clamp meter | Energy Monitor | Error |

|---|---:|---:|---:|

| 3 | 0.885 A | 0.855 A | -3.4% |

| 2 | 0.740 A | 0.710 A | -4.1% |

| 1 | 0.660 A | 0.630 A | -4.5% |



The current calibration gain was changed from:



```yaml

current\_cal: '27518'

to:



current\_cal: '28646'

After calibration, the monitor matched the clamp meter to the displayed 0.01 A resolution at all three speeds.



All six board inputs were validated using the same SCT. Four individual SCT-013-000 sensors were then compared, with measurements remaining within approximately 4% of the clamp-meter reference.



Voltage



Reference comparison:



Clamp meter: 122.5 V

Energy Monitor before calibration: 129.3 V

Error: +5.55%



The voltage calibration gain was changed from:



voltage\_cal: '7305'



to:



voltage\_cal: '6921'



After calibration, the monitor reported 122.6–122.7 V.



Tower-Fan Experiment



Measurements were logged at 10-second intervals.



Condition	Current	Real Power	Reactive Power	Apparent Power	PF

Fan off	0.08 A	-0.07 W	-9.90 VAR	10.02 VA	N/A

Speed 1	0.67 A	80.00 W	-16.20 VAR	81.80 VA	0.98

Speed 2	0.74 A	90.63 W	-8.03 VAR	91.05 VA	1.00

Speed 3	0.90 A	105.58 W	30.87 VAR	110.03 VA	0.96



The results show that the fan's electrical behavior changes with its speed-control configuration. Speeds 1 and 2 appeared slightly capacitive, while speed 3 appeared inductive.



Power-Triangle Verification



The measurements satisfy approximately:



S² = P² + Q²

PF = P / S



For speed 3:



P = 105.58 W

Q = 30.87 VAR

S = 110.03 VA

PF = 0.96

Troubleshooting

Current present but watts and frequency were zero



Observed:



Current: approximately 0.87 A

Real power: approximately 0 W

Frequency: 0 Hz



Cause: the 9 VAC voltage-reference adapter was unplugged. The CT current path remained operational, but the meter had no voltage waveform for calculating frequency, phase relationship, or real power.



Firmware calibration appeared unchanged



Cause: duplicate YAML files existed in different directories. VS Code edited one copy while ESPHome compiled another.



Solution: verified the exact build input using:



findstr /n "current\_cal" energy\_meter.yaml



The active configuration was confirmed as:



C:\\energy-monitor\\energy\_meter.yaml

No-load measurement floor



With the fan off, CT6 reported approximately 0.08 A and 10 VA while real power remained near zero. Low-current VA, VAR, and PF readings therefore require thresholding or offset calibration.



Files

energy\_meter.yaml — active ESPHome configuration

energy\_meter\_calibrated\_backup.yaml — known-good backup

fan\_off\_baseline\_raw.txt — no-load log

fan\_speed1\_raw.txt — fan speed 1 log

fan\_speed2\_raw.txt — fan speed 2 log

fan\_speed3\_raw.txt — fan speed 3 log

fan\_test\_summary.csv — summarized results

plot\_fan\_test.py — analysis and plotting script

fan\_test\_results.png — generated results plot

Safety



CTs were installed only around single insulated conductors during bench testing. No work was performed on exposed energized conductors. Panel installation should be completed only using appropriate PPE, procedures, and qualified supervision.



Current Status



Completed:



Six-channel functional validation

Current calibration

Voltage calibration

Individual SCT comparison

Real, reactive, and apparent-power measurements

Power-factor testing

Raw data logging

Python visualization



Not yet completed:



SCT-016 mains-CT calibration

Electrical-panel installation

Long-term time-series database and dashboard deployment

