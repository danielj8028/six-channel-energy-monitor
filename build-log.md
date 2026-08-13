\# Smart Home Energy Monitor Build Log



\## Bench Validation — CT1/CT2/CT3



Date: 2026-08-02



Setup:

\- ESP32 mounted to CircuitSetup 6-channel energy meter board

\- ESPHome firmware flashed and web dashboard accessible

\- 9VAC AC-AC adapter used as voltage reference

\- SCT-013-000 current transformer used for bench testing

\- Lamp cord separated into individual insulated conductors

\- CT clamped around one insulated conductor only



Results:

\- CT1 showed approximately 0.11 A and 8.8 W with lamp ON

\- CT1 dropped to approximately 0 A / 0 W with lamp OFF

\- CT2 showed similar readings when the same CT was moved to CT2

\- CT3 showed similar readings when the same CT was moved to CT3

\- Frequency reading held at 60.0 Hz

\- Initial negative watt reading was corrected by flipping CT orientation



Conclusion:

\- ESP32, CircuitSetup board, ATM90E32 IC1, voltage reference, and CT channels 1–3 are functional.

\- Bench test confirms current and real power readings respond correctly to load on/off state.



Next Steps:

\- Validate CT4, CT5, and CT6

\- Test a larger load for clearer current/power readings

\- Begin calibration using a known load or clamp meter

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Full 6-Channel Bench Validation



Date: 2026-08-02



Test:

\- Moved the same SCT-013-000 CT across all six CT inputs.

\- Used the same lamp load and split single-conductor cord setup for each channel.

\- Took screenshots for lamp ON and lamp OFF states on CT1 through CT6.



Results:

\- CT1, CT2, CT3, CT4, CT5, and CT6 all responded to lamp ON/OFF state.

\- Lamp ON produced nonzero current and watt readings.

\- Lamp OFF dropped readings near zero.

\- CT orientation was corrected so watts were positive.



Conclusion:

\- All six CT input channels are functional.

\- Both ATM90E32 metering ICs are communicating with the ESP32.

\- The CircuitSetup board, ESPHome firmware, voltage reference, and CT sensing path are bench validated.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Larger Load Test — Tower Fan



Date: 2026-08-02



Setup:

\- Tower fan plugged into a split extension cord test setup

\- SCT-013-000 CT connected to CT1

\- CT clamped around one separated insulated conductor

\- 9VAC adapter used as voltage reference

\- ESPHome web dashboard used to monitor readings



Results:

\- Tower fan ON: CT1 measured approximately 0.88 A and 108.8 W

\- Tower fan OFF: CT1 dropped near 0 A / 0 W

\- Frequency remained at 60.0 Hz



Conclusion:

\- The energy monitor responds correctly to a larger real-world appliance load.

\- Current and wattage readings scale upward compared with the small lamp test.

