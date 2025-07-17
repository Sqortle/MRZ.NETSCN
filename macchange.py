import subprocess
import optparse
import re


def enter():
    parse = optparse.OptionParser()
    parse.add_option("-i", "--interface", dest="interface", help="Interface değiştirme: ")
    parse.add_option("-m", "--mac", dest="mac_address", help="Yeni MAC Adresi: ")

    return parse.parse_args()


def mac_changing(interface_name, mac_addr):
    subprocess.call(["ifconfig", interface_name, "down"])
    subprocess.call(["ifconfig", interface_name, "hw", "ether", mac_addr])
    subprocess.call(["ifconfig", interface_name, "up"])


# noinspection PyTypeChecker
def get_old_mac_addr(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac_addr = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:", ifconfig)  # w herhangi bir karakter anlamına gelir herhangi iki karakter ardından : olanalrı filtreler
    if new_mac_addr:
        return new_mac_addr.group(0)
    else:
        return None


(user_input, args) = enter()
mac_changing(user_input.interface, user_input.mac_address)
old_mac_addr = get_old_mac_addr(user_input.interface)

if old_mac_addr == user_input.mac_address:
    print("Successful")
else:
    print("Failed")
