#set var
$setPort = '5000'
$setLocation = 'C:\scripts\RestAPI'
$Env:FLASK_ENV = 'production'
$Env:FLASK_APP = 'main.py'


function closePython()
{
	$pids = (Get-Process -Name python -ErrorAction SilentlyContinue).Id
	
	if( $pids -eq $null )
	{
		return $false
	}else
	{
		foreach ($pidaux in $pids)
		{
			Stop-Process -Id $pidaux	
		}
		return $true
	}
}


Write-Host -ForegroundColor Green "Iniciando servidor"

for($aux = 0; $aux -le 5; $aux++){ echo '.' ; sleep -s 1 }
$ips = [System.Net.Dns]::GetHostAddresses($hostname).IPAddressToString

$aux = closePython

if ($aux -eq $true){ Write-Host -ForegroundColor yellow "Processos Python limpos!!!" } else {Write-Host -ForegroundColor Green "Sem processos python rodando!!!!"}


Write-Host -ForegroundColor yellow "IPs BY hostaname was found"

foreach ($ip in $ips)
{
	if( $ip -like "10.55*"  )
	{ 
		Set-Location -Path $setLocation -PassThru
		start-Process -FilePath "flask.exe" -ArgumentList "run", "-h", $ip, "-p", $setPort
	}
	sleep -s 1
}
			



