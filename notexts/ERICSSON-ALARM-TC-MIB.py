#
# PySNMP MIB module ERICSSON-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-ALARM-TC-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 10:11:34 2023
# On host fv-az732-878 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ericssonModules, = mibBuilder.importSymbols("ERICSSON-TOP-MIB", "ericssonModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, MibIdentifier, TimeTicks, iso, Bits, Integer32, Counter32, IpAddress, Gauge32, Counter64, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "MibIdentifier", "TimeTicks", "iso", "Bits", "Integer32", "Counter32", "IpAddress", "Gauge32", "Counter64", "ModuleIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ericssonAlarmTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 183, 3))
ericssonAlarmTCMIB.setRevisions(('2017-03-31 00:00', '2016-06-24 00:00', '2008-10-17 00:00',))
if mibBuilder.loadTexts: ericssonAlarmTCMIB.setLastUpdated('201703310000Z')
if mibBuilder.loadTexts: ericssonAlarmTCMIB.setOrganization('Ericsson AB')
class EriAlarmType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class EriAlarmIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class EriAdditionalText(TextualConvention, OctetString):
    reference = 'snmpFrameworkMIB in RFC 3411 defines SnmpAdminString'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 256)

class EriLargeAdditionalText(TextualConvention, OctetString):
    reference = 'snmpFrameworkMIB in RFC 3411 defines SnmpAdminString'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 512)

class EriAlarmSpecificProblem(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 64)

class EriAlarmSequenceNumber(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class EriAdditionalInfo(TextualConvention, OctetString):
    reference = 'snmpFrameworkMIB in RFC 3411 defines SnmpAdminString; TEA (The Ericsson Architecture), Operation & Maintenance Architecture Principles, FAE 151 01.'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 256)

class EriLargeAdditionalInfo(TextualConvention, OctetString):
    reference = 'snmpFrameworkMIB in RFC 3411 defines SnmpAdminString; TEA (The Ericsson Architecture), Operation & Maintenance Architecture Principles, FAE 151 01.'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 512)

class EriAlarmRecordType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("alarmNew", 0), ("alarmChange", 1))

mibBuilder.exportSymbols("ERICSSON-ALARM-TC-MIB", EriAlarmSpecificProblem=EriAlarmSpecificProblem, PYSNMP_MODULE_ID=ericssonAlarmTCMIB, EriLargeAdditionalText=EriLargeAdditionalText, EriAlarmIndex=EriAlarmIndex, EriAlarmSequenceNumber=EriAlarmSequenceNumber, EriAdditionalInfo=EriAdditionalInfo, EriAlarmRecordType=EriAlarmRecordType, EriAdditionalText=EriAdditionalText, EriLargeAdditionalInfo=EriLargeAdditionalInfo, EriAlarmType=EriAlarmType, ericssonAlarmTCMIB=ericssonAlarmTCMIB)
