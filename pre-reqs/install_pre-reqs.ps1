Set-ExecutionPolicy Bypass -Force -Scope CurrentUser

## Downloading Chocolatey, installing and upgrading it
$script = New-Object Net.WebClient
$script.DownloadString("https://chocolatey.org/install.ps1")
iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex
choco upgrade chocolatey

## Download and Install Python3
choco install -y python3
refreshenv
python -V

## Upgrade pip
python -m pip install --upgrade pip