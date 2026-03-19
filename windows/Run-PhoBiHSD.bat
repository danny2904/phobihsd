@echo off
setlocal

set IMAGE=ghcr.io/danny2904/phobihsd:cpu-latest
set CONTAINER=phobihsd
set PORT=7860

echo [1/4] Pulling image %IMAGE% ...
docker pull %IMAGE%
if errorlevel 1 goto :error

echo [2/4] Stopping old container if exists ...
docker rm -f %CONTAINER% >nul 2>nul

echo [3/4] Starting PhoBiHSD container ...
docker run -d --name %CONTAINER% -p %PORT%:7860 %IMAGE%
if errorlevel 1 goto :error

echo [4/4] Opening app in browser ...
start http://localhost:%PORT%

echo.
echo PhoBiHSD is starting at http://localhost:%PORT%
echo If this is first run, model download may take a few minutes.
exit /b 0

:error
echo.
echo Failed to run container. Ensure Docker Desktop is running.
exit /b 1
