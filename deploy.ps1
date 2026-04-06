# Script de deploiement pour GesUsers2

$projectPath = "c:\Users\DELL\Downloads\jee\workspace\gesusers2"
$buildDir = "$projectPath\build"
$classesDir = "$buildDir\classes"
$distDir = "$buildDir\dist"
$webappDir = "$projectPath\src\main\webapp"
$warFile = "$distDir\gesusers2.war"

# Creer le repertoire dist
if (!(Test-Path $distDir)) {
    New-Item -ItemType Directory -Force -Path $distDir | Out-Null
    Write-Host "[OK] Repertoire dist cree"
}

# Compiler les fichiers Java
Write-Host "Compilation des fichiers Java..."
$srcDir = "$projectPath\src\main\java"
$javaFiles = Get-ChildItem -Path $srcDir -Recurse -Filter "*.java" | ForEach-Object { $_.FullName }

# Classpath: JSTL + Tomcat libs
$tomcatLib = "C:\Program Files\Apache Software Foundation\Tomcat 11.0\lib"
$tomcatJars = @(
    "$webappDir\WEB-INF\lib\jstl-1.2.jar",
    "$webappDir\WEB-INF\lib\standard-1.1.2.jar",
    "$tomcatLib\jakarta.servlet-api-6.1.0.jar",
    "$tomcatLib\jakarta.servlet.jsp-api-4.0.0.jar",
    "$tomcatLib\jakarta.servlet.jsp.jstl-api-3.0.0.jar"
) -join ";"

$javacPath = "C:\jdk-17.0.10\bin\javac.exe"

if (Test-Path $javacPath) {
    & $javacPath -d $classesDir -cp $tomcatJars $javaFiles 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[OK] Compilation reussie"
    } else {
        Write-Host "[ERREUR] Erreur de compilation"
        exit 1
    }
} else {
    Write-Host "[ERREUR] javac non trouve a $javacPath"
    exit 1
}

# Creer le WAR avec jar.exe
Write-Host "Creation du fichier WAR..."
$jarPath = "C:\jdk-17.0.10\bin\jar.exe"

if (Test-Path $jarPath) {
    $tempWarDir = "$buildDir\war_temp"
    if (Test-Path $tempWarDir) {
        Remove-Item -Recurse -Force $tempWarDir
    }
    Copy-Item -Path $webappDir -Destination $tempWarDir -Recurse
    Copy-Item -Path "$classesDir\*" -Destination "$tempWarDir\WEB-INF\classes" -Recurse -Force
    
    Push-Location $tempWarDir
    & $jarPath -cf $warFile -C . .
    Pop-Location
    
    if (Test-Path $warFile) {
        Write-Host "[OK] WAR cree: $warFile"
    } else {
        Write-Host "[ERREUR] Erreur lors de la creation du WAR"
        exit 1
    }
} else {
    Write-Host "[ERREUR] jar.exe non trouve a $jarPath"
    exit 1
}

# Copier le WAR vers Tomcat
$tomcatWebapps = "C:\Program Files\Apache Software Foundation\Tomcat 11.0\webapps"

if (Test-Path $tomcatWebapps) {
    Write-Host "Deploiement sur Tomcat..."
    Copy-Item -Path $warFile -Destination "$tomcatWebapps\gesusers2.war" -Force
    Write-Host "[OK] WAR deploye sur Tomcat"
    Write-Host ""
    Write-Host "Acces a l'application: http://localhost:8080/gesusers2"
    Write-Host "Attendez quelques secondes que Tomcat redploie..."
} else {
    Write-Host "[ERREUR] Tomcat non trouve a $tomcatWebapps"
    Write-Host "Verifiez l'installation de Tomcat"
    exit 1
}
