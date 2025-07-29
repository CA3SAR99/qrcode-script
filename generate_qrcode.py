import sys
import qrcode

def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_qrcode.py [ARGUMENT]")
        sys.exit(1)

    ARGUMENT = sys.argv[1]
    img = qrcode.make(ARGUMENT)
    img.save("qrcode.png")
    print("QR code saved as qrcode.png")

if __name__ == "__main__":
    main()
