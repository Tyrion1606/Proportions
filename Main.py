while True:
	WideProportion_Hypo = ((16**2) + (9**2))**(1/2)
	WideProportion_LengthCateto = 9/WideProportion_Hypo
	WideProportion_WidthCateto = 16/WideProportion_Hypo
	
	UltraWideProportion_Hypo = ((21**2) + (9**2))**(1/2)
	UltraWideProportion_LengthCateto = 9/UltraWideProportion_Hypo
	UltraWideProportion_WidthCateto = 21/UltraWideProportion_Hypo
	
	MonitorSize = float(input("Quantas polegadas tem o monitor?"))
	Uy = UltraWideProportion_LengthCateto * MonitorSize
	Ux = UltraWideProportion_WidthCateto * MonitorSize
	Wy = WideProportion_LengthCateto * MonitorSize
	Wx = WideProportion_WidthCateto * MonitorSize
	
	print("Ultrawide: %.1f x %.1f  Área: %.2f\n	 Wide: %.1f x %.1f  Área: %.2f\n" % (Ux,Uy,(Ux*Uy),Wx,Wy,(Wx*Wy)))
	