"""Script to help you conveniently create SAP notes"""
"""creation by Michael Karek an Anne Kirchhof"""
"""An idea by Lorenzo de Luca"""
print("Hit enter if you do not know the answer.")
print("If you dont have an answer, type k.a.")
print("Generated files are located in C:\sophos-tmp\<case number>")

from datetime import datetime
case_number = input("Case number: ")
issue_description_cx = input("Enter customer description: ")
issue_description_tse = input("Enter your description: ")
error = input("Error message: ")
customer_name = input("Customer name: ")
customer_phone = input("Customer phone number: ")
customer_language = input("Customer language: ")
new_configuration = input("Is it a new configuration? (yes/no): ")
product_cat = input("Enter the product category. (UTM, XG, Sophos Central etc): ")
product_formatted = product_cat.lower()
product_typ = input("Enter the product type. ( e.g. XG310, SG85W etc): ")
product_formatted_type = product_typ.lower()
product_sn = input("Product serial number(s). (In HA case all first the active appliance): ")
firmware_version = input("Firmware version (Format: x.x.x): ")
ha = input("Is the device part of an HA cluster? (yes/no): ")
ha_mode = input("Which mode? (AA or AP): ")
ha_count = input("Number of HA devices: ")
access_id_fw = input("Access ID firewall = ")
access_id_expired = input("Access ID firewall expired Timestamp = ")
access_id_uid = input("Access UID central or second firewall = ")
access_id_expired2 = input("Access UID central or second firewall creation or expire Timestamp = ")
sophos_case_ftp_username = input("Sophos case FTP username = ")
sophos_case_ftp_password = input("Sophos case FTP password = ")
frequency_of_the_issue = input("Is this a one time issue? If not, how often does the problem occur? ")
repro_possible = input ("Can the issue be reproduced (yes/no)? ")
timestamp = input("Repro timestamp: ")
source_details = input("Source details (IP, username etc) ")

import os

path = 'C:\sophos-tmp'
joined_path = os.path.join(path,case_number)

# Check whether the specified path exists or not
isExist = os.path.exists(joined_path)

if not isExist:
  # Create a new directory because it does not exist 
  os.makedirs(joined_path)
  print("Created directory "+joined_path)

"""external_file = open("C:/sophos-tmp/"+case_number"SAP-"+case_number+"-"+datetime.today().strftime('%Y-%m-%d')+".txt", "w")"""
external_file = open(joined_path+"\SAP-"+case_number+"-"+datetime.today().strftime('%Y-%m-%d')+".txt", "w")
print("***** SAP Case " + case_number + " from " + datetime.today().strftime('%Y-%m-%d') + " *****\n", file = external_file)
print("Customer description:\n" + issue_description_cx, file = external_file)
print("TSE description:\n" + issue_description_tse, file = external_file)
print("Error message:\n" + error, file = external_file)
print("\n", file = external_file)

print("***** DATA: ***** \n", file = external_file)
print("Customer name: " + customer_name, file = external_file)
print("Customer phone number: " + customer_phone, file = external_file)
print("Customer language: " + customer_language, file = external_file)
print("New configuration = " + new_configuration, file = external_file) 
print("Product = " + product_formatted, file = external_file)
print("Product Type = " + product_formatted_type, file = external_file)
print("Product serial number(s) = " + product_sn, file = external_file)
print("Firmware version = " + firmware_version, file = external_file)
print("High availability = " + ha, file = external_file)
print("High availability mode = " + ha_mode, file = external_file)
print("How many devices in HA Cluster? = " + ha_count, file = external_file)
print("Remote access ID firewall = " + access_id_fw, file = external_file)
print("Remote access ID firewall expired = " + access_id_expired, file = external_file)
print("Access UID central or second firewall = " + access_id_uid, file = external_file)
print("Access UID central or second firewall creation or expire Timestamp = " + access_id_expired2, file = external_file)
print("Sophos FTP server credentials = " + sophos_case_ftp_username + ":" + sophos_case_ftp_password, file = external_file)
print("\n", file = external_file)

print("***** Issue Details: ***** ", file = external_file)
print("\n", file = external_file)
print("Issue Frequency = " + frequency_of_the_issue, file = external_file)
print("Repro possible = " + repro_possible, file = external_file)
print("Repro details:", file = external_file)
print("> Timestamp = " + timestamp, file = external_file)
print("> Source details = " + source_details, file = external_file)
print("\n", file = external_file)

print("***** ASSESSMENT: ***** ", file = external_file)
print("\n", file = external_file)
print("***** TROUBLESHOOTING STEPS: ***** ", file = external_file)
print("\n", file = external_file)
print("***** ACTION PLAN: ***** ", file = external_file)
print("\n", file = external_file)
print("***** LOG ANALYSIS: ***** ", file = external_file)
print("\n", file = external_file)
print("***** LOGS: ***** ", file = external_file)
print("\n", file = external_file)
print("***** FOLLOWED KB: ***** ", file = external_file)
print("\n", file = external_file)
print("***** COMMANDS USED FOR LOG COLLECTION: ***** ", file = external_file) 
print("\n", file = external_file)