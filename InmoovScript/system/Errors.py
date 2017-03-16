# -- coding: utf-8 --
# ##############################################################################
# ERRORS FILE
# ##############################################################################



def errorSpokenFunc(errorType,param="0"):
	global RobotIsErrorMode
	
	subconsciousMouth.speakBlocking(unicode(lang_alert,'utf-8'))
	RobotIsErrorMode=1
	
	if errorType=="BadLanguagePack":
		RobotIsErrorMode=0
		errorSpokenAlert=lang_BadLanguagePack
	
	if errorType=="ArduinoNotConnected":
		errorSpokenAlert=lang_ArduinoNotConnected+param

	if errorType=="BadMrlcommVersion":
		errorSpokenAlert=lang_BadMrlcommVersion+param
		
	if errorType=="VoiceDownloaded":
		errorSpokenAlert=lang_VoiceDownloaded
	
	if errorType=="MyvoiceType":
		errorSpokenAlert=lang_MyvoiceType

	if errorType=="MyLanguage":
		errorSpokenAlert=lang_MyLanguage
		
	if errorType=="MrlNeedUpdate":
		errorSpokenAlert=lang_MrlNeedUpdate
		
	if errorType=="BAdrduinoChoosen":
		errorSpokenAlert=lang_BAdrduinoChoosen+param
		
	if errorType=="ConfigParserProblem":
		errorSpokenAlert=lang_ConfigParserProblem+param
		
	if errorType=="I_cannot_download_this_mary_T_T_S_voice":
		errorSpokenAlert=lang_I_cannot_download_this_mary_T_T_S_voice
	
	if errorType=="ChatbotError":
		errorSpokenAlert=lang_ChatbotError	
		
	if errorType=="OpenCvNoWorky":
		errorSpokenAlert=lang_OpenCvNoWorky+param
		
	if errorType=="NeopixelNoWorky":
		errorSpokenAlert=lang_NeopixelNoWorky
		
	if errorType=="lang_newMRL":
		errorSpokenAlert=lang_newMRL
		
		
		
		
	
		
	print errorSpokenAlert
	subconsciousMouth.speakBlocking(unicode(errorSpokenAlert,'utf-8'))
	
	
		
