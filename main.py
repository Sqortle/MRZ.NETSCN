import subprocess
import optparse


def enter():
    parse = optparse.OptionParser()
    parse.add_option("-i", "--interface", dest="interface", help="Interface değiştirme: ")
    parse.add_option("-m", "--mac", dest="mac_address", help="Yeni MAC Adresi: ")

    return parse.parse_args()


def mac_changing(interface_name, mac_addr):
    subprocess.call(["ifconfig", interface_name, "down"])
    subprocess.call(["ifconfig", interface_name, "hw", "ether", mac_addr])
    subprocess.call(["ifconfig", interface_name, "up"])


(user_input, args) = enter()
mac_changing(user_input.interface, user_input.mac_address)
