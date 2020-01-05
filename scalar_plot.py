import nt_vtk

#%%
data = nt_vtk.Data("test/PELOOP.00001000.dat",nt_vtk.SCALAR)
data.get_np_array()
data.get_vtk_file('output/test.vtk',0)
data.get_dat_file('output/test.dat')

#%%