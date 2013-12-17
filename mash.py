# Justin A
# @itsFL4GSH1P

# Script is based on degrees F. If you want to use degrees C change the constant .2 to .41

def single_infusion():
	ratio = float(raw_input("Please enter the qt/lb ration you will be using (ie. 1.25): ")) #accepts your water to grain ratio

	target_temp = int(raw_input("Please enter the temperature you're trying to achieve: ")) #accepts your target mash temp

	grain_temp = int(raw_input("Please enter the current temperature of your grain: ")) #accepts your grains temperature currently

	infusion_temp = (.2/ratio)*(target_temp - grain_temp) + target_temp #formula based on "How to Brew" See readme for more details
	print "Your initial addition of water will need to be",round(infusion_temp, 2),"*F"

def multi_infusion():
	temps = [] #defines a list 'temps' to store all the temperature goals
	print "Please enter the", infusions, "temperatures you are trying to achieve."
	initial_temp = int(raw_input("Please enter the initial temperature target: ")) #accepts your target mash temp

	for x in range(infusions-1): #will loop the same number of times as temperatures entered
		targets = int(raw_input("Please enter the next temperature target: ")) #creates a new variable 'targets' that stores the values entered into a list
		temps.append(targets) #adds user entered temps from above to the list 'temps'

	ratio = float(raw_input("Please enter the qt/lb ration you will be starting with (ie. 1.25): ")) #accepts your water to grain ratio

	grain_temp = int(raw_input("Please enter the current temperature of your grain: ")) #accepts your grains temperature currently

	infusion_temp = (.2/ratio)*(initial_temp - grain_temp) + initial_temp #formula based on "How to Brew" See readme for more details

	grain_wgt = float(raw_input("Please enter the total weight of your grain bill (in lbs): "))

	amts = []
	initial_water = (ratio*grain_wgt)
	amts.append(initial_water)
	
	print "Your initial addition of water will need to be",round(infusion_temp, 2),"*F to bring the mash temp to:",initial_temp,"*F"
	
	boiling_amt = (temps[0]-initial_temp)*(.2*grain_wgt+initial_water)/(210-temps[0])
	amts.append(boiling_amt)

	print "The amount of your first boiling water addition will be ", round(boiling_amt, 2), "qts to bring the mash temp to:", temps[0],"*F"

	nums = len(temps) #stores the amount of numbers in the list 'temps'
	#print nums 
	
	count = 0
	while count < nums-1: #subtracting 1 from 'nums' to compensate for list arrays starting at 0
		count = count + 1 #looping through each value in the list starting at the 2nd item
		print count
		next_amt = (temps[count]-temps[count-1])*(.2*grain_wgt+(amts[count-1]+amts[count]))/(210-temps[count])	
		amts.append(next_amt) 
		print "The amount of your next boiling water addition will be",round(amts[count+1], 2), "qts to bring the mash temp to:", temps[count],"*F"

	print amts
	print temps
	print temps[0]
	print temps[1]



print "============================================================================"
print "| Please note this script is based on the assumption we are working in *F. |"
print "|      If you wish to work in *C please feel free to modify to code.       |"
print "============================================================================"	

infusions = int(raw_input("Please enter the number of infusions you're planning: "))

if infusions == 1:
	single_infusion()
elif infusions >= 2:
	multi_infusion()



