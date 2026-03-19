@echo off
setlocal

set IMAGE=ghcr.io/danny2904/phobihsd:gpu-latest
set CONTAINER=phobihsd-gpu
set PORT=7860

echo [1/4] Pulling image %IMAGE% ...
docker pull %IMAGE%
if errorlevel 1 goto :error

echo [2/4] Stopping old container if exists ...
docker rm -f %CONTAINER% >nul 2>nul

echo [3/4] Starting PhoBiHSD GPU container ...
docker run -d --gpus all --name %CONTAINER% -p %PORT%:7860 %IMAGE%
if errorlevel 1 goto :error

echo [4/4] Opening app in browser ...
start http://localhost:%PORT%

echo.
echo PhoBiHSD GPU is starting at http://localhost:%PORT%
exit /b 0

:error
echo.
echo Failed to run GPU container. Ensure Docker Desktop + NVIDIA runtime are ready.
exit /b 1
