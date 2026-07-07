# Create the folders
$folders = @("01_Foundations", "02_Infrastructure", "03_Scripting", "04_Operations", "05_Advanced")
foreach ($folder in $folders) { if (!(Test-Path $folder)) { New-Item -ItemType Directory -Path $folder } }

# Create files for Days 1-6
1..6 | ForEach-Object { New-Item -Path "01_Foundations/Day_$($_.ToString('00')).md" }

# Create files for Days 7-12
7..12 | ForEach-Object { New-Item -Path "02_Infrastructure/Day_$($_.ToString('00')).md" }

# Create files for Days 13-19
13..19 | ForEach-Object { New-Item -Path "03_Scripting/Day_$($_.ToString('00')).md" }

# Create files for Days 20-31
20..31 | ForEach-Object { New-Item -Path "04_Operations/Day_$($_.ToString('00')).md" }

# Create files for Days 32-36
32..36 | ForEach-Object { New-Item -Path "05_Advanced/Day_$($_.ToString('00')).md" }
