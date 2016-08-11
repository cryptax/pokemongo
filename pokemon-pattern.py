#!/usr/bin/env python

"""
__author__ = "Axelle Apvrille"
__copyright__ = "Copyright 2016, Fortinet, Fortiguard Labs"
__license__ = "MIT License"

Meant for reseach only - based on v0.29.x versions (may change in the future!)
"""

import argparse

__version__ = '0.1'


def str_comma_to_list(s): return [int(x) for x in s[0].split(',')]

def get_arguments():
    parser = argparse.ArgumentParser(description='Pokemon Go Plus v0.29.x pattern decoder', prog='pokemon-pattern', epilog='Version '+__version__+' - Greetz from Axelle Apvrille')
    parser.add_argument('-d','--decode', help='decode this pattern. The pattern is expected to be a comma separated string. Quote the string. e.g python pokemon-pattern.py -d "0, 0, 0, 0"', nargs='+', action='store')
    parser.add_argument('-v', '--verbose', help='prints everything about arguments etc', action='store_true')
    args = parser.parse_args()
    return args


def parse_header(pattern, verbose=False):
    '''Parses a pattern header (normally 4 bytes)
    Input pattern is expected to be a list of decimal values e.g [1,0,0,13]'''
    assert len(pattern) >= 4, "Header is too small"
    if verbose:
        print "---> parse_header(): %s " % (pattern[0:3])
    input_read_time = pattern[0] * 50

    # byte 4: bit 7 is priority. bits 0-6 is number of following 3-byte patterns
    priority = (pattern[3] >> 5) & 0x07
    nb = pattern[3] & 0x1f

    print "--- Header ---"
    print "Input Read Time       : %d ms" % (input_read_time)
    print "Priority              : %d " % (priority)
    print "Nb of 3-byte patterns : %d" % (nb)

    if verbose:
        print "<--- parse_header(): nb=%d" % (nb)
    return nb

def parse_pattern(pattern, number=0, verbose=False):
    '''Input pattern is expected to be a list of 3 decimal values'''
    assert len(pattern) >= 3, "Pattern is truncated"
    if verbose:
        print "---> parse_pattern(): %s " % (pattern)
    flash_time_ms = pattern[0] * 50
    green = (pattern[1] >> 4) & 0x0f
    red = pattern[1] & 0x0f
    interpolate = (pattern[2] >> 7) & 0x01
    vibrate = (pattern[2] >> 4) & 0x07
    blue = pattern[2] & 0x0f
    
    print "%2d Flash Time: %3d ms, Interpolate: %5r, Vibration: %1d, RGB: (%s, %s, %s)" % (number, flash_time_ms, bool(interpolate), vibrate, hex(red), hex(green), hex(blue))
    #print "Flash Time: %d ms" % (flash_time_ms)
    #print "Interpolate: %r" % (bool(interpolate))
    #print "Vibration intensity: %d" % (vibrate)
    #print "R, G, B: (%s, %s, %s)" % (hex(red), hex(green), hex(blue))


def decode(pattern, verbose=False):
    '''Decodes the pattern array
    The input pattern is supposed to be something like 
    [ '0, 0, 0, 13, 1, 15, 112, 1...' ]
    '''
    if verbose:
        print "-> decode(): pattern=%s" % (pattern)

    pattern_list = str_comma_to_list(pattern)
    if verbose:
        print "   decode(): list=%s" % (pattern_list)

    # decode header
    nb = parse_header(pattern_list)
    if verbose:
        print "   decode(): nb=%d" % (nb)

    # check we have enough bytes
    if len(pattern_list) < ((3*nb)+4):
        print "ERROR: pattern is incomplete"

    # decode as much 3-byte patterns as we can
    current_index = 4
    pattern_no = 1
    while current_index + 3 <= len(pattern_list):
        #print "--- Pattern %d ---" % (pattern_no)
        parse_pattern(pattern_list[current_index:current_index+3], pattern_no, verbose)
        current_index = current_index + 3
        pattern_no = pattern_no + 1
    

if __name__ == "__main__":
    print "=== Pokemon Go Plus LED and Vibration characteristic pattern decoder ==="
    args = get_arguments()
    decode(args.decode, args.verbose)
    
