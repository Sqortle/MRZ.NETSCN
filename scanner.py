import scapy.all as scapy
import optparse


def entry():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP")

    (user_options, args) = parser.parse_args()

    if not(user_options.target):
        print("Please enter a valid IP")

    return user_options.target


def scanner(ip_address):
    request_package = scapy.ARP(pdst=ip_address)
    stream_package = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    package = stream_package / request_package # bu ikisini birleşitiryor package altında
    (main_package, failed_package) = scapy.srp(package, timeout=1)  # timeout bekleme süresini bbelirler bir yerdne maks 1 saniye  cevap bekle der
    main_package.summary()


ip = entry()
scanner(ip)
