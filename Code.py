import os
import ansa
from ansa import mesh, base, constants
import time
def main():
    comp_array = base.CollectEntities(constants.FLUENT, None, "__PROPERTIES__")
    # print(comp_array[0])
    total_off = sum([base.CalculateOffElements(comp)['TOTAL OFF'] for comp in comp_array])
    print('Total number of OFF elements = ', total_off)

    def offs_per_comp(comp, ind=0):
        id = int(str(comp).split(':')[-1].split('>')[0])
        try:
        	component_off = base.CalculateOffElements(comp)['TOTAL OFF']
        	elem_count = len(base.CollectEntities(constants.FLUENT, comp, "__ELEMENTS__"))
        	percent_off = (component_off*100)/elem_count
        	print(f'Total number of OFF elements in component {id}\t:\t{component_off} ({round(percent_off, 5)}%)')
        except:
        	print(f'This component ({id}) has no elements')
        

    for ind_, comp_ in enumerate(comp_array):
        offs_per_comp(comp_, ind_)

    n_off = 1.1
    while total_off != n_off:
        n_off = total_off
        mesh.FixQuality()
        total_off = sum([base.CalculateOffElements(comp)['TOTAL OFF'] for comp in comp_array])

    print('\nFIX QUALITY METHOD')
    print('Total number of OFF elements = ', total_off)
    if total_off != 0:
    	for ind_, comp_ in enumerate(comp_array):
        	offs_per_comp(comp_, ind_)


    #2
    i = 0
    while total_off != 0:
    	if i == 0:
    		print('\nMESH RECONSTRUCT METHOD')
    	print(f'\nExpand Level : {i}')
    	mesh.ReconstructViolatingShells(i)
    	i+=1
    	total_off = sum([base.CalculateOffElements(comp)['TOTAL OFF'] for comp in comp_array])
    	
    	print('Total number of OFF elements = ', total_off)
    	if total_off != 0:
    		for ind_, comp_ in enumerate(comp_array):
        		offs_per_comp(comp_, ind_)

    def compute_skews():
    	elems = base.CollectEntities(constants.FLUENT, None, "__ELEMENTS__")
    	qual = [base.ElementQuality(elem, "SKEW") for elem in elems]
    	skews = [elem for elem in qual if elem >= 0.6]
    	return max(qual), len(skews)
    skew_info = compute_skews()
    print(f'\nProcess Complete.\nTotal Skew = {skew_info[1]}\nMaximum Skew = {skew_info[0]}\n')

start = time.time()
main()
print(f'Time taken for code completion: {round(time.time() - start, 4)} seconds\n')
