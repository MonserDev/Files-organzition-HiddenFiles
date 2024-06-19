@echo off 

> "%temp%\run_vbs.vbs" <nul (
      set /p "'=WScript.CreateObject("WScript.Shell").AppActivate WScript.CreateObject("WScript.Shell").CurrentDirectory : "
      set /p "'=WScript.Sleep 3000: WScript.CreateObject("WScript.Shell").SendKeys "{F5}""
    )  & cd /d "%temp%\." && %__AppDir__%cscript.exe //nologo "%temp%\run_vbs.vbs"

2>nul del/q /f "%temp%\run_vbs.vbs"