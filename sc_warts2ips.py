#!/usr/bin/env python
#
# Program:      $Id: $ 
# Author:       Robert Beverly <rbeverly@nps.edu>, mod by Quirin Scheitle
# Description:  Print scamper output without source or destination IP
 
import sys
from sc_stats import WartsStats

if __name__ == "__main__":
  assert len(sys.argv) == 2

  w = WartsStats(sys.argv[1], verbose=False)
  while True:
    try:
      (flags, ips, rtts, meta) = w.next_trace()
      if flags == None: break
      for i, ip in enumerate(ips):
        if( ip != flags['srcaddr'] and ip != flags['dstaddr'] ):
	        print "%s\n" % (ip),
    except Exception, e:
      print "Flags:", flags
      print "** Error:", e
      sys.exit(-1)
