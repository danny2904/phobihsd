@echo off
setlocal EnableExtensions

title PhoBiHSD Launcher (CPU)
set "LOG=%~dp0Run-PhoBiHSD.log"
echo [%date% %time%] Starting Run-PhoBiHSD.bat > "%LOG%"

echo ==============================================
echo PhoBiHSD CPU Launcher

echo ==============================================
echo Log file: "%LOG%"
echo.

call :main
set "EXITCODE=%errorlevel%"

>> "%LOG%" echo [%date% %time%] ExitCode=%EXITCODE%
echo.
echo ExitCode=%EXITCODE%
if not "%EXITCODE%"=="0" (
  echo Failed. Open log file for details.
)
pause
exit /b %EXITCODE%

:main
set "IMAGE=ghcr.io/danny2904/phobihsd:cpu-latest"
set "CONTAINER=phobihsd"
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
  call :log Docker CLI not found. Install Docker Desktop first.
  exit /b 10
)

call :log [check] Using docker command: %DOCKER_BIN%
%DOCKER_BIN% info >nul 2>&1
if not "%errorlevel%"=="0" (
  call :log Docker daemon is not ready. Start Docker Desktop and wait until status is Running.
  exit /b 11
)

call :log [prep] Resetting GHCR auth cache to use anonymous pull...
%DOCKER_BIN% logout ghcr.io >nul 2>nul

call :log [1/4] Pulling image %IMAGE% ...
%DOCKER_BIN% pull %IMAGE%
if not errorlevel 1 goto :pull_ok

call :log Pull failed once. Retrying after logout from ghcr.io ...
%DOCKER_BIN% logout ghcr.io >nul 2>nul
%DOCKER_BIN% pull %IMAGE%
if errorlevel 1 goto :error_pull

:pull_ok
call :log [2/4] Stopping old container if exists ...
%DOCKER_BIN% rm -f %CONTAINER% >nul 2>nul

call :log [3/4] Starting PhoBiHSD container ...
%DOCKER_BIN% run -d --name %CONTAINER% -p %PORT%:7860 %IMAGE%
if errorlevel 1 goto :error

call :log [4/4] Opening app in browser ...
start http://localhost:%PORT%

call :log PhoBiHSD is starting at http://localhost:%PORT%
call :log Note: first run may need a few minutes to download pretrained model.
exit /b 0

:error
call :log Failed to run container. Ensure Docker Desktop is running.
exit /b 1

:error_pull
call :log Failed to pull image from GHCR.
call :log This image is public, login is not required.
call :log Try: docker logout ghcr.io
call :log Then verify: docker pull %IMAGE%
exit /b 2

:log
echo %*
>> "%LOG%" echo [%date% %time%] %*
exit /b 0
