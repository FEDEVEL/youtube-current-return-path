# -*- coding: utf-8 -*-

import empro.toolkit.sipi as sipi

def main():
	path=r"E:/Github/youtube-current-return-path/Return Current Path_wrk"
	lib=r"PCB02_lib"
	subst=r"PCB02_lib/PCB02.subst"
	substlib=r"PCB02_lib"
	substname=r"PCB02"
	ltdSubst=r"simulation/PCB02_lib/%P%C%B02/rfpro/proj.ltd"
	cell=r"PCB02"
	layout=r"layout"
	sipiSetup=r"rfpro"
	libS3D=r"simulation/PCB02_lib/%P%C%B02/rfpro/proj_libS3D.xml"
	varDictionary={}
	exprDictionary={}
	sipi.loadDesign(path=path, lib=lib, subst=subst, substlib=substlib, substname=substname, ltd_subst=ltdSubst, cell=cell, layout_view=layout, sipi_view=sipiSetup, libS3D=libS3D, var_dict=varDictionary, expr_dict=exprDictionary)
