#!/usr/bin/env python3

# Copyright (c) 2019, Richard Hughes All rights reserved.
# Released under the BSD license. Please see LICENSE.md for more information.

import os
import argparse
import paho.mqtt.client as paho

# Define command line arguments
parms=argparse.ArgumentParser()
parms.add_argument("-b", "--broker", type=str, required=False, help="Broker", default=os.environ.get('DNSMSG_MQTT_HOST'))
parms.add_argument("-P", "--port", type=int, required=False, help="Pass", default=os.environ.get('DNSMSG_MQTT_PORT'))
parms.add_argument("-u", "--user", type=str, required=False, help="User", default=os.environ.get('DNSMSG_MQTT_USER'))
parms.add_argument("-p", "--pass", type=str, required=False, help="Pass", default=os.environ.get('DNSMSG_MQTT_PASS'))
parms.add_argument("-t", "--topic", type=str, required=False, help="Pass", default=os.environ.get('DNSMSG_MQTT_PUBQ'))
parms.add_argument("-c", "--client", type=str, required=True, help="Identity")
parms.add_argument("-m", "--message", type=str, required=True, help="Message")
args = vars(parms.parse_args())

# Main processing
def main(args):
  client = paho.Client(args['client'], transport='websockets')
  client.username_pw_set(username=args['user'], password=args['pass'])
  client.tls_set()
  client.connect(args['broker'], args['port'])
  client.publish(args['topic'], args['message'])
  client.disconnect() 

if __name__ == '__main__':
  # Execute main method 
  main(args)
