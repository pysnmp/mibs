#
# PySNMP MIB module TAIT-INFRA93-94SERIES-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-INFRA93-94SERIES-TC-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:28:07 2022
# On host fv-az206-808 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, Gauge32, iso, TimeTicks, ObjectIdentity, MibIdentifier, Bits, Counter64, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "Gauge32", "iso", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Bits", "Counter64", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
infra93_94MibModule, = mibBuilder.importSymbols("TAIT-INFRA93-94SERIES-COMMON-MIB", "infra93-94MibModule")
infra93_94TC = ModuleIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1, 10, 1)).setLabel("infra93-94TC")
infra93_94TC.setRevisions(('2018-08-31 00:00', '2018-05-22 00:26', '2017-11-28 00:00', '2017-07-28 00:00', '2016-03-21 00:00', '2015-05-15 12:00', '2014-10-30 15:00', '2014-01-14 11:00',))
if mibBuilder.loadTexts: infra93_94TC.setLastUpdated('201808310000Z')
if mibBuilder.loadTexts: infra93_94TC.setOrganization('www.taitradio.com')
class BaseStationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("offline", 0), ("online", 1), ("unknown", 2))

class Condition(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("bad", 0), ("good", 1), ("notFitted", 2))

class CurrentmA(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-3'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AlarmState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unavailable", 0), ("cleared", 1), ("raised", 2), ("disabled", 3))

class FrequencyHz(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-6'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class PowerW(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TransmitterStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("unconfigured", 1), ("untuned", 2), ("idle", 3), ("transmitting", 4), ("calibrating", 5), ("fault", 6))

class VoltageV(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32768, 32767)

class Milliseconds(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class ChannelGroupStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noLicense", 0), ("offline", 1), ("isolated", 2), ("satellite", 3), ("centralVoter", 4), ("singleBaseStation", 5), ("backupCentral", 6))

class TimingControlType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("fixed", 0), ("selfRegulating", 1))

class GateState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("closed", 0), ("open", 1))

class OptionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

mibBuilder.exportSymbols("TAIT-INFRA93-94SERIES-TC-MIB", PYSNMP_MODULE_ID=infra93_94TC, GateState=GateState, PowerW=PowerW, OptionState=OptionState, AlarmState=AlarmState, CurrentmA=CurrentmA, Condition=Condition, FrequencyHz=FrequencyHz, BaseStationMode=BaseStationMode, infra93_94TC=infra93_94TC, VoltageV=VoltageV, Milliseconds=Milliseconds, ChannelGroupStatus=ChannelGroupStatus, TimingControlType=TimingControlType, TransmitterStatus=TransmitterStatus)
