#!/bin/bash
echo "Starting simulations"
time python MDCore.py gas.xyz gasin.txt
cp kineticenergytime.png GasKinCam.png
cp potentialenergytime.png GasPotCam.png
cp energytime.png GasEnCam.png
cp Msdtime.png GasMsdCam.png
echo "Cameron gas done"
time python MDCore.py liquid.xyz liquidin.txt
cp kineticenergytime.png LiqKinCam.png
cp potentialenergytime.png LiqPotCam.png
cp energytime.png LiqEnCam.png
cp Msdtime.png LiqMsdCam.png
echo "Cameron liquid done"
time python MDCore.py solid.xyz solidin.txt
cp kineticenergytime.png SolKinCam.png
cp potentialenergytime.png SolPotCam.png
cp energytime.png SolEnCam.png
cp Msdtime.png SolMsdCam.png
echo "Cameron solid done"

