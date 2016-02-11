
#switch class from http://code.activestate.com/recipes/410692/
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

#A program to calculate acrylamide gel ratios
print("This program calculates reagent volumes for SDS and Urea page gel solutions using reagents from National Diagnostics. ")

#Collecting gel info from user
#Later, potentially add function to calculate gel percent from kDa
gel_type = input('SDS or Urea PAGE?: ')
gel_percent = (input('Enter the gel percentage: '))
gel_volume = (input('Enter the solution volume (mL): '))
print(" ")

#Reformatting input data
gel_type = str(gel_type)
gel_type = gel_type.replace(" ", "")

for case in switch(gel_type.lower()):
	if case('sds'):
		sds_gel = {}
		sds_gel['ProtoGel'] = gel_volume * gel_percent / 30
		sds_gel['Resolving Bfr'] = gel_volume / 4
		sds_gel['Water'] = gel_volume - (sds_gel['ProtoGel'] + sds_gel['Resolving Bfr'])
		sds_gel['APS'] = (gel_volume / 100)
		sds_gel['TEMED (uL)'] = gel_volume
		for k, v in sds_gel.items():
			print(k + ':', round(v, 2))

	elif case('urea'):
                urea_gel = {}
                urea_gel['Concentrate'] = gel_volume * gel_percent / 25
                urea_gel['Buffer'] = gel_volume * 0.1
                urea_gel['Diluent'] = gel_volume - (urea_gel['Concentrate'] + urea_gel['Buffer'])
                urea_gel['APS'] = (gel_volume / 100) * 0.8
                urea_gel['TEMED (uL)'] = (gel_volume / 100) * 40
                for x, y in urea_gel.items():
                        print(x + ':', round(y, 2))
	else:
		print("Error, gel type not recognized.")

print(" ")

