import glob
import sys
import rasterio
from rasterio.merge import merge

def create_filestomosaic(path):
    images_to_mosaic = glob.glob(path + '*.tif')
    src_files=[]

    for fp in images_to_mosaic:
        src = rasterio.open(fp)
        src_files.append(src)
        out_meta = src.meta.copy()

    return out_meta, src.crs, src_files

def gen_mosaic(bits,type):
    out_meta, crs, src_files_to_mosaic = create_filestomosaic(path)

    mosaic, out_trans = merge(src_files_to_mosaic, dtype=type)

    return crs, out_meta, mosaic, out_trans

def create_mosaic(bits):
    if bits == 8:
        type = rasterio.uint8
    else:
        type = rasterio.uint16

    crs, out_meta, mosaic, out_trans = gen_mosaic(bits,type)
    out_meta.update({"driver": "GTiff",
                     "height": mosaic.shape[1],
                     "width": mosaic.shape[2],
                     "transform": out_trans,
                     "dtype": type,
                     "compress": 'JPEG',
                     "crs": crs
                     }
                    )

    with rasterio.open(
            path+'rasterio.jpeg',
            "w", **out_meta) as dest:
        dest.write(mosaic.astype(type))

    return

if __name__ == '__main__':
    args = sys.argv
    bits = int(args[1])
    path = str(args[2])
    create_mosaic(bits)