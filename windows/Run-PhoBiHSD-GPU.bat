@echo off
setlocal EnableExtensions

set "LOG=%~dp0Run-PhoBiHSD-GPU.log"
echo [%date% %time%] Starting Run-PhoBiHSD-GPU.bat > "%LOG%"
call :main >> "%LOG%" 2>&1
set "EXITCODE=%errorlevel%"

echo.
echo ExitCode=%EXITCODE%
echo Log file: "%LOG%"
if not "%EXITCODE%"=="0" (
  echo.
  echo Failed. Open log file for full error details.
)
pause
exit /b %EXITCODE%

:main

set "IMAGE=ghcr.io/danny2904/phobihsd:gpu-latest"
set "CONTAINER=phobihsd-gpu"
set "PORT=7860"
set "DOCKER_BIN="

where docker >nul 2>&1
if "%errorlevel%"=="0" set "DOCKER_BIN=docker"
if not defined DOCKER_BIN (
  if exist "C:\Program Files\Docker\Docker\resources\bin\docker.exe" (
    set "DOCKER_BIN=C:\Program Files\Docker\Docker\resources\bin\docker.exe"
  )
)
if not defined DOCKER_BIN (
  echo Docker CLI not found. Install Docker Desktop first.
  exit /b 10
)

echo [check] Using docker command: %DOCKER_BIN%
%DOCKER_BIN% info >nul 2>&1
if not "%errorlevel%"=="0" (
  echo Docker daemon is not ready. Please start Docker Desktop and wait until status is Running.
  exit /b 11
)

echo [prep] Resetting GHCR auth cache to use anonymous pull (public image)...
%DOCKER_BIN% logout ghcr.io >nul 2>nul

echo [1/4] Pulling image %IMAGE% ...
%DOCKER_BIN% pull %IMAGE%
if not errorlevel 1 goto :pull_ok

echo Pull failed once. Retrying after logout from ghcr.io ...
%DOCKER_BIN% logout ghcr.io >nul 2>nul
%DOCKER_BIN% pull %IMAGE%
if errorlevel 1 goto :error_pull

:pull_ok

echo [2/4] Stopping old container if exists ...
%DOCKER_BIN% rm -f %CONTAINER% >nul 2>nul

echo [3/4] Starting PhoBiHSD GPU container ...
%DOCKER_BIN% run -d --gpus all --name %CONTAINER% -p %PORT%:7860 %IMAGE%
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

:error_pull
echo.
echo Failed to pull image from GHCR.
echo This image is public, so login is not required.
echo Try clearing cached credentials in Docker Desktop and rerun:
echo   Settings ^> Resources ^> Proxies/Credentials (or equivalent)
echo   then: docker logout ghcr.io
echo.
echo If needed, verify manually:
echo   docker pull %IMAGE%
exit /b 2
