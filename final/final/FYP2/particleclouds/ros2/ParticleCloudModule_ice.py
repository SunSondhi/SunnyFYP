# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.10
#
# <auto-generated>
#
# Generated from file `ParticleCloudModule.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module ParticleCloudModule
_M_ParticleCloudModule = Ice.openModule('ParticleCloudModule')
__name__ = 'ParticleCloudModule'

if 'Pose' not in _M_ParticleCloudModule.__dict__:
    _M_ParticleCloudModule.Pose = Ice.createTempClass()
    class Pose(object):
        def __init__(self, positionx=0.0, positiony=0.0, positionz=0.0, orientationx=0.0, orientationy=0.0, orientationz=0.0, orientationw=0.0):
            self.positionx = positionx
            self.positiony = positiony
            self.positionz = positionz
            self.orientationx = orientationx
            self.orientationy = orientationy
            self.orientationz = orientationz
            self.orientationw = orientationw

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_ParticleCloudModule.Pose):
                return NotImplemented
            else:
                if self.positionx != other.positionx:
                    return False
                if self.positiony != other.positiony:
                    return False
                if self.positionz != other.positionz:
                    return False
                if self.orientationx != other.orientationx:
                    return False
                if self.orientationy != other.orientationy:
                    return False
                if self.orientationz != other.orientationz:
                    return False
                if self.orientationw != other.orientationw:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_ParticleCloudModule._t_Pose)

        __repr__ = __str__

    _M_ParticleCloudModule._t_Pose = IcePy.defineStruct('::ParticleCloudModule::Pose', Pose, (), (
        ('positionx', (), IcePy._t_double),
        ('positiony', (), IcePy._t_double),
        ('positionz', (), IcePy._t_double),
        ('orientationx', (), IcePy._t_double),
        ('orientationy', (), IcePy._t_double),
        ('orientationz', (), IcePy._t_double),
        ('orientationw', (), IcePy._t_double)
    ))

    _M_ParticleCloudModule.Pose = Pose
    del Pose

if 'Time' not in _M_ParticleCloudModule.__dict__:
    _M_ParticleCloudModule.Time = Ice.createTempClass()
    class Time(object):
        def __init__(self, secs=0, nsecs=0):
            self.secs = secs
            self.nsecs = nsecs

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.secs)
            _h = 5 * _h + Ice.getHash(self.nsecs)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_ParticleCloudModule.Time):
                return NotImplemented
            else:
                if self.secs is None or other.secs is None:
                    if self.secs != other.secs:
                        return (-1 if self.secs is None else 1)
                else:
                    if self.secs < other.secs:
                        return -1
                    elif self.secs > other.secs:
                        return 1
                if self.nsecs is None or other.nsecs is None:
                    if self.nsecs != other.nsecs:
                        return (-1 if self.nsecs is None else 1)
                else:
                    if self.nsecs < other.nsecs:
                        return -1
                    elif self.nsecs > other.nsecs:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_ParticleCloudModule._t_Time)

        __repr__ = __str__

    _M_ParticleCloudModule._t_Time = IcePy.defineStruct('::ParticleCloudModule::Time', Time, (), (
        ('secs', (), IcePy._t_long),
        ('nsecs', (), IcePy._t_long)
    ))

    _M_ParticleCloudModule.Time = Time
    del Time

if 'Header' not in _M_ParticleCloudModule.__dict__:
    _M_ParticleCloudModule.Header = Ice.createTempClass()
    class Header(object):
        def __init__(self, seq=0, stamp=Ice._struct_marker, frameid=''):
            self.seq = seq
            if stamp is Ice._struct_marker:
                self.stamp = _M_ParticleCloudModule.Time()
            else:
                self.stamp = stamp
            self.frameid = frameid

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.seq)
            _h = 5 * _h + Ice.getHash(self.stamp)
            _h = 5 * _h + Ice.getHash(self.frameid)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_ParticleCloudModule.Header):
                return NotImplemented
            else:
                if self.seq is None or other.seq is None:
                    if self.seq != other.seq:
                        return (-1 if self.seq is None else 1)
                else:
                    if self.seq < other.seq:
                        return -1
                    elif self.seq > other.seq:
                        return 1
                if self.stamp is None or other.stamp is None:
                    if self.stamp != other.stamp:
                        return (-1 if self.stamp is None else 1)
                else:
                    if self.stamp < other.stamp:
                        return -1
                    elif self.stamp > other.stamp:
                        return 1
                if self.frameid is None or other.frameid is None:
                    if self.frameid != other.frameid:
                        return (-1 if self.frameid is None else 1)
                else:
                    if self.frameid < other.frameid:
                        return -1
                    elif self.frameid > other.frameid:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_ParticleCloudModule._t_Header)

        __repr__ = __str__

    _M_ParticleCloudModule._t_Header = IcePy.defineStruct('::ParticleCloudModule::Header', Header, (), (
        ('seq', (), IcePy._t_long),
        ('stamp', (), _M_ParticleCloudModule._t_Time),
        ('frameid', (), IcePy._t_string)
    ))

    _M_ParticleCloudModule.Header = Header
    del Header

if '_t_Poses' not in _M_ParticleCloudModule.__dict__:
    _M_ParticleCloudModule._t_Poses = IcePy.defineSequence('::ParticleCloudModule::Poses', (), _M_ParticleCloudModule._t_Pose)

if 'ParticleCloudData' not in _M_ParticleCloudModule.__dict__:
    _M_ParticleCloudModule.ParticleCloudData = Ice.createTempClass()
    class ParticleCloudData(object):
        def __init__(self, header=Ice._struct_marker, poses=None):
            if header is Ice._struct_marker:
                self.header = _M_ParticleCloudModule.Header()
            else:
                self.header = header
            self.poses = poses

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_ParticleCloudModule.ParticleCloudData):
                return NotImplemented
            else:
                if self.header != other.header:
                    return False
                if self.poses != other.poses:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_ParticleCloudModule._t_ParticleCloudData)

        __repr__ = __str__

    _M_ParticleCloudModule._t_ParticleCloudData = IcePy.defineStruct('::ParticleCloudModule::ParticleCloudData', ParticleCloudData, (), (
        ('header', (), _M_ParticleCloudModule._t_Header),
        ('poses', (), _M_ParticleCloudModule._t_Poses)
    ))

    _M_ParticleCloudModule.ParticleCloudData = ParticleCloudData
    del ParticleCloudData

_M_ParticleCloudModule._t_ParticleCloud = IcePy.defineValue('::ParticleCloudModule::ParticleCloud', Ice.Value, -1, (), False, True, None, ())

if 'ParticleCloudPrx' not in _M_ParticleCloudModule.__dict__:
    _M_ParticleCloudModule.ParticleCloudPrx = Ice.createTempClass()
    class ParticleCloudPrx(Ice.ObjectPrx):

        def receiveParticleCloudData(self, data, context=None):
            return _M_ParticleCloudModule.ParticleCloud._op_receiveParticleCloudData.invoke(self, ((data, ), context))

        def receiveParticleCloudDataAsync(self, data, context=None):
            return _M_ParticleCloudModule.ParticleCloud._op_receiveParticleCloudData.invokeAsync(self, ((data, ), context))

        def begin_receiveParticleCloudData(self, data, _response=None, _ex=None, _sent=None, context=None):
            return _M_ParticleCloudModule.ParticleCloud._op_receiveParticleCloudData.begin(self, ((data, ), _response, _ex, _sent, context))

        def end_receiveParticleCloudData(self, _r):
            return _M_ParticleCloudModule.ParticleCloud._op_receiveParticleCloudData.end(self, _r)

        def getParticleCloudData(self, context=None):
            return _M_ParticleCloudModule.ParticleCloud._op_getParticleCloudData.invoke(self, ((), context))

        def getParticleCloudDataAsync(self, context=None):
            return _M_ParticleCloudModule.ParticleCloud._op_getParticleCloudData.invokeAsync(self, ((), context))

        def begin_getParticleCloudData(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_ParticleCloudModule.ParticleCloud._op_getParticleCloudData.begin(self, ((), _response, _ex, _sent, context))

        def end_getParticleCloudData(self, _r):
            return _M_ParticleCloudModule.ParticleCloud._op_getParticleCloudData.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_ParticleCloudModule.ParticleCloudPrx.ice_checkedCast(proxy, '::ParticleCloudModule::ParticleCloud', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_ParticleCloudModule.ParticleCloudPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::ParticleCloudModule::ParticleCloud'
    _M_ParticleCloudModule._t_ParticleCloudPrx = IcePy.defineProxy('::ParticleCloudModule::ParticleCloud', ParticleCloudPrx)

    _M_ParticleCloudModule.ParticleCloudPrx = ParticleCloudPrx
    del ParticleCloudPrx

    _M_ParticleCloudModule.ParticleCloud = Ice.createTempClass()
    class ParticleCloud(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::ParticleCloudModule::ParticleCloud')

        def ice_id(self, current=None):
            return '::ParticleCloudModule::ParticleCloud'

        @staticmethod
        def ice_staticId():
            return '::ParticleCloudModule::ParticleCloud'

        def receiveParticleCloudData(self, data, current=None):
            raise NotImplementedError("servant method 'receiveParticleCloudData' not implemented")

        def getParticleCloudData(self, current=None):
            raise NotImplementedError("servant method 'getParticleCloudData' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_ParticleCloudModule._t_ParticleCloudDisp)

        __repr__ = __str__

    _M_ParticleCloudModule._t_ParticleCloudDisp = IcePy.defineClass('::ParticleCloudModule::ParticleCloud', ParticleCloud, (), None, ())
    ParticleCloud._ice_type = _M_ParticleCloudModule._t_ParticleCloudDisp

    ParticleCloud._op_receiveParticleCloudData = IcePy.Operation('receiveParticleCloudData', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_ParticleCloudModule._t_ParticleCloudData, False, 0),), (), None, ())
    ParticleCloud._op_getParticleCloudData = IcePy.Operation('getParticleCloudData', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_ParticleCloudModule._t_ParticleCloudData, False, 0), ())

    _M_ParticleCloudModule.ParticleCloud = ParticleCloud
    del ParticleCloud

# End of module ParticleCloudModule