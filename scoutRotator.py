import pyrebase
import DataModel
import SPR
import firebaseCommunicator
import time
import traceback
import CrashReporter

PBC = firebaseCommunicator.PyrebaseCommunicator()
PBC.initializeFirebase()
fb = PBC.firebase

#testScouts = "calvin ethan nathan wentao janet carter kenny ryan nate astha astha gemma livy ben".split()
scouts = "aidan alex calvin carter evan gemma jack janet jesse jon justin jishnu katie kyle mingyo mx rachel sage sam sophia wesley westley zoe".split()
SPR = SPR.ScoutPrecision()
oldMatchNum = 0

#Creates list of availability values in firebase for each scout
def resetAvailability():
	availability = {name: 1 for name in scouts} 
	fb.child('availability').set(availability)

#Creates firebase objects for 18 scouts
def resetScouts():
	scouts = {'scout' + str(num) : {'currentUser': '', 'scoutStatus': ''} for num in range(1,19)}
	fb.child('scouts').set(scouts)

def doSPRsAndAssignments(newMatchNumber):
	while True:
		try:
			availabilityUpdated = fb.child("availabilityUpdated").get().val()
		except:
			availabilityUpdated = 0
		if availabilityUpdated: break
		time.sleep(2)
	try:
		fb.child("availabilityUpdated").set(0)
		if newMatchNumber.get('data') == None: return
		print('Setting scouts for match ' + str(fb.child('currentMatchNum').get().val()))
		#Gets scouting data from firebase
		newMatchNumber = str(fb.child('currentMatchNum').get().val())
		scoutDict = fb.child("scouts").get().val()
		#Gets the teams we need to scout for in the upcoming match
		blueTeams = fb.child("Matches").child(newMatchNumber).get().val()['blueAllianceTeamNumbers']
		redTeams = fb.child("Matches").child(newMatchNumber).get().val()['redAllianceTeamNumbers']
		#Finds and assigns available scouts
		available = [k for (k, v) in fb.child("availability").get().val().items() if v == 1]
		#Grades scouts and assigns them to robots
		SPR.calculateScoutPrecisionScores(fb.child("TempTeamInMatchDatas").get().val(), available)
		# SPR.sprZScores(PBC)
		newAssignments = SPR.assignScoutsToRobots(available, redTeams + blueTeams, fb.child("scouts").get().val())
		#and it is put on firebase
		fb.child("scouts").update(newAssignments)
	except Exception as e:
		CrashReporter.reportServerCrash(traceback.format_exc())

#Use this to reset scouts and availability before assigning tablets
#e.g. at the beginning of the day at a competition
def tabletHandoutStream():
	resetScouts()
	resetAvailability()
	fb.child("currentMatchNum").stream(doSPRsAndAssignments)

#Use this for running the server again (e.g. after a crash) to avoid reassigning scouts
def alreadyAssignedStream():
	global oldMatchNum
	oldMatchNum = fb.child("currentMatchNum").get().val()
	fb.child("currentMatchNum").stream(startAtNewMatch)

def startAtNewMatch(newMatchNum):
	if fb.child("currentMatchNum").get().val() > oldMatchNum:
		doSprsAndAssignments(newMatchNum)

#Use this if you are restarting the server and need to reassign scouts but scouts already have tablets
#Also useful for unexpected changes in availability
def simpleStream():
	fb.child("currentMatchNum").stream(doSPRsAndAssignments)

tabletHandoutStream()
