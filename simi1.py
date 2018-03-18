#!usr/bin/env python3
#simi0op.py

import sys
from simi1cl import House
i = 0
while True:
	run = str(input('please confirm...enter \'go\':'))
	if run != 'go':
	#	print('thx for using CestiMATE.  C ya round...')
		sys.exit()
	while True:
		i += 1
		print(i)
		try:
			street_name=str(input('enter a street name for house.'))
			town=str(input('enter town'))
			alterations=str(input('do you expect remodeling [yes/no]?'))
			space = street_name.find(' ')
			code, lbl = street_name.split(' ')
		except ValueError:
			print('please enter letters only.')
			continue
		break
	if alterations =='yes' or alterations == 'y':
		code.alter(alterations, alterations_cost)
		try:
			alterations_cost= float(input('how much do you anticpate spending on remodeling: $'))
		except ValueError:
			print('please enter a dollar amount')
			continue
	while True:
		try:
			price=int(input('price of house...'))
			income = int(input('annual income generated...'))
			units = int(input('how many units on property? '))
			age = int(input('age of dwelling? '))
			sqft=int(input('what is the floor plan square footage?'))
			lot=int(input('lot size: '))
		except ValueError:
			print('please enter whole numbers only...')
			continue
		break

	code = House(code, price,income,units,age,sqft,lot)
	
	code.questionable_time()
	code.info()
	print('20%[-#--------]80% to go')

	while True:
		generic = input('{:^s}'.format('wish to view generic financial earnings\' info? [yes/no]'))
		if generic =='':
			continue
		code.generic_info()
		if generic == 'n' or generic == 'no':
			print('ok, no problem')
			break
		else:
			code.print_generic_info()
			break
	print('moving on')
	print('30%[--#------]70% to go')

	while True:
		try:
			electric=int(input('power is...'))
			gas = int(input('gas is...'))
			if gas =='':
				gas = (electric/2)
				electric = gas
			heat = int(input('heat is...'))
			water = int(input('water is...'))
			break
		except ValueError:
			print('please round up...')
			continue
	print('thank you...')
	code.utility(electric,gas,heat,water)
	print('40%[---#------]60% to go')

	while True:
		print('{:^30}'.format('please answer [yes/no]\nBLANK = \'NO\''))
		try:
			telectric=str(input('Does tenant pay electric?...'))
			if telectric == '':
				telectric = 'no'
			tgas = str(input('Does tenant pay gas?...'))
			if tgas == '':
				tgas = 'no'
			theat = str(input('Does tenant pay heat?...'))
			if theat == '':
				theat = 'no'
			twater = str(input('Does tenant pay water?...'))
			if twater == '':
				twater = 'no'
			break
		except ValueError:
			print('must be a string...')
			continue

	print('thank you...')
	code.tenant_utilities(telectric, tgas, theat, twater)
	print('50%[----#-----]50% to go')

	while True:
		try:
			print('''SCHOOL SYSTEM
			use a scale of 1 -5:
			1 = worst (cambden/paterson)
			3 = middle (dumont)
			5 = best (alpine/norwood)
			''')
			school = int(input('enter your town\'s reputation score...basically are its schools great?'))
			break
		except ValueError:
			print('must be a number.')
			continue

	while True:
		try:
			taxes=int(input('annual taxes...'))
			break
		except ValueError:
			print('must be annual amount')
			continue
	code.town(town,school,taxes)
	print('60%[-----#----]40% to go')

	while True:
		try:
			hoins=int(input('annual h.o ins premium...'))
			break
		except ValueError:
			print('must be annual amount')
			continue
	print('70%[------#---]30% to go')
	print('gettin\' there')

	while True:
		try:
			flood = str(input('''enter [yes/no]
			Is flood insurance required? '''))
			break
		except ValueError:
			print('must be [yes/no]')
			continue
	code.ins(flood,hoins)
	print('80%[-------#--]20% to go')

	while True:
		try:
			roof=int(input('please enter age of roof in years.'))
			break
			if roof == '':
				roof = 15
		except ValueError:
			print('please enter whole numbers only')
			continue
	print('90%[--------#-]10% to go')

	while True:
		try:
			print('please answer [yes/no]...')
			basement=str(input('basement?...'))
			garage = str(input('garage?...'))
			insulation=str(input('insulation?options-->[yes,partial,no]...'))
			break
		except ValueError:
			print('please answer yes/no...')
			continue
	code.physical(roof,basement,garage,insulation)
	print('100%[---------#]Done.')

	#print('{:^30s}'.format(mort_question))
	while True:
		try:
			mort_question = input('Do you wish to find your 30 year mortgage quote?')
		except ValueError:
			print('please answer [yes/no]')
			continue
		if mort_question =='no' or mort_question== 'n':
			break
		try:
			amount_down = float(input('Enter amount you are putting down...'))
			if amount_down ==25 or amount_down == '':
				amount_down = float(price /4)
			if amount_down ==20:
				amount_down =float(price /5)
			if amount_down == 5:
				amount_down = float(price/20)
			prate = float(input('Enter APR'))
		except ValueError:
			print('please enter numbers...')
			continue
		print('price: ',price,'  amount down: ',amount_down)
		code.mortg_calc(amount_down, prate)
		break

	code.sqft_score()
	code.lot_score()
	code.score()
	write_file=str(input('confirm you want to save into a file..'))
	if write_file == 'yes' or  write_file == 'y':
		code.writeintofile()
	run = str(input('do you wish to look at another property now?'))
	if run == 'no' or run == 'n':
		print('i: ',i,'House class: ',code._propcounter)
		print('t\'was a pleasure interacting with yoou...\nCestiMATE looks forward to seeing you back!')
		sys.exit()

