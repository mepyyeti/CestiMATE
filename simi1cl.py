#!usr/bin/env python3

import os

class House():
	_propcounter = 0
	def __init__(self, street_name, price, income, units, age, sqft,lot):
		self.street_name = street_name
		self.price = float(price)
		self.original_price = self.price
		self.income = float(income)
		if self.income == 0:
			self.income = 1
		self.units = int(units)
		self.age = int(age)
		self.sqft = float(sqft)
		if self.units > 1:
			self.avgsqft = self.sqft / self.units
		self.lot = float(lot)
		House._propcounter += 1
	def alter(self,alterations,alterations_cost=0):
		self.alterations = alterations
		self.alterations_cost = alterations_cost
		self.price += self.alterations_cost
		print('***Please be cognizant you have chosen to add a remodeling charge of: '+str('{:,}'.format(self.alterations_cost)) +' to property price.')
		print('>>>Your new price is amended to: $'+str('{:,}'.format(self.price)))
		return self.alterations,self.alterations_cost, self.price
	def questionable_time(self):
		if (self.price/self.income) >12:
			print('**this property does not generate sufficient cash flows**')
			self.questionable = 'will not break even.'
			self.calib = self.income * 8
			print('** $'+str(self.calib)+' is more realistic.**') 
		else:
			self.questionable = 'timely.'
			self.calib = self.price
		return self.questionable, self.calib
	def info(self):
		if self.calib:
			print('Currently:')
		if self.units > 1:
			self.unitpl = 'units'
		else:
			self.unitpl = 'unit'
		if 9999>=self.lot>=100:
			self.lot /= 10000
		if 100>self.lot >=10:
			self.lot /= 100
		if 10 > self.lot>=1:
			self.lot /= 10 
		self.avgsqft = self.sqft / self.units
		self.sqft_income = float(self.income / self.sqft)
		print('sqft: {:,}'.format(self.sqft))
		print('''\tThis house is ${:,}.\n\tHouse generates ${:,} in annual income.\n\tIt has {} {} and {:,} sqft {}.\n\tIts floor plan is {:,} sqft. \n\tIts lot size is {:,} acres.\n\tIt generates ${:,} /sqft yrly.
'''.format(self.price,self.income,self.units,self.unitpl,self.avgsqft,self.unitpl,self.sqft,self.lot,self.sqft_income))
		return self.avgsqft,self.lot,self.sqft_income
	def generic_info(self,vrate=0.05):
		self.vrate = vrate
		self.monthly_income = self.income/self.units/12
		self.vmi = (1-self.vrate) * self.monthly_income
		if (0<=self.age<=35):
			self.upkeep = float(0.05 * self.monthly_income)
			self.vupkeep = float(0.05 * self.vmi)
		elif (35<self.age<=60):
			self.upkeep = float(0.1 * self.monthly_income)
			self.vupkeep = float(0.1 * self.vmi)
		else:
			self.upkeep = float(0.2 * self.monthly_income)
			self.vupkeep = float(0.2 * self.vmi)
		self.pretax_income = self.monthly_income - self.upkeep
		self.vpretax_income = self.vmi - self.vupkeep
		if self.lot >=10:
			self.lot /= 100
		if 10 > self.lot>=1:
			self.lot /= 10 
		return self.sqft, self.lot, self.monthly_income, self.upkeep, self.pretax_income, self.vmi, self.vupkeep, self.vpretax_income
	def print_generic_info(self):
		print('Your monthly income is...${:,}. Monthly upkeep is ${:,}.\nMonthly pretax is ${:,}.'.format(self.monthly_income,self.upkeep,self.pretax_income))
		if self.vrate != 0:
			print('VACANCY VERSION \nYour monthly income is ${:,}. Monthly upkeep is ${:,}.\nMonthly pretax is ${:,}.'.format(self.vmi,self.vupkeep, self.vpretax_income))
	def utility(self,electric,gas,heat,water):
		self.electric = int(electric)
		self.gas = int(gas)
		self.heat = int(heat)
		self.water = int(water)
		self.totalu = self.electric + self.gas + self.heat + self.water
		self.totaluu = int(self.totalu/self.units)
		print('total cost of utilities is ${:,}.\nWith {} {}, this is ${:,}/unit.'.format(self.totalu, self.units,self.unitpl, self.totaluu))
		return self.totalu, self.totaluu
	def tenant_utilities(self,telectric,tgas,theat,twater):
		self.telectric = telectric
		self.tgas = tgas
		self.theat = theat
		self.twater = twater
		return self.telectric, self.gas, self.theat, self.twater
	def town(self,town,school,taxes):
		self.town = str(town)
		self.school = int(school)
		self.taxes = float(taxes)
		self.rep = self.school + (0.0001*self.taxes)
		return self.rep, self.town
	def sqft_score(self):
		if self.sqft <= 1200:
			self.rep -= 0.4
		elif self.sqft > 2000:
			self.rep += 0.4
		return self.rep
	def lot_score(self):
		if self.lot > 0.3:
			self.rep += 1
		if 0.3 >= self.lot >0.275:
			self.rep +=0.75
		if 0.275 >= self.lot <0.250:
			self.rep +=0.50
		if 0.250>=self.lot > 0.225:
			self.rep += 0.25
		if self.lot < 0.2:
			self.lot -= 1
		return self.rep
	def ins(self,flood, hoins=0):
		self.flood = flood
		self.hoins = int(hoins)
		return self.flood, self.hoins,
	def physical(self,roof,basement=None,garage=None,insulation=None):
		self.roof = roof
		self.basement = basement
		self.garage = garage
		self.insulation = insulation
		return self.roof, self.basement, self.garage,self.insulation
	def score(self):
		if self.telectric == 'n' or self.telectric == 'no':
			self.rep -=0.5
		if self.tgas == 'no' or self.tgas == 'n':
			self.rep -= 0.5
		if self.theat == 'no' or self.theat == 'n':
			self.rep -= 0.7
		if self.twater == 'no' or self.twater =='n':
			self.rep -= 0.5
		if (self.price / self.income) <=9:
			self.rep += 2
		if 9 < (self.price/self.income) <=12:
			self.rep += 0
		if (self.price/self.income) >12:
			self.rep -=1
			print('**this property does not generate sufficient cash flows**')
		if self.hoins <= 1400:
			self.rep += 1
		if self.flood == 'no' or self.flood =='n':
			self.rep += 2
		if self.basement == 'yes' or self.basement == 'y':
			self.rep += 1
		if 0 <= self.roof <=5:
			self.rep += 0.8
		if 5<self.roof <10:
			self.rep += 0.5
		if self.roof>= 15:
			self.rep -= 0.5
		if self.garage == 'yes' or self.garage == 'y':
			self.rep += 1.3
		if self.insulation =='yes' or self.insulation=='y':
			self.rep +=1.0
		if self.insulation =='partial' or self.insulation =='part' or self.insulation =='p':
			self.rep +=0.5
		print(self.rep)
		return self.rep
	def mortg_calc(self,down,prate):
		self.prate=float(prate)
		if self.prate >= 1.00:
			self.prate /= 100 
			self.prate /= 12
		self.payment= float((self.price - down)*((self.prate*(1+self.prate)**360) / ((1+self.prate)**360 -1)))
		if self.payment:
			filen ='mlstest0.txt'
			with open(filen,'a+') as f:
				f.write(str(House._popcounter) + ' '+ self.town.upper() + " " +self.street_name)
				f.write('\n######MORTGAGE CALC: ')
				f.write('monthly payment is: ' +str(self.payment))
				f.write('\n\t---this includes tax, h.o.i., and flood')
		self.ins = (self.taxes + self.hoins)/12
		print('self.prate' +str(self.prate) +'self.down'+str(down)+'self.py'+str(self.payment))
		if self.flood:
			self.ins += 200
			self.payment += self.ins 
		return self.prate, self.ins, self.payment
	def writeintofile(self):
		filen ='mlstest0.txt'
		with open(filen,'a+') as f:
			f.write('\n\n\n')
			f.write(str(House._propcounter) + ' '+ self.town.upper() + " ")
			f.write(self.street_name + '\n---final score: ')
			f.write(str(self.rep)+ self.questionable.upper())
			if (self.price/self.income) >12:
				f.write('\n\t\t>>REASONABLE: $' +str(self.calib))
			f.write('\n---price: $' +str('{:,}'.format(self.price)))
			if self.price != self.original_price:
				f.write('\n\t>>you have added a remodeling charge of: $'+str('{:,}'.format(self.alterations_cost)) +'to property price.')
			f.write('\n---income: $'+str('{:,}'.format(self.income)))
			f.write('\n---floor: '+str(self.sqft)+ ' --monthly sqft income: $' +str(self.sqft_income))
			f.write('\n---lot size: '+str('{:,}'.format(self.lot)) +' acres')
			f.write(' ---'+str('{:,}'.format(self.sqft))  +' sqft floor plan')
			f.write('\n---pretax income: '+str('{:,}'.format(self.pretax_income)))
			f.write('\n---pretax w/ vacancy: '+ str('{:,}'.format(self.vpretax_income)))
			f.write('\n---home age: '+ str(self.age))
			f.write('\n---insulation: '+ str(self.insulation.upper()))
			f.write('------\n\n')
		print('all done...you may open file...\nlocated in: '+os.getcwd()) 

if __name__=='__main__':
	print('ok...running module as main file...')
else:
	print(__name__,' not run as main file.')
