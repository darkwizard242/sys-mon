$env:ChocolateyInstall="$env:ProgramData\chocoportable"
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))



#$InstallDir="$choco_dir"
#$env:ChocolateyInstall="$InstallDir"
#Set-ExecutionPolicy Bypass -Scope CurrentUser
#iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
#Set-ExecutionPolicy Bypass -Force -Scope CurrentUser

## Downloading Chocolatey, installing and upgrading it
#iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex
choco upgrade chocolatey

## Download and Install Python3
choco install -y python3
refreshenv
python -V

## Upgrade pip
python -m pip install --upgrade pip