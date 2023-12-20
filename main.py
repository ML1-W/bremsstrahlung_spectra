# Created by E. Wilhelm at 10/10/2023
import matplotlib.pyplot as plt
from xpecgen import xpecgen as xg

plt.ioff()

s = xg.calculate_spectrum(300, 12, 3, 100, z=74)
# print(s.x, s.y)
# s.attenuate(0.12, xg.get_mu(13))
# s.attenuate(100, xg.get_mu("air"))
# s.export_xlsx("spectrum.xlsx")
# s.show_plot()


s2 = xg.calculate_spectrum(300, 12, 3, 100, z=82)
# s2.attenuate(0.12, xg.get_mu(13))
# s2.attenuate(100, xg.get_mu("air"))
# s2.export_xlsx("spectrum_z82.xlsx")
# s2.show_plot()

# The spectrum can be cloned so the original needn't be recalculated
s_attenuation = s.clone()
s_attenuation.attenuate(1.2, xg.get_mu(13))  # 1.2 mm of Al

plt.figure()
plt.plot(s.x, s.y, label="z=74")
plt.plot(s2.x, s2.y, label="z=82")
plt.legend()

plt.figure()
plt.plot(s2.x, s2.y, label="z=82, wo attenuation")
plt.plot(s_attenuation.x, s_attenuation.y, label="z=82, 1.2cm Al")
plt.legend()
plt.show()
