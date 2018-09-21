$env:ChocolateyInstall="$env:ProgramData\chocoportable"
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

## Downloading Chocolatey, installing and upgrading it
choco upgrade chocolatey

## Download and Install Python3
$env:PythonInstall="$env:ProgramData\Python37"
choco install -y python3 --params '"/InstallDir:"$env:PythonInstall"'
#choco install -y python3 --install-directory "$env:PythonInstall"
refreshenv
python -V

## Upgrade pip
python -m pip install --upgrade pip