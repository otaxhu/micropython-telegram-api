# Connecting to Telegram Bots API
In this repository I'm connecting to Telegram Bots API from a ESP-32 microcontroller using MicroPython / Python as programming language.

## Concept
What I wanted to do is like a proof of concept on how to do a "smart doorbell application", I don't have any server on my own so I'm gonna use Telegram API to make it.

## How to run it
- ### Prerequisites
  - `ampy` tool.

    Tool for flashing python scripts to the ESP-32

  - `esptool.py` tool.

    Tool for flashing the Python Interpreter to the ESP-32

- ### Steps
  If you wanna get this project up, you gonna have to clone it and create the file `config.py` where you gonna put all of the credentials specified in `config.py.example`.

  I'm using "ampy" tool to flash the python scripts `boot.py` and `config.py`, if you have all of the prerequisites then just run the bash script `flash_firmware` followed by `flash_mp`, here is a example on how to do it:

  ```bash
  $ ./flash_firmware

  $ ./flash_mp
  ```

  #### **Note:**
  You just need to run `flash_firmware` the first time, it is very heavy to execute that command and it's only needed when you wanna use MicroPython for the first time.

I hope you find it useful.
