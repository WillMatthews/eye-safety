# eye-safety
laser and LED safety calculation code

# Introduction
I generally struggled to get "gut feeling" estimates of laser and LED safety calculations. This code is an attempt to make that easier.
It is based on the Appendix A of [Lasers and Optoelectronics: Fundamentals, Devices and Applications](https://onlinelibrary.wiley.com/doi/pdf/10.1002/9781118688977.app1) by Anil K. Maini.

LEDs, similar to lasers, can present ocular and skin hazards.
Unlike lasers, LEDs have a completely separate set of safety standards and calculations, which are incoherent with laser safety standards.
Weirdly, the only LED safety standard that I know of is BS EN 62471:2008, which is a measurement standard, not necessarily a safety standard.

Nonetheless, we can use a combination of the two standards to get a rough estimate of the safety of LEDs, and an idea of laser standards.

# Assumptions
1. You know what the irradiance of the laser or LED is in W/m^2.
2. You know the wavelength of the laser or LED in nm.
3. You can assume that the laser or LED is monocromatic (not sure how strong this assumption is -- need to check).


# WARNING
CONSULT YOUR LASER SAFETY OFFICER BEFORE EVEN THINKING ABOUT USING THIS CODE. THIS CODE IS PROVIDED AS IS AND WITHOUT WARRANTY. USE AT YOUR OWN RISK.
I make NO guarantees that this code is correct or that it will keep you safe. I am not responsible for any harm that comes to you or others as a result of using this code.

This code will NOT replace a proper laser safety analysis. It is only meant to give you a rough idea of what the safety of a laser or LED is.
Use a real laser safety calculator, like [LaserBee](https://www.laserphysics.co.uk/store/laser-safety/laserbee-software) (or [here](https://lucidos.co.uk/blog/led-laser-safety/laserbee/)).
Real laser safety calculators will take into account the beam diameter, divergence, and other factors that this code does not.
This code is a blunt instrument, and should be used as such.
In general, if you have ANY doubt, ask a laser safety officer.

