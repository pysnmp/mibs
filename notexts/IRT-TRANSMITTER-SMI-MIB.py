#
# PySNMP MIB module IRT-TRANSMITTER-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rs/IRT-TRANSMITTER-SMI-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 17:10:52 2021
# On host fv-az33-471 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, enterprises, Unsigned32, Counter32, NotificationType, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Bits, IpAddress, MibIdentifier, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "enterprises", "Unsigned32", "Counter32", "NotificationType", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Bits", "IpAddress", "MibIdentifier", "iso", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("IRT-TRANSMITTER-SMI-MIB", dab=dab, LocalRemote=LocalRemote, PresentNotPresent=PresentNotPresent, common=common, dvbT=dvbT, fm=fm, irt=irt, drm=drm, MuteOk=MuteOk, ExecutedNotExecuted=ExecutedNotExecuted, FaultOK=FaultOK, Input1Input2=Input1Input2, ReadyNotReady=ReadyNotReady, OkNotOk=OkNotOk, SFNMFN=SFNMFN, SelectOnOff=SelectOnOff, SelectManualAuto=SelectManualAuto, PYSNMP_MODULE_ID=irt, WarningOK=WarningOK, transmitter=transmitter, broadcast=broadcast)
