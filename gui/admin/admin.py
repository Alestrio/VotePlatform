#
# Copyright (c) 2020 by Alexis LEBEL, BOUDRY Hugo and PEDROSA Théo. All Rights Reserved.
# This is the model. There, we will do all the computations needed by the controller,
# and send back data to the software in itself.
#
import admincontroller
import adminview
import sys
sys.path.insert(0, "../../ioactions") #We need to use sys because those are in
import csvactions as csva             #another folder
import settings as sett

class Admin:

    def __init__(self):
        st = sett.Settings('settings.yaml') #if we want to move the voters
        csvpath = st.getCsvPath()                 #file to another folder
        self.csv = csva.CsvActions(csvpath)

        self.view = adminview.Adminview(self)
        self.view.createAndShowWindow()
        return None

    def addVoter(self, forename:str, lastname:str, passwordhash:str):
        self.csv.addLine(forename, lastname, passwordhash, -1, -1) #vote to -1 to
        self.view.setVotersListContent(self.getVoters()) #assert that no
        return None                                 #vote has been done


    def delVoter(self, id:int):
        self.csv.delById(id)
        return None

    def getVoters(self) -> list:
        lines = self.csv.getAllLines()
        print(lines)
        return lines

#We'll add methods to edit voters maybe later. Now, we focus on creating a
#simple but robust app. Furthermore, ideally, we can move the definition of
#the settings file to a global variable somewhere in the code.
