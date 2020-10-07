from .models import (
    OpticalPower,
    Radius,
    Brand,
    Material,
    SubCategory,
    Volume,
)

def getQS(id):
    res = {}
    if 'volume' in id:
        val = Volume.objects.filter(id=id['volume']).first()
        if val:
            res['id'] = id['volume']
            res['name'] = val.value
        else:
            res = None
    elif 'material' in id:
        val = Material.objects.filter(id=id['material']).first()
        if val:
            res['id'] = id['material']
            res['name'] = val.value
        else:
            res = None
    elif 'brand' in id:
        val = Brand.objects.filter(id=id['brand']).first()
        if val:
            res['id'] = id['brand']
            res['name'] = val.value
        else:
            res = None
    elif 'radius' in id:
        val = Radius.objects.filter(id=id['radius']).first()
        if val:
            res['id'] = id['radius']
            res['name'] = val.value
        else:
            res = None
    elif 'opt_power' in id:
        val = OpticalPower.objects.filter(id=id['opt_power']).first()
        if val:
            res['id'] = id['opt_power']
            res['name'] = val.value
        else:
            res = None
    return res
