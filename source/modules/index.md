# Modules Overview

MTDataPro supports multiple geophysical instruments through dedicated modules.

## Supported Instruments

| Instrument | Module | Notes |
|------------|--------|-------|
| Phoenix MTU-5/6 | [Phoenix](modules/phoenix/) | Native .bin/.hdr format |
| Metronix ADU | [Metronix](modules/metronix/) | .SBS, .BLK formats |
| LEMI-417/418 | [LEMI](modules/lemi/) | LEMI binary format |
| ATTS | [ATTS](modules/atts/) | ATTS proprietary format |
| RMT/CASRMT | [RMT](modules/rmt/) | RMT network format |
| MSTS | [MSTS](modules/msts/) | MSTS format support |

## Common Operations

All instrument modules share a common workflow:

1. **Import**: Load raw data files
2. **Preview**: Preview time series before full import
3. **Configure**: Set channel mapping and metadata
4. **Process**: Apply processing pipelines
5. **Export**: Output to standard formats (EDI, J-format)

## Module Configuration

Each module can be individually configured via **Settings → Modules**.
