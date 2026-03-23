![Flow](flow.png)
# 🚦 Pico Traffic Light

## Project Description

A minimalistic MicroPython application for the Raspberry Pi Pico that simulates a standard three-stage traffic light sequence using GPIO pins and a modular timing function.

This project utilizes the RP2040 microcontroller to control three LEDs (Red, Yellow, and Green). The logic is implemented in MicroPython using a simple `flash_led` function to manage GPIO states and timing delays.

The traffic light sequence follows a continuous loop:
- Green: 30 seconds  
- Yellow: 5 seconds  
- Red: 30 seconds  

Designed for simplicity, this project serves as a foundational example of GPIO control and timing in embedded systems.

---

## License

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
