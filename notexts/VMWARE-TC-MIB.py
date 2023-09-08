#
# PySNMP MIB module VMWARE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-TC-MIB
# Produced by pysmi-1.1.8 at Fri Sep  8 11:22:29 2023
# On host fv-az343-374 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Gauge32, ModuleIdentity, ObjectIdentity, Counter64, Counter32, NotificationType, IpAddress, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Counter64", "Counter32", "NotificationType", "IpAddress", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwSystem, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwSystem")
vmwTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 1, 11))
vmwTcMIB.setRevisions(('2009-09-05 00:00', '2007-12-27 00:00',))
if mibBuilder.loadTexts: vmwTcMIB.setLastUpdated('200909050000Z')
if mibBuilder.loadTexts: vmwTcMIB.setOrganization('VMware, Inc')
class VmwSubsystemTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("unknown", 1), ("chassis", 2), ("powerSupply", 3), ("fan", 4), ("cpu", 5), ("memory", 6), ("battery", 7), ("temperatureSensor", 8), ("raidController", 9), ("voltage", 10))

class VmwCIMAlertTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("communications", 2), ("qos", 3), ("processingError", 4), ("deviceAlert", 5), ("environmentalAlert", 6), ("modelChange", 7), ("securityAlert", 8))

class VmwCIMAlertFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("other", 1), ("cimObjectPath", 2))

class VmwSubsystemStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("normal", 2), ("marginal", 3), ("critical", 4), ("failed", 5))

class VmwCIMSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 0), ("other", 1), ("information", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6), ("fatal", 7))

class VmwCimName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class VmwConnectedState(TextualConvention, OctetString):
    status = 'current'
    displayHint = '7a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 7)

class VmwLongDisplayString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a'

class VmwLongSnmpAdminString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4096t'

class VmwUnixAbsFilePath(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

mibBuilder.exportSymbols("VMWARE-TC-MIB", VmwCIMAlertTypes=VmwCIMAlertTypes, VmwUnixAbsFilePath=VmwUnixAbsFilePath, VmwLongDisplayString=VmwLongDisplayString, VmwCIMSeverity=VmwCIMSeverity, VmwSubsystemStatus=VmwSubsystemStatus, VmwCimName=VmwCimName, vmwTcMIB=vmwTcMIB, VmwSubsystemTypes=VmwSubsystemTypes, VmwLongSnmpAdminString=VmwLongSnmpAdminString, VmwCIMAlertFormat=VmwCIMAlertFormat, PYSNMP_MODULE_ID=vmwTcMIB, VmwConnectedState=VmwConnectedState)
