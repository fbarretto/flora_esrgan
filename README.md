# Flora ESRGAN Library
## Overview
This library is a [fork of BlueAmulet's fork](https://github.com/BlueAmulet/ESRGAN) of [ESRGAN by Xinntao](https://github.com/xinntao/ESRGAN). It includes various enhancements and features for image upscaling using ESRGAN models.

## Features

- In-memory splitting/merging functionality (fully seamless, no longer requires tile size)
- Seamless texture preservation (both tiled and mirrored)
- Model chaining
- Transparency preservation (3 different modes)
- 1-bit transparency support (with half transparency as well)
- Variations of the ESRGAN (RRDB) architecture, including ESRGAN, ESRGAN+, BSRGAN, RealSR, SPSR, Real-ESRGAN, and Real-ESRGANv2 (SRVGG)
- Any scale and most other internal model parameter settings
- On-the-fly interpolation

## Installation

To install the library, run the following commands:

```sh
pip install --upgrade pip
pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124
pip install git+https://github.com/fbarretto/flora_esrgan.git@master -U
```

## Usage

To use the library, import and initialize the `Upscale` class as shown in the snippet below:

```python
from flora_esrgan.upscale import Upscale

upscale = Upscale(
    model="4x-UltraSharp.pth",
    input=upscale_input.image,
)
output = upscale.run()
```

