"""
Get the geographic location of the IPs visited to get to a particular URL
(given by a traceroute command)
From https://blogs.oracle.com/ksplice/entry/learning_by_doing_writing_your

This should be executed as 'root'
"""

import logging as log
import socket
import sys
import requests
import json

log.basicConfig(level=log.INFO)


class Url():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "URL Object: {}".format(self.name)

    def traceroute(self):
        """
        Python version of the 'traceroute' Unix command
        """
        log.info("Tracing route to {}".format(self.name))

        # Translate the given domain name into the IPv4 address
        dest_addr = IpAddress(socket.gethostbyname(self.name))
        # Create 2 sockets for sending (udp) and receiving (icmp) packets
        icmp = socket.getprotobyname('icmp')
        udp = socket.getprotobyname('udp')
        ttl = 1
        port = 33434
        max_hops = 30

        while True:
            recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
            send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
            send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
            recv_socket.bind(('', port))
            send_socket.sendto(''.encode(), (self.name, port))
            curr_addr = None

            try:
                # Return the data and the IP address of the connected router
                _, curr_addr = recv_socket.recvfrom(512)
                curr_addr = IpAddress(curr_addr[0])
                try:
                    # Mapping IP to a domain name
                    curr_name = socket.gethostbyaddr(curr_addr.num)[0]
                except socket.error:
                    curr_name = curr_addr.num

            # Some domain will hide their address, which will raise an error
            except socket.error:
                pass

            finally:
                send_socket.close()
                recv_socket.close()

            # Like in 'traceroute', returning IP and domain name, if available
            if curr_addr is not None:
                curr_host = '{0} ({1})'.format(curr_name, curr_addr.num)
            else:
                curr_host = '*'
            log.info('{0}\t{1}'.format(ttl, curr_host))
            curr_addr.localize()

            ttl += 1
            if curr_addr.num == dest_addr.num or ttl > max_hops:
                break


class IpAddress():
    def __init__(self, num):
        self.num = num

    def localize(self):
        url = 'http://ipinfo.io/' + self.num + '/json'
        r = requests.get(url)
        log.info(r.json())

if __name__ == '__main__':
    u = Url(sys.argv[1])

    u.traceroute()
