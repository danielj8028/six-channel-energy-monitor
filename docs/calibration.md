# Calibration

## Gain calculation

Current gain was corrected with simultaneous reference measurements:

\[
G_{new}=G_{old}\left(\frac{I_{reference}}{I_{monitor}}\right)
\]

Multiple stable readings were used where possible rather than calibrating from a single low-current point.

## SCT-013-000 branch sensors

The initial gain was `27518`. A tower fan provided three repeatable load levels.

| Setting | Clamp meter | Monitor | Ratio |
|---|---:|---:|---:|
| Speed 1 | 0.660 A | 0.630 A | 1.0476 |
| Speed 2 | 0.740 A | 0.710 A | 1.0423 |
| Speed 3 | 0.885 A | 0.855 A | 1.0351 |

The deployed branch-sensor gain is `28646`. All six inputs were separately checked by moving the same CT and load between channels before permanent installation.

## SCT-016 main sensors

The main sensors were calibrated after installation so the test current was large enough to reduce the relative influence of noise and quantization.

### CT1

| Trial | Monitor | Clamp meter | Correction ratio |
|---|---:|---:|---:|
| 1 | 18.37 A | 27.49 A | 1.4965 |
| 2 | 23.40 A | 34.69 A | 1.4825 |

The two independently calculated gains were approximately 62,521 and 61,958. Their average is approximately 62,240; the deployed value is `62250`.

### CT2

| Monitor | Clamp meter | Correction ratio | Deployed gain |
|---:|---:|---:|---:|
| 4.78 A | 6.76 A | 1.4142 | `59095` |

## Voltage

| Measurement | Value |
|---|---:|
| Reference meter | 122.5 V |
| Monitor before calibration | 129.3 V |
| Initial gain | `7305` |
| Final gain | `6921` |
| Monitor after calibration | 122.6–122.7 V |

## Polarity verification

A positive-consuming load should report positive real power. Negative real power during early bench tests was corrected by reversing CT orientation. Very small negative readings near zero load can still occur because phase error and noise dominate at low current.

## Bench dataset

The `data/` directory contains the raw 10-second samples, processed summary, and plotting script used for the tower-fan experiment. The source dataset is retained so the plotted results can be audited and regenerated.
