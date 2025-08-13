Write-Host "Starting API server..."
$server = Start-Process -NoNewWindow -PassThru python -ArgumentList "-m uvicorn src.server.main:app --port 8000"

Start-Sleep -Seconds 2  # wait for server to start

try {
    Write-Host "Running pytest..."
    $env:RUN_UI="1"
    pytest --alluredir=allure-results

    Write-Host "Running Behave..."
    behave -f allure_behave.formatter:AllureFormatter -o allure-results
}
finally {
    if ($server -and $server.Id) {
        Write-Host "Stopping API server..."
        Stop-Process -Id $server.Id -Force
    }
}

Write-Host "Generating Allure report..."
allure serve allure-results
