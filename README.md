# enviropi

In addition to installing from the requirements.txt:

pip install -r requirements.txt

You also need to enable SPI and I2C.

Finally you need to run:

sudo apt install libatlas-base-dev python3-pil libopenjp2-7-dev

to make sure you have the right C files for numpy and Pillow.
