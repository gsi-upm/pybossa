#!/usr/bin/env python2

import sys

from pybossa import *


##FUNCIONA
if ((sys.argv[1] == 'jsongolden') and (len(sys.argv) > 3)):
	jsonfile = sys.argv[2]
	goldencsvpath = sys.argv[3]
	print(jsonfile)
	tweetsForPybossaJsonGolden(jsonfile, goldencsvpath)

##FUNCIONA
elif ((sys.argv[1] == 'jsonnogolden') and (len(sys.argv) > 2)):
	jsonfile = sys.argv[2]
	print(jsonfile)
	tweetsForPybossaJsonWithoutGolden(jsonfile)

##FUNCIONA
elif ((sys.argv[1] == 'csvgolden') and (len(sys.argv) > 3)):
	csvfile = sys.argv[2]
	print(csvfile)
	goldencsvpath = sys.argv[3]
	print(goldencsvpath)
	tweetsForPybossaCsvGolden(csvfile, goldencsvpath)

elif ((sys.argv[1] == 'csvnogolden') and (len(sys.argv) > 2)):
	csvfile = sys.argv[2]
	print(csvfile)
	tweetsForPybossaCsvNoGolden(csvfile)

##FUNCIONA
elif ((sys.argv[1] == 'reportwithgolden') and (len(sys.argv) > 6) ):
		filewithids = sys.argv[2]
		taskjsonpath = sys.argv[3]
		taskrunjsonpath = sys.argv[4]
		goldenpath = sys.argv[5]
		numberofcategories = int(sys.argv[6])
		pybossaReportWithGolden(filewithids, taskjsonpath, taskrunjsonpath, goldenpath, numberofcategories)

elif ((sys.argv[1] == 'reportwithoutgolden') and (len(sys.argv) > 5) ):
		filewithids = sys.argv[2]
		taskjsonpath = sys.argv[3]
		taskrunjsonpath = sys.argv[4]
		numberofcategories = int(sys.argv[5])
		pybossaReportWithoutGolden(filewithids, taskjsonpath, taskrunjsonpath, numberofcategories)



else:
	raise ValueError('The only valid parameters are json +jsonfile, csv + csvfile or report + idstrfile + number of categories')