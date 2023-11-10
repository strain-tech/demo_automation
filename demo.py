import os
import netmiko

print("Hello World")
if 'JENKINS_URL' in os.environ:
  print('Inside Jenkins')
