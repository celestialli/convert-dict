# Convert-dict

This repository stores code for converting dictionaries from [The People's Dictionary](https://folkets-lexikon.csc.kth.se/folkets/folkets.en.html) and releases the converted dictionaries.

## Details

[The People's Dictionary](https://folkets-lexikon.csc.kth.se/folkets/om.en.html) can be downloaded in 2 formats: XML and XDXF. The XML format contains more information but does not include audio download URLs, while the XDXF format has better phonetic symbols. However, both XML and XDXF formats are difficult for software to parse directly. 

This repository combines audio download URLs and phonetic symbols from the XDXF format with the comprehensive data from the XML dictionary, then converts the merged dictionary into JSON format for easier processing.

### Example

We'll use a dictionary entry as an example to explain how to read the converted dictionary:

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
    "id": {
        "v": "falla i god jord (\"tas emot med uppskattning\")",
        "t": "fall on fertile ground (\"be received with appreciation\")"
    },
    "s": {
        "v": "mull",
        "l": "3.3"
    },
    "d": "mull, mylla; odlat markområde",
    "p": "jo:r_d",
    "a": "http://lexin.nada.kth.se/sound/jord.mp3"
},
```

**Field explanations:**
- `t`: translation
- `c`: class (part of speech)
- `i`: inflection
- `e`: example
- `id`: idiom
- `s`: synonym
- `d`: definition
- `p`: phonetic transcription
- `a`: audio URL
- `v`: value
- `l`: level

By default, the dictionary is saved as JSON without indentation to minimize file size. You can manually set `indent=4` in the `json.dump()` method to generate a human-friendly JSON output.

## Thanks

Thanks to the excellent work of [The People's Dictionary](https://folkets-lexikon.csc.kth.se/folkets/folkets.en.html), all dictionaries released by this repository are republished works based on The People's Dictionary.


## License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/2.5/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/2.5/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/2.5/">Creative Commons Attribution-ShareAlike 2.5 Generic License</a>.
