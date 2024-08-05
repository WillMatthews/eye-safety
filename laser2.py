import math

# https://onlinelibrary.wiley.com/doi/pdf/10.1002/9781118688977.app1

# Table A.1 Pathological effects of different wavelength ranges
# Wavelength range Pathological effect
# 180–315 nm Photokeratitis: inflammation of cornea, equivalent to sun burn
# 315–400 nm Photochemical cataract
# 400–780 nm Photochemical damage to retina, retinal burn
# 780–1400 nm Cataract, retinal burn
# 1.4–3.0mm Aqueous flare, cataract, corneal burn
# 3.0–1000mm Corneal burn


def calculate_correction_factors(wavelength, alpha=None):
    """Calculate correction factors based on wavelength."""

    if 0.400 <= wavelength < 0.700:
        CA = 1.0
    elif 0.700 <= wavelength < 1.050:
        CA = 10 ** (2 * (wavelength - 0.700))
    elif 1.050 <= wavelength <= 1.400:
        CA = 5.0
    else:
        CA = None
    
    if 0.400 <= wavelength < 0.450:
        CB = 1.0
    elif 0.450 <= wavelength < 0.600:
        CB = 10 ** (20 * (wavelength - 0.450))
    else:
        CB = None
    
    if 1.050 <= wavelength < 1.150:
        CC = 1.0
    elif 1.150 <= wavelength < 1.200:
        CC = 10 ** (18 * (wavelength - 1.150))
    elif 1.200 <= wavelength <= 1.400:
        CC = 8.0
    else:
        CC = None
    
    if alpha is not None and 0.400 <= wavelength <= 1.400:
        alpha_min = 1.5e-3  # 1.5 mrad
        alpha_max = 100e-3  # 100 mrad
        if alpha < alpha_min:
            CE = 1.0
        elif alpha_min <= alpha <= alpha_max:
            CE = alpha / alpha_min
        else: # alpha > alpha_max
            CE = alpha**2 / (alpha_min * alpha_max)
    else:
        CE = None

    # if 0.180 <= wavelength < 1.000:
    #     CP = n ** -0.25
    # else:
    #     CP = None

    if 0.450 <= wavelength < 0.500:
        T1 = 10 * 10 ** (20 * (wavelength - 0.450))
    else:
        T1 = None

    if 0.400 <= wavelength < 1.400 and alpha is not None:
        if alpha < 1.5e-3:
            T2 = 10.0
        elif alpha > 100e-3:
            T2 = 100.0
        else:
            T2 = 10 * 10 ** ((alpha - 0.15)/98.5)
    else:
        T2 = None
    
    return CA, CB, CC, CE, T1, T2


# CHECK THIS! Compare to Table A.4
def calculate_mpe_ocular(wavelength, time):
    """Calculate MPE for ocular exposure."""
    CA, CB, CC, CE, T1, T2 = calculate_correction_factors(wavelength)
    
    if 0.180 <= wavelength < 0.302:
        return 3e-3, None
    elif 0.302 <= wavelength < 0.315:
        return 3e-3 * 10**(0.302 - wavelength), None
    elif 0.315 <= wavelength < 0.400:
        if time <= 10:
            return 0.56 * time**0.25, None
        else:
            return 1.0, None
    elif 0.400 <= wavelength < 0.700:
        if time <= 18e-6:
            return 5e-7, None
        elif 18e-6 < time <= 0.25:
            return 1.8 * time**0.75 * 1e-3, None
        elif 0.25 < time <= 3e4:
            if 0.400 <= wavelength < 0.450:
                return None, 1e-3
            elif 0.450 <= wavelength < 0.700:
                return None, CB * 1e-3
    elif 0.700 <= wavelength < 1.050:
        if time <= 18e-6:
            return 5.0 * CA * 1e-7, None
        elif 18e-6 < time <= 0.25:
            return 1.8 * CA * time**0.75 * 1e-3, None
        else:
            return None, CA * 1e-3
    elif 1.050 <= wavelength < 1.400:
        if time <= 50e-6:
            return 5.0 * CC * 1e-6, None
        elif 50e-6 < time <= 0.25:
            return 9.0 * CC * time**0.75 * 1e-3, None
        else:
            return None, 5.0 * CC * 1e-3
    elif 1.400 <= wavelength <= 2.600:
        if time <= 1e-3:
            return 0.1, None
        elif 1e-3 < time <= 0.25:
            return 0.56 * time**0.25, None
        else:
            return None, 0.1
    elif 2.600 < wavelength <= 1000:
        if time <= 1e-7:
            return 1e-2, None
        elif 1e-7 < time <= 0.25:
            return 0.56 * time**0.25, None
        else:
            return None, 0.1
    
    return None, None


# CHECK THIS! Compare to Table A.5
def calculate_mpe_skin(wavelength, time):
    """Calculate MPE for skin exposure."""
    CA, CB, CC, CE, T1, T2 = calculate_correction_factors(wavelength)
    
    if 0.180 <= wavelength < 0.302:
        return 3e-3, None
    elif 0.302 <= wavelength < 0.315:
        # WRONG! Check Table A.5
        return 3e-3 * 10**(0.302 - wavelength), None 
    elif 0.315 <= wavelength < 0.400:
        if time <= 10:
            return 0.56 * time**0.25, None
        elif 10 < time <= 1e3:
            return 1.0, None
        else:
            return None, 1e-3
    elif 0.400 <= wavelength <= 1.400:
        if time <= 1e-7:
            return 2 * CA * 1e-2, None
        elif 1e-7 < time <= 0.25:
            return 1.1 * CA * time**0.25, None
        else:
            return None, 0.2 * CA
    elif 1.400 < wavelength <= 1.500:
        if time <= 1e-3:
            return 0.1, None
        elif 1e-3 < time <= 0.25:
            return 0.56 * time**0.25, None
        else:
            return None, 0.1
    elif 1.500 < wavelength <= 1.800:
        if time <= 0.25:
            return 1.0, None
        else:
            return None, 0.1
    elif 1.800 < wavelength <= 2.600:
        if time <= 1e-3:
            return 0.1, None
        elif 1e-3 < time <= 0.25:
            return 0.56 * time**0.25, None
        else:
            return None, 0.1
    elif 2.600 < wavelength <= 1000:
        if time <= 1e-7:
            return 1e-2, None
        elif 1e-7 < time <= 0.25:
            return 0.56 * time**0.25, None
        else:
            return None, 0.1
    
    return None, None

def format_output(value, unit):
    """Format the output with appropriate units."""
    if value is not None:
        return f"{value:.2e} {unit}"
    return "N/A"

def calculate_mpe(wavelength, time):
    """Calculate and display MPE for both ocular and skin exposure."""
    ocular_energy, ocular_irradiance = calculate_mpe_ocular(wavelength, time)
    skin_energy, skin_irradiance = calculate_mpe_skin(wavelength, time)
    
    print(f"Wavelength: {wavelength:.3f} μm, Exposure time: {time:.2e} s")
    print("\nMPE for ocular exposure (intra-beam viewing):")
    print(f"Energy: {format_output(ocular_energy, 'J/cm^2')}")
    print(f"Irradiance: {format_output(ocular_irradiance, 'W/cm^2')}")
    
    print("\nMPE for skin exposure:")
    print(f"Energy: {format_output(skin_energy, 'J/cm^2')}")
    print(f"Irradiance: {format_output(skin_irradiance, 'W/cm^2')}")


if __name__ == "__main__":
    # Example usage
    wavelength = 0.532  # μm (e.g., green laser)
    exposure_time = 0.25  # seconds

    calculate_mpe(wavelength, exposure_time)
