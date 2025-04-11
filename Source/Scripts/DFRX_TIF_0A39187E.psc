;BEGIN FRAGMENT CODE - Do not edit anything between this and the end comment
;NEXT FRAGMENT INDEX 3
Scriptname DFRX_TIF_0A39187E Extends TopicInfo Hidden

;BEGIN FRAGMENT Fragment_2
Function Fragment_2(ObjectReference akSpeakerRef)
Actor akSpeaker = akSpeakerRef as Actor
;BEGIN CODE
(GetOwningQuest() as _DFGoldConQScript).Recalc()
;END CODE
EndFunction
;END FRAGMENT

;END FRAGMENT CODE - Do not edit anything between this and the begin comment
