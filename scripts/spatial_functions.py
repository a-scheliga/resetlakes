from shapely import Polygon


def polygon_from_bbox(minx,miny,maxx,maxy):
    """
    Create a shapely Polygon from bounding box values.

    Inputs
    ------
    minx, miny, maxx, maxy : float
        Typical order of a Geopandas bounding box output.

    Outputs
    -------
    polygon : shapely Polygon
    """
    coords_tuple = ((minx,miny),(maxx,miny),(maxx,maxy),(minx,maxy),(minx,miny))
    polygon = Polygon(coords_tuple)
    return polygon