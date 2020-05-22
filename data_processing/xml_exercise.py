import random
import string
from xml.etree.ElementTree import parse, dump


def get_random_100_long_string():
    return ''.join(random.choice(string.ascii_letters) for i in range(100))


def find_element(root, element):
    return root.find(".//{0}".format(element))


def find_element_value(root, element_name):
    element = find_element(root, element_name)
    return element.text


def set_element(root, element_name, new_value):
    element = find_element(root, element_name)
    element.text = new_value


# Load data.xml file into memory.

xml_file_path = "resources/data.xml"
xml_object = parse("resources/data.xml")

# Extract & print to console: (sportsBookReference, transactionId, outcomeId, totalStake)

xml_root = xml_object.getroot()
for element_name in ["sportsBookReference", "transactionId", "outcomeId", "totalStake"]:
    element_value = find_element_value(xml_root, element_name)
    print("{:>20}: {:<12}".format(element_name, element_value))

# Modify:
#   BetDescription to random 100 characters.

set_element(xml_root, "betDescription", get_random_100_long_string())

#   totalStake to 10

set_element(xml_root, "totalStake", "10")

#   transactionId to 1

set_element(xml_root, "transactionId", "1")

# Print modified payload.

print("\n#### Modified payload: ####\n")
dump(xml_root)
