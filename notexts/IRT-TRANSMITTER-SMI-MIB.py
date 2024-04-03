#
# PySNMP MIB module IRT-TRANSMITTER-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rs/IRT-TRANSMITTER-SMI-MIB
# Produced by pysmi-1.1.11 at Wed Apr  3 14:03:44 2024
# On host fv-az1200-481 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, MibIdentifier, ModuleIdentity, NotificationType, ObjectIdentity, Integer32, enterprises, TimeTicks, Counter32, Gauge32, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "MibIdentifier", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Integer32", "enterprises", "TimeTicks", "Counter32", "Gauge32", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
irt = ModuleIdentity((1, 3, 6, 1, 4, 1, 19831))
irt.setRevisions(('2007-05-04 14:00', '2006-12-20 14:00', '2006-09-07 14:00',))
if mibBuilder.loadTexts: irt.setLastUpdated('200705041400Z')
if mibBuilder.loadTexts: irt.setOrganization('IRT for WORKING-GROUP-TC-MIB')
class SelectManualAuto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("manual", 1), ("automatic", 2))

class SelectOnOff(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("on", 1), ("off", 2))

class Input1Input2(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("input1", 1), ("input2", 2))

class OkNotOk(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("ok", 1), ("notok", 2))

class FaultOK(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("fault", 1), ("ok", 2))

class WarningOK(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("warning", 1), ("ok", 2))

class LocalRemote(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("local", 1), ("remote", 2))

class MuteOk(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("mute", 1), ("ok", 2))

class ReadyNotReady(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("ready", 1), ("notready", 2))

class ExecutedNotExecuted(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("executed", 1), ("notexecuted", 2))

class PresentNotPresent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("present", 1), ("notpresent", 2))

class SFNMFN(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("sfn", 1), ("mfn", 2))

broadcast = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1))
transmitter = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1))
dvbT = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1))
dab = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 2))
fm = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 3))
drm = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 4))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7))
mibBuilder.exportSymbols("IRT-TRANSMITTER-SMI-MIB", drm=drm, irt=irt, OkNotOk=OkNotOk, ExecutedNotExecuted=ExecutedNotExecuted, FaultOK=FaultOK, SelectOnOff=SelectOnOff, ReadyNotReady=ReadyNotReady, broadcast=broadcast, WarningOK=WarningOK, PresentNotPresent=PresentNotPresent, SelectManualAuto=SelectManualAuto, transmitter=transmitter, dvbT=dvbT, common=common, Input1Input2=Input1Input2, SFNMFN=SFNMFN, LocalRemote=LocalRemote, PYSNMP_MODULE_ID=irt, fm=fm, dab=dab, MuteOk=MuteOk)
