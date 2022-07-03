#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Renamer.py

Description:
Rename multi objects/takes in motionbuilder

Support:
Email: hudidinini@gmail.com

Update:
6/20/2022
refactor by internal UI package

6/22/2022
refactor code

6/29/2022
remove namespace funciton

7/2/2022
update to python3 for motionbuilder2022/2023
'''

from pyfbsdk import *
from pyfbsdk_additions import *

class main():

    def __init__(self):
        # rename rule params
        baseName = ""
        prefix = ""
        removeFirstIndex = 0
        suffix = ""
        removeLastIndex = 0
        baseNumber = 0
        step = 0
        searchForStr = ""
        replaceWithStr = ""

        # ui component params
        self.chkBaseName = None
        self.edtBaseName = None
        self.chkPrefix = None
        self.edtPrefix = None
        self.chkRemoveFirst = None
        self.spnRemoveFirst = None
        self.chkSuffix = None
        self.edtSuffix = None
        self.chkRemoveLast = None
        self.spnRemoveLast = None
        self.chkNumbered = None
        self.edtNumbered = None
        self.spnBaseNumber = None
        self.spnStep = None
        self.chkSearchReplace = None
        self.edtSearchFor = None
        self.edtReplaceWith = None
        self.btnRename = None

    def setupUI(self, mainLayout):
        # Create Main region frame:
        x = FBAddRegionParam(5,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(5,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(-5,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(-5,FBAttachType.kFBAttachBottom,"")
        lytMain = FBVBoxLayout()
        mainLayout.AddRegion("lytMain","lytMain", x, y, w, h)
        mainLayout.SetControl("lytMain",lytMain)

        lytNameSpace = FBHBoxLayout()
        lytBaseName = FBHBoxLayout()
        lytPrefix = FBHBoxLayout()
        lytRemoveFirst = FBHBoxLayout()
        lytSuffix = FBHBoxLayout()
        lytRemoveLast = FBHBoxLayout()
        lytNumbered = FBHBoxLayout()
        lytNumberedBaseNumber = FBHBoxLayout()
        lytNumberedStep = FBHBoxLayout()
        lytSearchReplace = FBHBoxLayout()
        lytSearchFor = FBHBoxLayout()
        lytReplaceWith = FBHBoxLayout()
        lytRename = FBHBoxLayout()

        # *** basename layout ***
        #check box button
        self.chkBaseName = FBButton()
        self.chkBaseName.Caption = "Base Name:"
        self.chkBaseName.Style = FBButtonStyle.kFBCheckbox
        self.chkBaseName.Justify = FBTextJustify.kFBTextJustifyLeft

        # edit line
        self.edtBaseName = FBEdit()

        lytBaseName.AddRelative(self.chkBaseName,0.4)
        lytBaseName.AddRelative(self.edtBaseName,0.6)
        #----------------------------------------


        # *** prefix layout ***
        #check box button
        self.chkPrefix = FBButton()
        self.chkPrefix.Caption = "Prefix:"
        self.chkPrefix.Style = FBButtonStyle.kFBCheckbox
        self.chkPrefix.Justify = FBTextJustify.kFBTextJustifyLeft

        # edit line
        self.edtPrefix = FBEdit()

        lytPrefix.AddRelative(self.chkPrefix,0.4)
        lytPrefix.AddRelative(self.edtPrefix,0.6)
        #----------------------------------------


        # *** remove first layout ***
        #check box button
        self.chkRemoveFirst = FBButton()
        self.chkRemoveFirst.Caption = "Remove First:"
        self.chkRemoveFirst.Style = FBButtonStyle.kFBCheckbox
        self.chkRemoveFirst.Justify = FBTextJustify.kFBTextJustifyLeft

        # edit line
        self.spnRemoveFirst = FBEditNumber()

        lytRemoveFirst.AddRelative(self.chkRemoveFirst,0.4)
        lytRemoveFirst.AddRelative(self.spnRemoveFirst,0.6)
        #----------------------------------------


        # *** suffix layout ***
        #check box button
        self.chkSuffix = FBButton()
        self.chkSuffix.Caption = "Suffix:"
        self.chkSuffix.Style = FBButtonStyle.kFBCheckbox
        self.chkSuffix.Justify = FBTextJustify.kFBTextJustifyLeft

        # edit line
        self.edtSuffix = FBEdit()

        lytSuffix.AddRelative(self.chkSuffix,0.4)
        lytSuffix.AddRelative(self.edtSuffix,0.6)
        #----------------------------------------


        # *** remove last layout ***
        #check box button
        self.chkRemoveLast = FBButton()
        self.chkRemoveLast.Caption = "Remove Last:"
        self.chkRemoveLast.Style = FBButtonStyle.kFBCheckbox
        self.chkRemoveLast.Justify = FBTextJustify.kFBTextJustifyLeft

        # edit line
        self.spnRemoveLast = FBEditNumber()

        lytRemoveLast.AddRelative(self.chkRemoveLast,0.4)
        lytRemoveLast.AddRelative(self.spnRemoveLast,0.6)
        #----------------------------------------


        # *** numbered layout ***
        #check box button
        self.chkNumbered = FBButton()
        self.chkNumbered.Caption = "Numbered"
        self.chkNumbered.Style = FBButtonStyle.kFBCheckbox
        self.chkNumbered.Justify = FBTextJustify.kFBTextJustifyLeft

        lytNumbered.AddRelative(self.chkNumbered,1)
        #----------------------------------------


        # *** numbered base number layout ***
        # create label
        self.lblBaseNumber = FBLabel()
        self.lblBaseNumber.Caption = "Base Number:"

        # create EditNumber/spinner
        self.spnBaseNumber = FBEditNumber()

        lytNumberedBaseNumber.AddRelative(self.lblBaseNumber,0.4)
        lytNumberedBaseNumber.AddRelative(self.spnBaseNumber,0.6)
        #----------------------------------------

        # *** numbered base number layout ***
        # create label
        self.lblStep = FBLabel()
        self.lblStep.Caption = "Step:"

        # create EditNumber/spinner
        self.spnStep = FBEditNumber()

        lytNumberedStep.AddRelative(self.lblStep,0.4)
        lytNumberedStep.AddRelative(self.spnStep,0.6)
        #----------------------------------------


        # *** search replace layout ***
        # create check box
        self.chkSearchReplace = FBButton()
        self.chkSearchReplace.Caption = "Search Replace"
        self.chkSearchReplace.Style = FBButtonStyle.kFBCheckbox
        self.chkSearchReplace.Justify = FBTextJustify.kFBTextJustifyLeft

        lytSearchReplace.AddRelative(self.chkSearchReplace,1)
        #----------------------------------------


        # *** search for layout***
        # create label
        self.lblSearchFor = FBLabel()
        self.lblSearchFor.Caption = "Search For:"

        self.edtSearchFor = FBEdit()

        lytSearchFor.AddRelative(self.lblSearchFor,0.4)
        lytSearchFor.AddRelative(self.edtSearchFor,0.6)
        #----------------------------------------


        # *** Replace with layout***
        # create label
        self.lblReplaceWith = FBLabel()
        self.lblReplaceWith.Caption = "Replace With:"

        self.edtReplaceWith = FBEdit()

        lytReplaceWith.AddRelative(self.lblReplaceWith,0.4)
        lytReplaceWith.AddRelative(self.edtReplaceWith,0.6)
        #----------------------------------------


        # *** Rename layout***
        # create label
        self.btnRename = FBButton()
        self.btnRename.Caption = "Rename!"
        self.btnRename.OnClick.Add(self.renameCallback)

        lytRename.AddRelative(self.btnRename,1)
        #----------------------------------------

        lytMain.AddRelative(lytBaseName,1.0)
        lytMain.AddRelative(lytPrefix,1.0)
        lytMain.AddRelative(lytRemoveFirst,1.0)
        lytMain.AddRelative(lytSuffix,1.0)
        lytMain.AddRelative(lytRemoveLast,1.0)
        lytMain.AddRelative(lytNumbered,1.0)
        lytMain.AddRelative(lytNumberedBaseNumber,1.0)
        lytMain.AddRelative(lytNumberedStep,1.0)
        lytMain.AddRelative(lytSearchReplace,1.0)
        lytMain.AddRelative(lytSearchFor,1.0)
        lytMain.AddRelative(lytReplaceWith,1.0)
        lytMain.AddRelative(lytRename,1.0)

    def getSelectedTake(self):
        selectedTakeList = []
        for take in FBSystem().Scene.Takes:
            if take.Selected:
                selectedTakeList.append(take)

        return selectedTakeList
    
    # http://awforsythe.com/tutorials/pyfbsdk-4
    def getSelectedModel(self):

        #selectedModelList = []
        selectedModels = FBModelList()

        topModel = None # Search all models, not just a particular branch
        selectionState = True # Return models that are selected, not deselected
        sortBySelectOrder = True # The last model in the list was selected most recently
        FBGetSelectedModels(selectedModels, topModel, selectionState, sortBySelectOrder)

        return selectedModels

    def getRenameRule(self):
        # init
        baseName = ""
        prefix = ""
        removeFirstIndex = 0
        suffix = ""
        removeLastIndex = 0
        baseNumber = 0
        step = 0
        searchForStr = ""
        replaceWithStr = ""

        # check if get base name input
        if self.chkBaseName.State:
            if self.edtBaseName.Text != "":
                baseName = self.edtBaseName.Text
            else:
                pass
        else:
            pass

        # check if get prefix input
        if self.chkPrefix.State:
            if self.edtPrefix.Text != "":
                prefix = self.edtPrefix.Text
            else:
                pass
        else:
            pass

        # check if remove first string
        if self.chkRemoveFirst.State:
            removeFirstIndex = self.spnRemoveFirst.Value
        else:
            pass

        # check if remove last string
        if self.chkRemoveLast.State:
            removeLastIndex = self.spnRemoveLast.Value
        else:
            pass

        # check if get suffix input
        if self.chkSuffix.State:
            if self.edtSuffix.Text != "":
                suffix = self.edtSuffix.Text
            else:
                pass
        else:
            pass

        # check if numbered
        if self.chkNumbered.State:
            baseNumber = self.spnBaseNumber.Value
            step = self.spnStep.Value
        else:
            pass

        # check if search replace
        if self.chkSearchReplace.State:
            if self.edtSearchFor.Text != "":
                searchForStr = self.edtSearchFor.Text
            else:
                pass

            if self.edtReplaceWith.Text != "":
                replaceWithStr = self.edtReplaceWith.Text
            else:
                pass
        else:
            pass

        return baseName, prefix, int(removeFirstIndex), suffix, int(removeLastIndex), \
                int(baseNumber), int(step), searchForStr, replaceWithStr
    
    def renameCallback(self, control, event):
        baseName, prefix, removeFirstIndex, suffix, removeLastIndex, baseNumber, step, searchForStr, replaceWithStr=self.getRenameRule()
        print ("----------[Rename Rule]----------")
        print ("Base name:%s" % baseName)
        print ("Prefix:%s" % prefix)
        print ("Remove First:%s" % str(removeFirstIndex))
        print ("Suffix:%s" % suffix)
        print ("Remove LastIndex:%s" % str(removeLastIndex))
        print ("Base Number:%s" % str(baseNumber))
        print ("Step:%s" % str(step))
        print ("Search For:%s" % searchForStr)
        print ("Replace With:%s" % replaceWithStr)
        #print "--------------------------------------------------"


        # ------------------------------------------------------------------
        # step number
        curNum = 0
        stepNum = 0
        # undoMangager = fb.FBUndoManager()
        # undoMangager.TransactionBegin("Rename Process")
        selectedTakeList = self.getSelectedTake()
        selectedModelList = self.getSelectedModel()
        if selectedTakeList:
            print ("----------[Rename Log]----------")
            for take in selectedTakeList:
                takeOrgName = take.Name
                tempName = ""

                if baseName == "":
                    tempName = take.Name
                else:
                    tempName = baseName

                # remove first index character
                if removeFirstIndex:
                    tempNameIndex = len(tempName)
                    if removeFirstIndex >= tempNameIndex:
                        FBMessageBox ("Remove First Error", "The take being renamed doesn't have enough characters in"\
                                    " its name to remove the requested number\nRename cancelled", "OK")
                    else:
                        tempName = tempName[removeFirstIndex:tempNameIndex]

                # remove last character
                if removeLastIndex:
                    tempNameIndex = len(tempName)
                    if removeLastIndex >= tempNameIndex:
                        FBMessageBox ("Remove Last Error", "The take being renamed doesn't have enough characters in"\
                                    " its name to remove the requested number\nRename cancelled", "OK")
                    else:
                        tempName = tempName[0:tempNameIndex-removeLastIndex]
                else:
                    pass

                # add prefix
                if prefix != "":
                    tempName = prefix + tempName
                else:
                    pass

                # add suffix
                if suffix != "":
                    tempName = tempName + suffix
                else:
                    pass

                # Numbered
                if baseNumber == step == 0:
                    pass
                else:
                    if curNum == 0:
                        tempName = tempName + str(baseNumber)
                        curNum = 1
                    elif curNum == 1:
                        stepNum = stepNum + step
                        tempName = tempName + str(baseNumber+stepNum)
                    else:
                        pass

                # search replace
                if searchForStr == "" or replaceWithStr == "":
                    pass
                else:
                    if tempName.find(searchForStr) != -1:
                        tempName = tempName.replace(searchForStr, replaceWithStr)

                take.Name = tempName
                print ("%s >> %s" % (takeOrgName,tempName))

            #undoMangager.TransactionEnd()
        
        elif selectedModelList:
            print ("----------[Rename Log]----------")
            for model in selectedModelList:
                modelOrgName = model.Name
                tempName = ""

                if baseName == "":
                    tempName = model.Name
                else:
                    tempName = baseName

                # remove first index character
                if removeFirstIndex:
                    tempNameIndex = len(tempName)
                    if removeFirstIndex >= tempNameIndex:
                        FBMessageBox ("Remove First Error", "The take being renamed doesn't have enough characters in"\
                                    " its name to remove the requested number\nRename cancelled", "OK")
                    else:
                        tempName = tempName[removeFirstIndex:tempNameIndex]

                # remove last character
                if removeLastIndex:
                    tempNameIndex = len(tempName)
                    if removeLastIndex >= tempNameIndex:
                        FBMessageBox ("Remove Last Error", "The take being renamed doesn't have enough characters in"\
                                    " its name to remove the requested number\nRename cancelled", "OK")
                    else:
                        tempName = tempName[0:tempNameIndex-removeLastIndex]
                else:
                    pass

                # add prefix
                if prefix != "":
                    tempName = prefix + tempName
                else:
                    pass

                # add suffix
                if suffix != "":
                    tempName = tempName + suffix
                else:
                    pass

                # Numbered
                if baseNumber == step == 0:
                    pass
                else:
                    if curNum == 0:
                        tempName = tempName + str(baseNumber)
                        curNum = 1
                    elif curNum == 1:
                        stepNum = stepNum + step
                        tempName = tempName + str(baseNumber+stepNum)
                    else:
                        pass

                # search replace
                if searchForStr == "" or replaceWithStr == "":
                    pass
                else:
                    if tempName.find(searchForStr) != -1:
                        tempName = tempName.replace(searchForStr, replaceWithStr)

                model.Name = tempName
                print ("%s >> %s" % (modelOrgName,tempName))


        else:
            FBMessageBox ("Attention!", "Please select at least one model or take to using this tool~\n\nRename cancelled\n ","OK")
            print("Please select at least one model or take to using this tool~")


    def CreateTool(self):    
        # Tool creation will serve as the hub for all other controls
        t = FBCreateUniqueTool("Renamer")
        self.setupUI(t)

        t.StartSizeX = 280
        t.StartSizeY = 400
        ShowTool(t)
    


renamerTool = main()
renamerTool.CreateTool()
#Ending