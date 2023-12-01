import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from EdgeExtractor import EdgeExtractor

matrices_folder = 'C:/Users/Julia/Documents/NSS_lab/autoencoder_ice_forecasting/matrices/osisaf/test/'
mask_folder = 'C:/Users/Julia/Documents/NSS_lab/autoencoder_ice_forecasting/supporting_files/osi_land_mask.npy'
rough_mask_folder = 'C:/Users/Julia/Documents/NSS_lab/autoencoder_ice_forecasting/supporting_files/rough_land_mask.npy'


dates_range = pd.date_range('20190218', '20200101')
files = [date.strftime('osi_iceconc_%Y%m%d.npy') for date in dates_range]
mask = np.load(mask_folder)
mask[58:, :] = 1
rough_mask = np.load(rough_mask_folder)
rough_mask[58:, :] = 1

extractor = EdgeExtractor(mask)
for file in files:
    matrix = np.load(f'{matrices_folder}/{file}')
    matrix[matrix >= 0.8] = 1
    matrix[matrix < 0.8] = 0

    edge = extractor.extract_max_edge(matrix, to_length=100)
    plt.imshow(matrix)
    if edge!=[]:
        plt.scatter(edge[:, 0], edge[:, 1], c='g', s=8)
    plt.title(file)
    plt.savefig(f'C:/Users/Julia/Pictures/test_edge2/{file}.png')
    plt.show()

'''    edges = extractor.extract_edges(matrix)
    plt.imshow(matrix)
    for e in edges:
        plt.scatter(e[:, 0], e[:, 1], c='g', s=8)
    plt.title(file)
    plt.show()'''
