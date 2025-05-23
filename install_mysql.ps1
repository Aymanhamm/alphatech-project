Write-Host "Downloading MySQL Installer..."
$installerUrl = "https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-web-community-8.0.34.0.msi"
$installerPath = Join-Path $PSScriptRoot "mysql-installer.msi"

# Download MySQL Installer
Invoke-WebRequest -Uri $installerUrl -OutFile $installerPath

Write-Host "MySQL Installer downloaded successfully. Please run the installer manually."
Write-Host "Steps to follow:"
Write-Host "1. Double-click the downloaded mysql-installer.msi file"
Write-Host "2. Select 'Custom' installation"
Write-Host "3. Select these components:"
Write-Host "   - MySQL Server"
Write-Host "   - MySQL Workbench"
Write-Host "4. Follow the installation wizard"
Write-Host "5. When prompted, set a root password (remember this password)"
Write-Host "6. Complete the installation"

Write-Host "After installation, please run MySQL Workbench to create the database and user."
