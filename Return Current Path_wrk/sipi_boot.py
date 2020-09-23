# -*- coding: utf-8 -*-

import empro.toolkit.sipi as sipi

def main():
	momentum_dir=r"C:\Program Files\Keysight\ADS2020_update2\Momentum\2020.20"
	try:
		sipi.setMomentumDir(momentum_dir)
	except:
		pass
	path=r"E:/Github/youtube-current-return-path/Return Current Path_wrk"
	lib=r"PCB02_lib"
	subst=r"PCB02_lib/PCB02.subst"
	substlib=r"PCB02_lib"
	substname=r"PCB02"
	ltdSubst=r"simulation/PCB02_lib/%P%C%B02/sipi%Setup/proj.ltd"
	cell=r"PCB02"
	layout=r"layout"
	sipiSetup=r"sipiSetup"
	libS3D=r"simulation/PCB02_lib/%P%C%B02/sipi%Setup/proj_libS3D.xml"
	varDictionary={}
	exprDictionary={}
	hpeesof_dir=r"C:\Program Files\Keysight\ADS2020_update2"

	sipi.loadDesign(path=path, lib=lib, subst=subst, substlib=substlib, substname=substname, ltd_subst=ltdSubst, cell=cell, layout_view=layout, sipi_view=sipiSetup, libS3D=libS3D, var_dict=varDictionary, expr_dict=exprDictionary, hpeesof_dir=hpeesof_dir)
