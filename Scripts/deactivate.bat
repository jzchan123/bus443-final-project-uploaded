@echo off

set VIRTUAL_ENV=

REM Don't use () to avoid problems with them in %PATH%
if not defined _OLD_VIRTUAL_PROMPT goto ENDIFVPROMPT
    set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
    set _OLD_VIRTUAL_PROMPT=
:ENDIFVPROMPT

if not defined _OLD_VIRTUAL_PYTHONHOME goto ENDIFVHOME
    set "PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%"
    set _OLD_VIRTUAL_PYTHONHOME=
:ENDIFVHOME

if not defined _OLD_VIRTUAL_PATH goto ENDIFVPATH
    set "PATH=%_OLD_VIRTUAL_PATH%"
    set _OLD_VIRTUAL_PATH=
:ENDIFVPATH

if defined _OLD_VIRTUAL_PYTHONPATH (
    set "PYTHONPATH=%_OLD_VIRTUAL_PYTHONPATH%"
)