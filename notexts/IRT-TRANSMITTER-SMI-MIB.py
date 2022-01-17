#
# PySNMP MIB module IRT-TRANSMITTER-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rs/IRT-TRANSMITTER-SMI-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 18:53:33 2022
# On host fv-az33-58 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Unsigned32, Integer32, iso, Gauge32, ObjectIdentity, MibIdentifier, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, ModuleIdentity, Counter64, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Integer32", "iso", "Gauge32", "ObjectIdentity", "MibIdentifier", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "ModuleIdentity", "Counter64", "NotificationType", "Bits")
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
mibBuilder.exportSymbols("IRT-TRANSMITTER-SMI-MIB", OkNotOk=OkNotOk, drm=drm, FaultOK=FaultOK, PYSNMP_MODULE_ID=irt, dab=dab, SelectOnOff=SelectOnOff, ExecutedNotExecuted=ExecutedNotExecuted, MuteOk=MuteOk, PresentNotPresent=PresentNotPresent, fm=fm, irt=irt, common=common, LocalRemote=LocalRemote, WarningOK=WarningOK, dvbT=dvbT, SFNMFN=SFNMFN, Input1Input2=Input1Input2, ReadyNotReady=ReadyNotReady, broadcast=broadcast, SelectManualAuto=SelectManualAuto, transmitter=transmitter)
