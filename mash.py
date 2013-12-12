# Justin A
# @itsFL4GSH1P

# Script is based on degrees F. If you want to use degrees C change the constant .2 to .41

def single_infusion():
	ratio = float(raw_input("Please enter the qt/lb ration you will be using (ie. 1.25): ")) #accepts your water to grain ratio

	target_temp = int(raw_input("Please enter the temperature(s)  you're trying to acheive: ")) #accepts your target mash temp

	grain_temp = int(raw_input("Please enter the current temperature of your grain: ")) #accepts your grains temperature currently

	infusion_temp = (.2/ratio)*(target_temp - grain_temp) + target_temp #formula based on "How to Brew" See readme for more details
	print "Your initial addition of water will need to be",round(infusion_temp, 2),"*F"

#def multi_infusion():


print "Please note this script is based on the assumption we are working in *F."
print "     If you wish to work in *C please feel free to modify to code.      "
print "========================================================================"	

infusions = int(raw_input("Please enter the number of infusions you're planning: "))

if infusions == 1:
	single_infusion()
elif infusions >= 2:
	multi_infusion()



