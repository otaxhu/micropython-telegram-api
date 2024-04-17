from machine import Pin
import network
import requests
import config
from time import sleep

# Global state
previous_time_msg = 0
button_pressed = False


def irq_handler(_pin: Pin):
    global button_pressed
    button_pressed = True


def main():
    global previous_time_msg
    global button_pressed
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to network...")
        wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
        while not wlan.isconnected():
            pass
        print("network config:", wlan.ifconfig())

    Pin(13, Pin.IN).irq(irq_handler, Pin.IRQ_FALLING)

    while 1:
        sleep(1)
        base_url = config.TELEGRAM_BASE_URL
        # Gets the latest message
        res = requests.get(
            base_url + '/getUpdates?offset=-1&allowed_updates=["message"]'
        )
        obj = res.json()
        res.close()

        if not obj["ok"] or not obj["result"]:
            continue

        chat_id = obj["result"][0]["message"]["chat"]["id"]
        message_timestamp = obj["result"][0]["message"]["date"]

        if previous_time_msg is 0:
            requests.get(
                base_url + f"/sendMessage?chat_id={chat_id}&text=ESP-32+reconnected!"
            ).close()

        previous_time_msg = message_timestamp

        if not button_pressed:
            continue

        button_pressed = False

        requests.get(
            base_url
            + f"/sendMessage?chat_id={chat_id}&text=You+have+someone+in+the+door+%F0%9F%8C%9F"
        ).close()


if __name__ is "__main__":
    main()
