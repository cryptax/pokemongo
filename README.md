# Pokemon Go Plus Pattern Decoder

## LED and Vibration control

Versions 0.29.x of Pokemon Go application show "patterns" for the future Pokemon Go Plus hardware device. Those patterns are commands for the BLE LED and Vibration characteristic.

The pseudo-code shows patterns such as:

```java
public static byte[] getCaptureSucceed()
    {
        v0 = new byte[76];
        v0 = {0, 0, 0, 24, 3, 8, 240, 3, 240, 240, 2, 0, 255, 1, 0, 143, 3, 8, 240, 3, 240, 240, 2, 0, 255, 1, 0, 143, 3, 8, 240, 3, 240, 240, 2, 0, 255, 1, 0, 143, 3, 8, 240, 3, 240, 240, 2, 0, 255, 1, 0, 143, 3, 8, 240, 3, 240, 240, 2, 0, 255, 1, 0, 143, 3, 8, 240, 3, 240, 240, 2, 0, 255, 1, 0};
        return v0;
    }
```

The script pokemon-pattern.py _decodes_ this pattern in something which makes sense in terms of RGB LEDs and vibration. 

Please note that Pokemon Go Plus is still under development and that those patterns, the way they should be handled or even more generally the design of the device may be changed. 

This work is intended for research only. Please use responsibly.

## How to use the script

Get the patterns from the pseudo-code, and then provide them to the script, e.g:

```bash

$ python pokemon-pattern.py -d "0, 0, 0, 13, 1, 15, 112, 1, 0, 0, 1, 15, 112, 1, 0, 0, 1, 15, 112, 1, 0, 0, 1, 15, 112, 1, 0, 0, 1, 15, 112, 1, 0, 0, 1, 15, 112, 1, 0, 0, 1, 15, 112"
=== Pokemon Go Plus LED and Vibration characteristic pattern decoder ===
--- Header ---
Input Read Time       : 0 ms
Priority              : 0 
Nb of 3-byte patterns : 13
 1 Flash Time:  50 ms, Interpolate: False, Vibration: 7, RGB: (0xf, 0x0, 0x0)
 2 Flash Time:  50 ms, Interpolate: False, Vibration: 0, RGB: (0x0, 0x0, 0x0)
 3 Flash Time:  50 ms, Interpolate: False, Vibration: 7, RGB: (0xf, 0x0, 0x0)
 4 Flash Time:  50 ms, Interpolate: False, Vibration: 0, RGB: (0x0, 0x0, 0x0)
 5 Flash Time:  50 ms, Interpolate: False, Vibration: 7, RGB: (0xf, 0x0, 0x0)
 6 Flash Time:  50 ms, Interpolate: False, Vibration: 0, RGB: (0x0, 0x0, 0x0)
 7 Flash Time:  50 ms, Interpolate: False, Vibration: 7, RGB: (0xf, 0x0, 0x0)
 8 Flash Time:  50 ms, Interpolate: False, Vibration: 0, RGB: (0x0, 0x0, 0x0)
 9 Flash Time:  50 ms, Interpolate: False, Vibration: 7, RGB: (0xf, 0x0, 0x0)
10 Flash Time:  50 ms, Interpolate: False, Vibration: 0, RGB: (0x0, 0x0, 0x0)
11 Flash Time:  50 ms, Interpolate: False, Vibration: 7, RGB: (0xf, 0x0, 0x0)
12 Flash Time:  50 ms, Interpolate: False, Vibration: 0, RGB: (0x0, 0x0, 0x0)
13 Flash Time:  50 ms, Interpolate: False, Vibration: 7, RGB: (0xf, 0x0, 0x0)
```
