from astropy.io import fits
import numpy as np

# Open the FITS file
hdul = fits.open('APOGEE_stars.fits')

# Access the primary data (in this case, it is a Table)
data = hdul[1].data  # Often, the first extension contains the table
colnames = hdul[1].columns.names # List of the column names

print(colnames)

sf = data["STARFLAG"] == 0
af = data["ASPCAPFLAG"] == 0
snr = data["SNR"] > 10
err = data["GAIAEDR3_PARALLAX"]/data["GAIAEDR3_PARALLAX_ERROR"] > 5
g = np.isnan(data["GAIAEDR3_PHOT_G_MEAN_MAG"]) == False
bp = np.isnan(data["GAIAEDR3_PHOT_BP_MEAN_MAG"]) == False
rp = np.isnan(data["GAIAEDR3_PHOT_RP_MEAN_MAG"]) == False

cucc = [err,err, g, bp, rp, af, sf,snr]

string = ''
for i in range (len(data['GAIAEDR3_PARALLAX'])):
    string += str(data['GAIAEDR3_PARALLAX'][i]/data['GAIAEDR3_PARALLAX_ERROR'][i])+'\t'+str(err[i])+'\n'
    
file = open('GAIAEDR3_PARALLAX.csv','w')
file.write(string)
file.close()

for n in range (2,len(colnames)):
    string = ''
    name = colnames[n]
    for i in range (len(data[name])):
        string += str(data[name][i])+'\t'+str(cucc[colnames.index(name)][i])+'\n'
    file = open(name+'.csv','w')
    file.write(string)
    file.close()