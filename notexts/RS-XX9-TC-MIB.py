#
# PySNMP MIB module RS-XX9-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source RS-XX9-TC-MIB
# Source digest sha256:386aba1bfab8ee739feb80061fb4b4ee9c67e50bc922ba11ccbf87738e422c62
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
rsXx9MibModule, = mibBuilder.importSymbols("RS-XX9-SMI-MIB", "rsXx9MibModule")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rsXx9TcMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2566, 149, 1, 216, 1))
rsXx9TcMibModule.setRevisions(('2016-01-22 14:00', '2015-09-24 08:00', '2015-05-21 12:00', '2013-02-15 11:11', '2012-05-09 10:00', '2011-08-16 08:00',))
if mibBuilder.loadTexts: rsXx9TcMibModule.setLastUpdated('2016-01-22 14:00')
if mibBuilder.loadTexts: rsXx9TcMibModule.setOrganization('Rohde&Schwarz GmbH & Co. KG')
class EnableOption(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unconfigured", 1), ("disabled", 2), ("enabled", 3))

class IndexAB(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("a", 1), ("b", 2))

class IndexProgram(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 1000))
    namedValues = NamedValues(("program1", 1), ("program2", 2), ("program3", 3), ("program4", 4), ("program5", 5), ("program6", 6), ("program7", 7), ("program8", 8), ("programRes", 1000))

class IndexTransmitter(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 1000))
    namedValues = NamedValues(("transmitterA1", 1), ("transmitterA2", 2), ("transmitterA3", 3), ("transmitterA4", 4), ("transmitterA5", 5), ("transmitterA6", 6), ("transmitterA7", 7), ("transmitterA8", 8), ("transmitterB", 1000))

class NotificationClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("fault", 1), ("warning", 2), ("info", 3))

class NotificationMask(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class NotificationPriority(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class NotificationState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 1), ("off", 2), ("fault", 3), ("warning", 4), ("ok", 5))

class SwitchOnOff(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class Trigger(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("idle", 1), ("trigger", 2))

class Xx9AmplifierType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 21))
    namedValues = NamedValues(("unconfigured", 1), ("phu901", 2), ("pmu901", 3), ("phu902", 4), ("phv902", 5), ("pmv901", 6), ("pmu905", 7), ("phu903", 8), ("phr901", 21))

class Xx9ModulationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 21, 22, 23))
    namedValues = NamedValues(("unconfigured", 1), ("none", 2), ("dvbT2", 3), ("dvbT", 4), ("isdbT", 5), ("atsc", 6), ("atv", 7), ("dab", 8), ("dtmb", 9), ("fm", 21), ("hdRadioHybrid", 22), ("hdRadioFullDigital", 23))

class Xx9RedundancyMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("undefined", 1), ("singleDrive", 2), ("dualDrive", 3), ("backupDrive", 4), ("activePa", 5), ("backupTx", 6))

class Xx9SystemType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unconfigured", 1), ("transmitter", 2), ("multiTx", 3), ("nPlus1", 4))

mibBuilder.exportSymbols("RS-XX9-TC-MIB", EnableOption=EnableOption, IndexAB=IndexAB, IndexProgram=IndexProgram, IndexTransmitter=IndexTransmitter, NotificationClass=NotificationClass, NotificationMask=NotificationMask, NotificationPriority=NotificationPriority, NotificationState=NotificationState, PYSNMP_MODULE_ID=rsXx9TcMibModule, SwitchOnOff=SwitchOnOff, Trigger=Trigger, Xx9AmplifierType=Xx9AmplifierType, Xx9ModulationMode=Xx9ModulationMode, Xx9RedundancyMode=Xx9RedundancyMode, Xx9SystemType=Xx9SystemType, rsXx9TcMibModule=rsXx9TcMibModule)
