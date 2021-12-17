from types import new_class
from typing import Counter, Dict, List, Tuple
import queue

width, height = 0, 0

def parse_packet(packet: str):
    """
    Parse a packet.
    """
    version_sum = int(''.join(packet[:3]), 2)
    version = version_sum
    packet = packet[3:]
    type = int(''.join(packet[:3]), 2)
    packet = packet[3:]
    if type == 4:
        reading = True
        number = ""
        while reading:
            reading = bool(int(packet.pop(0)))
            number += ''.join(packet[:4])
            packet = packet[4:]
        return version_sum, packet, int(number, 2)
    else:
        size = bool(int(packet.pop(0)))
        packets = []
        if size:
            size = int(''.join(packet[:11]), 2)
            packet = packet[11:]
            for i in range(size):
                version, packet, result = parse_packet(packet)
                packets.append(result)
                version_sum += version
        else:
            size = int(''.join(packet[:15]), 2)
            packet = packet[15:]
            actual_size = 0 
            while actual_size < size:
                old_packet = packet
                version, packet, result = parse_packet(packet)
                packets.append(result)
                version_sum += version
                actual_size += (len(old_packet) - len(packet))
        if type == 0:
            result = sum(packets)
        elif type == 1:
            result = 1
            for i in packets:
                result *= i
        elif type == 2:
            result = min(packets)
        elif type == 3:
            result = max(packets)
        elif type == 5:
            result = int(packets[0] > packets[1])
        elif type == 6:
            result = int(packets[0] < packets[1])
        else:
                result = int(packets[0] == packets[1])
        return version_sum, packet, result

def solution1(input: List[str]):
    """
    Solution to problem 1.
    """
    sum, rest, result = parse_packet(input)
    return sum

def solution2(input: List[str]):
    """
    Solution to problem 2.
    """
    sum, rest, result = parse_packet(input)
    return result
    

if __name__ == "__main__":
    with open('input.txt') as f:
        input: List[str] = list(''.join([''.join(list(bin(int(c, 16)))[2:]).zfill(4) for c in list(f.read())]))
    print(solution1(input))
    print(solution2(input))