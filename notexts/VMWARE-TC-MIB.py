#
# PySNMP MIB module VMWARE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-TC-MIB
# Produced by pysmi-1.1.8 at Wed Feb  2 18:08:18 2022
# On host fv-az121-846 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibIdentifier, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Bits, IpAddress, Counter32, Gauge32, ObjectIdentity, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Bits", "IpAddress", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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

mibBuilder.exportSymbols("VMWARE-TC-MIB", vmwTcMIB=vmwTcMIB, VmwCIMSeverity=VmwCIMSeverity, VmwConnectedState=VmwConnectedState, VmwSubsystemStatus=VmwSubsystemStatus, VmwCimName=VmwCimName, VmwCIMAlertTypes=VmwCIMAlertTypes, VmwUnixAbsFilePath=VmwUnixAbsFilePath, PYSNMP_MODULE_ID=vmwTcMIB, VmwLongSnmpAdminString=VmwLongSnmpAdminString, VmwCIMAlertFormat=VmwCIMAlertFormat, VmwSubsystemTypes=VmwSubsystemTypes, VmwLongDisplayString=VmwLongDisplayString)
