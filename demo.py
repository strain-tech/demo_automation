import argparse
import os
import netmiko

def init_args():
  args = get_args()
  return args

def get_args():
  parser = argparse.ArgumentParser(description="Demo Automation Project")
  parser.add_argument("device", help="Device Hostname or IP")
  args = parser.parse_args()
  return args

def main():
  print("Hello World")
  args = init_args()
  print("args", args)
  if 'JENKINS_HOME' in os.environ:
    print('Inside Jenkins')

if __name__ == '__main__':
  main()
