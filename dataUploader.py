#Last Updated: 11/11/17
import pyrebase
import random
import time
import DataModel

#Makes a lot of random data and sets data on firebase for testing

class CalculatedTeamInMatchData(object):
	'''docstring for CalculatedTeamInMatchData'''
	def __init__(self, **args):
		#initializer for random CalculatedTIMDs
		super(CalculatedTeamInMatchData, self).__init__()
		self.numRPs = random.randint(0, 4)
		self.liftoffAbility = random.randint(0, 50)
		self.numHighShotsTele = random.randint(0, 50)
		self.numHighShotsAuto = random.randint(0, 50)
		self.numLowShotsTele = random.randint(0, 50)
		self.numLowShotsAuto = random.randint(0, 50)
		self.numGearsPlacedTele = random.randint(0, 50)
		self.numGearsPlacedAuto = random.randint(0, 50)
		self.wasDisfunctional = bool(random.randint(0, 1))
		self.avgKeyShotTime = random.randint(0, 50)

class TeamInMatchData(object):
	'''An FRC TeamInMatchData Object'''
	def __init__(self, **args):
		#initializer for random TIMDs
		super(TeamInMatchData, self).__init__()
		self.calculatedData = None
		'''
		 self.teamNumber = args['teamNumber']
		 self.matchNumber = args['matchNumber']
		 self.scoutName = args['scoutName']
		 self.superNotes = random.randint(0, 1)
		 self.numHoppersOpenedTele = random.randint(0, 1)
		 self.numGearGroundIntakesTele = random.randint(0, 1)
		 self.numGearLoaderIntakesTele = random.randint(0, 1)
		 self.numGearsEjectedTele = random.randint(0, 1)
		 self.numGearsFumbledTele = random.randint(0, 1)
		 self.didReachBaselineAuto = random.randint(0, 1)
		 self.numHoppersOpenedAuto = random.randint(0, 1)
		 self.didLiftoff = bool(random.randint(0, 1))
		 self.didStartDisabled = bool(random.randint(0, 1))
		 self.didBecomeIncapacitated = bool(random.randint(0, 1))
		'''
		self.rankSpeed = random.randint(0, 4)
		self.rankAgility = random.randint(0, 4)
		self.rankGearControl = random.randint(0, 4)
		self.rankBallControl = random.randint(0, 4)
		self.rankDefense = random.randint(0, 4)
		'''
		 self.gearsPlacedByLiftAuto = {
		 	'lift1' : random.randint(0, 1),
		 	'lift2' : random.randint(0, 1),
		 	'lift3' : random.randint(0, 1)
		 }
		 self.gearsPlacedByLiftTele = {
		 	'lift1' : random.randint(0, 1),
		 	'lift2' : random.randint(0, 1),
		 	'lift3' : random.randint(0, 1)
		 }
		 self.highShotTimesForBoilerAuto = [
		 	{
		 		'time' : random.randint(0, 1),
		 		'numShots' : random.randint(0, 1),
		 		'position' : 'Hopper'
		 	}
		 ]
		 self.lowShotTimesForBoilerAuto = [
		 	{
		 		'time' : random.randint(0, 1),
		 		'numShots' : random.randint(0, 1),
		 		'position' : 'Hopper'
		 	}
		 ]
		 self.highShotTimesForBoilerTele = [
		 	{
		 		'time' : random.randint(0, 1),
		 		'numShots' : random.randint(0, 1),
		 		'position' : 'Key'
		 	}
		 ]
		 self.lowShotTimesForBoilerTele = [
		 	{
		 		'time' : random.randint(0, 1),
		 		'numShots' : random.randint(0, 1),
		 		'position' : 'Key'
		 	}
		 ]
		'''

class Match(object):
	'''An FRC Match Object'''
	def __init__(self, **args):
		#initializer for random matches
		super(Match, self).__init__()
		self.number = args['number']
		self.calculatedData = None
		self.redAllianceTeamNumbers = args['redAllianceTeamNumbers']
		self.blueAllianceTeamNumbers = args['blueAllianceTeamNumbers']
		self.numRotorsSpinningRedAuto = random.randint(0, 1)
		self.numRotorsSpinningRedTele = random.randint(0, 1)
		self.numRotorsSpinningBlueAuto = random.randint(0, 1)
		self.numRotorsSpinningBlueTele = random.randint(0, 1)
		self.blueDidStartAllRotors = random.randint(0, 1)
		self.redDidReachFortyKilopascals = random.randint(0, 1)
		self.blueDidReachFortyKilopascals = random.randint(0, 1)
		self.redScore = random.randint(0, 1)
		self.blueScore = random.randint(0, 1)
		self.foulPointsGainedRed = random.randint(0, 1)
		self.foulPointsGainedBlue = random.randint(0, 1)

class CalculatedMatchData(object):
	'''docstring for CalculatedMatchData'''
	def __init__(self, **args):
		#initializer for random match data
		super(CalculatedMatchData, self).__init__()
		self.predictedRedScore = random.randint(0, 50)
		self.predictedBlueScore = random.randint(0, 50)
		self.sdPredictedRedScore = random.randint(0, 50)
		self.sdPredictedBlueScore = random.randint(0, 50)
		self.redWinChance = random.random()
		self.blueWinChance = random.random()
		self.predictedBlueRPs = random.random() * 4
		self.actualBlueRPs = random.random() * 4
		self.predictedRedRPs = random.random() * 4
		self.actualRedRPs =  random.random() * 4
		self.fortyKilopascalChanceRed = random.random()
		self.fortyKilopascalChanceBlue = random.random()
		self.allRotorsTurningChanceRed = random.random()
		self.allRotorsTurningChanceBlue = random.random()
		self.__dict__.update(args)

config = {
	'apiKey': 'mykey',
	'authDomain': '1678-scouting-2016.firebaseapp.com',
	# 'authDomain': 'scouting-2017-5f51c.firebaseapp.com',
	'databaseURL': 'https://www.1678-scouting-2016.firebaseio.com/'
	# 'databaseURL': 'https://www.scouting-2017-5f51c.firebaseio.com/'
}
app = pyrebase.initialize_app(config)
pyre = app.database()
testScouts = 'a b c d e f g h i j k l m n o p q r'.split()
cm = 1
while(True):
	match = pyre.child('/Matches', cm).get().val()
	m = Match(number = cm, redAllianceTeamNumbers = match['redAllianceTeamNumbers'], blueAllianceTeamNumbers = match['blueAllianceTeamNumbers'])
	# pyrebase.set('/Matches/', str(cm), m.__dict__)
	for team in match['redAllianceTeamNumbers'] + match['blueAllianceTeamNumbers']:
		pyre.child('TeamInMatchDatas').child(str(team) + 'Q' + str(match['number'])).set(TeamInMatchData().__dict__)
		time.sleep(4)
	print('Done with match' + str(cm))
	cm += 1
	time.sleep(20)
