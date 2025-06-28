# Convert-dict

This repository serves two purposes:

1. **Code storage**: Contains code for converting Swedish-English dictionaries from [The People's Dictionary](https://folkets-lexikon.csc.kth.se/folkets/folkets.en.html).
2. **Dictionary releases**: Provides the converted dictionaries in an optimized format.

## Overview

[The People's Dictionary](https://folkets-lexikon.csc.kth.se/folkets/om.en.html) is available in two formats: XML and XDXF. Each format has distinct advantages:

- **XML format**: Contains comprehensive information but lacks audio download URLs
- **XDXF format**: Includes better phonetic symbols and audio URLs but has less detailed content

However, both formats are challenging for software to parse directly.

## Solution

This repository addresses these limitations by:

1. **Merging data**: Combines audio download URLs and phonetic symbols from XDXF with comprehensive data from XML
2. **Format conversion**: Converts the merged dictionary to JSON format for easier processing
3. **Character normalization**: Converts HTML entities (`&quot;` and `&#39;`) to their corresponding characters in the output

## Usage Example

Here's a sample dictionary entry to illustrate the converted format:

```json
"jord": {
    "t": [
        "soil",
        "land"
    ],
    "c": "nn",
    "i": [
        "jorden",
        "jordar"
    ],
    "e": [
        {
            "v": "odlad jord",
            "t": "cultivated soil"
        },
        {
            "v": "äga jord",
            "t": "own land"
        },
        {
            "v": "gräva i jorden",
            "t": "work the land"
        }
    ],
    "id": [
        {
            "v": "falla i god jord (\"tas emot med uppskattning\")",
            "t": "fall on fertile ground (\"be received with appreciation\")"
        }
    ],
    "s": [
        {
            "v": "mull",
            "l": "3.3"
        }
    ],
    "d": [
        "mull, mylla; odlat markområde"
    ],
    "p": "jo:r_d",
    "a": "http://lexin.nada.kth.se/sound/jord.mp3"
}
```

### Field Reference

| Field | Description |
|-------|-------------|
| `t` | Translation |
| `c` | Class (part of speech) |
| `i` | Inflection |
| `e` | Example |
| `id` | Idiom |
| `s` | Synonym |
| `d` | Definition |
| `p` | Phonetic transcription |
| `a` | Audio URL |
| `v` | Value |
| `l` | Level |

### Output Format

By default, the dictionary is saved as compact JSON (without indentation) to minimize file size. To generate human-readable output, set `indent=4` in the `json.dump()` method.

## Acknowledgments

We extend our gratitude to [The People's Dictionary](https://folkets-lexikon.csc.kth.se/folkets/folkets.en.html) for their excellent work. All dictionaries released by this repository are derivative works based on The People's Dictionary.


## License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/2.5/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/2.5/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/2.5/">Creative Commons Attribution-ShareAlike 2.5 Generic License</a>.
