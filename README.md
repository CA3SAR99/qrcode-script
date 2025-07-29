# QRcode-Script

A simple Python command-line script to generate QR codes from text or URLs. This is useful for quickly converting strings into scannable QR codes.

# Requirements

You need to have the following Python packages installed:

- [`qrcode`](https://pypi.org/project/qrcode/)
- [`Pillow`](https://pypi.org/project/Pillow/) (used internally by `qrcode` to generate images)

Install both with:

```bash
pip install qrcode[pil]
 
