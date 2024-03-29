# Gaia_spec

[![astropy](http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat)](http://www.astropy.org/)

``Spec_compare`` is a Python module to compare Gaia low-resolution BP-RP spectra to templates created from Gaia spectra of confirmed spectral types (A0V-L1V).

## Module dependencies

The Python Standard Library, NumPy, Matplotlib, Astropy, Specutils and GaiaXPy (which is the Gaia BP/RP spectra package)

## Installation

The code can be installed as follows:
```
git clone https://github.com/fkiwy/Gaia_spec.git
cd Gaia_spec
python setup.py install
```

## Example usage

```
from speccomp.Spec_compare import compare_spectra

sources = [58925512487888896, 378026395579692672, 200296663143599104, 1204754033223498624]  # K5, M0, M5, M9

results = compare_spectra(sources, plot_spectrum=True, plot_template=True, spectrum_uncertainty=True, template_uncertainty=True)

for result in results:
    print('Gaia source id:', result[0], 'Matched tempalte:', result[2])
```

### Console output:
```
Gaia source id: 58925512487888896 Matched tempalte: K5V
Gaia source id: 378026395579692672 Matched tempalte: M0V
Gaia source id: 200296663143599104 Matched tempalte: M5V
Gaia source id: 1204754033223498624 Matched tempalte: M9V
```

### Plots:
![K5](examples/K5V_58925512487888896.png)
![M0](examples/M0V_378026395579692672.png)
![M5](examples/M5V_200296663143599104.png)
![M9](examples/M9V_1204754033223498624.png)


### Parameters:
``sources`` : A list of Gaia source identifiers to download spectra for. At least one is required e.g. [1657463068195202432]  
``plot_spectrum`` : Whether to plot the downloaded Gaia spectra. The default is True. (bool, optional)  
``plot_template`` : Whether to overplot the matched templates. The default is True. (bool, optional)  
``spectrum_uncertainty`` : Whether to plot the spectra uncertainty. The default is False. (bool, optional)  
``template_uncertainty`` : Whether to plot the templates uncertainty. The default is False. (bool, optional)  
``output_dir`` : The directory where the plots will be saved to. The default is tempfile.gettempdir(). (str, optional)  
``file_format`` : Output file format: pdf, png, eps, etc.. The default is 'pdf'. (str, optional)  

### Returns:
A list containing one row per source including the Gaia source id, the Gaia spectrum, the matched spectral type and the matched template.
All spectra and tempaltes are instances of ``specutils.Spectrum1D``.
Wavelength, flux and error arrays can be extracted as follows:
- ``Spectrum1D.spectral_axis.value``
- ``Spectrum1D.flux.value``
- ``Spectrum1D.uncertainty.array``

<br/>

``Spec_compare`` uses [GaiaXPy](https://gaia-dpci.github.io/GaiaXPy-website), the Gaia BP/RP spectra package.
