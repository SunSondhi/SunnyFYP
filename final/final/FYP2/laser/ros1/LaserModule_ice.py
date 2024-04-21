# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.10
#
# <auto-generated>
#
# Generated from file `LaserModule.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module LaserModule
_M_LaserModule = Ice.openModule('LaserModule')
__name__ = 'LaserModule'

if '_t_Floats' not in _M_LaserModule.__dict__:
    _M_LaserModule._t_Floats = IcePy.defineSequence('::LaserModule::Floats', (), IcePy._t_float)

if 'LaserScan' not in _M_LaserModule.__dict__:
    _M_LaserModule.LaserScan = Ice.createTempClass()
    class LaserScan(object):
        def __init__(self, seq=0, sec=0, nsec=0, frameId='', angleMin=0.0, angleMax=0.0, angleIncrement=0.0, timeIncrement=0.0, scanTime=0.0, rangeMin=0.0, rangeMax=0.0, ranges=None, intensities=None):
            self.seq = seq
            self.sec = sec
            self.nsec = nsec
            self.frameId = frameId
            self.angleMin = angleMin
            self.angleMax = angleMax
            self.angleIncrement = angleIncrement
            self.timeIncrement = timeIncrement
            self.scanTime = scanTime
            self.rangeMin = rangeMin
            self.rangeMax = rangeMax
            self.ranges = ranges
            self.intensities = intensities

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_LaserModule.LaserScan):
                return NotImplemented
            else:
                if self.seq != other.seq:
                    return False
                if self.sec != other.sec:
                    return False
                if self.nsec != other.nsec:
                    return False
                if self.frameId != other.frameId:
                    return False
                if self.angleMin != other.angleMin:
                    return False
                if self.angleMax != other.angleMax:
                    return False
                if self.angleIncrement != other.angleIncrement:
                    return False
                if self.timeIncrement != other.timeIncrement:
                    return False
                if self.scanTime != other.scanTime:
                    return False
                if self.rangeMin != other.rangeMin:
                    return False
                if self.rangeMax != other.rangeMax:
                    return False
                if self.ranges != other.ranges:
                    return False
                if self.intensities != other.intensities:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_LaserModule._t_LaserScan)

        __repr__ = __str__

    _M_LaserModule._t_LaserScan = IcePy.defineStruct('::LaserModule::LaserScan', LaserScan, (), (
        ('seq', (), IcePy._t_int),
        ('sec', (), IcePy._t_int),
        ('nsec', (), IcePy._t_int),
        ('frameId', (), IcePy._t_string),
        ('angleMin', (), IcePy._t_float),
        ('angleMax', (), IcePy._t_float),
        ('angleIncrement', (), IcePy._t_float),
        ('timeIncrement', (), IcePy._t_float),
        ('scanTime', (), IcePy._t_float),
        ('rangeMin', (), IcePy._t_float),
        ('rangeMax', (), IcePy._t_float),
        ('ranges', (), _M_LaserModule._t_Floats),
        ('intensities', (), _M_LaserModule._t_Floats)
    ))

    _M_LaserModule.LaserScan = LaserScan
    del LaserScan

_M_LaserModule._t_LaserData = IcePy.defineValue('::LaserModule::LaserData', Ice.Value, -1, (), False, True, None, ())

if 'LaserDataPrx' not in _M_LaserModule.__dict__:
    _M_LaserModule.LaserDataPrx = Ice.createTempClass()
    class LaserDataPrx(Ice.ObjectPrx):

        def publishLaserScan(self, scan, context=None):
            return _M_LaserModule.LaserData._op_publishLaserScan.invoke(self, ((scan, ), context))

        def publishLaserScanAsync(self, scan, context=None):
            return _M_LaserModule.LaserData._op_publishLaserScan.invokeAsync(self, ((scan, ), context))

        def begin_publishLaserScan(self, scan, _response=None, _ex=None, _sent=None, context=None):
            return _M_LaserModule.LaserData._op_publishLaserScan.begin(self, ((scan, ), _response, _ex, _sent, context))

        def end_publishLaserScan(self, _r):
            return _M_LaserModule.LaserData._op_publishLaserScan.end(self, _r)

        def getLatestLaserData(self, context=None):
            return _M_LaserModule.LaserData._op_getLatestLaserData.invoke(self, ((), context))

        def getLatestLaserDataAsync(self, context=None):
            return _M_LaserModule.LaserData._op_getLatestLaserData.invokeAsync(self, ((), context))

        def begin_getLatestLaserData(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_LaserModule.LaserData._op_getLatestLaserData.begin(self, ((), _response, _ex, _sent, context))

        def end_getLatestLaserData(self, _r):
            return _M_LaserModule.LaserData._op_getLatestLaserData.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_LaserModule.LaserDataPrx.ice_checkedCast(proxy, '::LaserModule::LaserData', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_LaserModule.LaserDataPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::LaserModule::LaserData'
    _M_LaserModule._t_LaserDataPrx = IcePy.defineProxy('::LaserModule::LaserData', LaserDataPrx)

    _M_LaserModule.LaserDataPrx = LaserDataPrx
    del LaserDataPrx

    _M_LaserModule.LaserData = Ice.createTempClass()
    class LaserData(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::LaserModule::LaserData')

        def ice_id(self, current=None):
            return '::LaserModule::LaserData'

        @staticmethod
        def ice_staticId():
            return '::LaserModule::LaserData'

        def publishLaserScan(self, scan, current=None):
            raise NotImplementedError("servant method 'publishLaserScan' not implemented")

        def getLatestLaserData(self, current=None):
            raise NotImplementedError("servant method 'getLatestLaserData' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_LaserModule._t_LaserDataDisp)

        __repr__ = __str__

    _M_LaserModule._t_LaserDataDisp = IcePy.defineClass('::LaserModule::LaserData', LaserData, (), None, ())
    LaserData._ice_type = _M_LaserModule._t_LaserDataDisp

    LaserData._op_publishLaserScan = IcePy.Operation('publishLaserScan', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_LaserModule._t_LaserScan, False, 0),), (), None, ())
    LaserData._op_getLatestLaserData = IcePy.Operation('getLatestLaserData', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_LaserModule._t_LaserScan, False, 0), ())

    _M_LaserModule.LaserData = LaserData
    del LaserData

# End of module LaserModule
