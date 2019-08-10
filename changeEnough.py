def changeEnough(nums, x):
	y = []
	y.append(nums[0]*0.25)
	y.append(nums[1]*0.10)
	y.append(nums[2]*0.05)
	y.append(nums[3]*0.01)
	o = sum(y)
	print y
	print o
	if o/2 == x:
		return True
	else:
		return False

print(changeEnough([25,20,5,0], 4.35))



