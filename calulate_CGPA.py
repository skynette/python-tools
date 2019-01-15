import argparse
import time

# i wanna turn this into a gp calculator
'''
CGPA calculator for 5 year course
Calculates cumulative CGPA after 5 years
'''

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("year_1_cgpa", help="year_1_cgpa", type=float)
parser.add_argument("year_2_cgpa", help="year_2_cgpa", type=float)
parser.add_argument("year_3_cgpa", help="year_3_cgpa", type=float)
parser.add_argument("year_4_cgpa", help="year_4_cgpa", type=float)
parser.add_argument("year_5_cgpa", help="year_5_cgpa", type=float)
parser.add_argument("-o", "--output", help="output to a file", action="store_true")

args = parser.parse_args()
R1 = args.year_1_cgpa
R2 = args.year_2_cgpa
R3 = args.year_3_cgpa
R4 = args.year_4_cgpa
R5 = args.year_5_cgpa

final_CGPA = (0.1*R1)+(0.15*R2)+(0.2*R3)+(0.25*R4)+(0.3*R5)

if args.output:

    f = open("cgpa_log.txt", "a")
    f.write(time.ctime() + " Calculated Entry: " + str(final_CGPA) + "\n")
    
if args.verbose:
	print("year_1_cgpa: " + str(args.year_1_cgpa))
	print("year_2_cgpa: " + str(args.year_2_cgpa))
	print("year_3_cgpa: " + str(args.year_2_cgpa))
	print("year_4_cgpa: " + str(args.year_2_cgpa))
	print("year_5_cgpa: " + str(args.year_2_cgpa))
	print ("Accumulative CGPA is " + str(final_CGPA))

elif args.quiet:
    print (final_CGPA)
else:
    print ("Final CGPA is " + str(final_CGPA))










