powershell.exe -command "&{Set-ExecutionPolicy Unrestricted -Scope LocalMachine}" > NULL
start powershell.exe -executionpolicy bypass -f "%~dp0ATS_start.ps1"