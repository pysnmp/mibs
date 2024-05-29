#
# PySNMP MIB module ERICSSON-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-ALARM-TC-MIB
# Produced by pysmi-1.1.12 at Wed May 29 10:55:17 2024
# On host fv-az1200-312 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ericssonModules, = mibBuilder.importSymbols("ERICSSON-TOP-MIB", "ericssonModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, IpAddress, TimeTicks, Bits, ObjectIdentity, Integer32, ModuleIdentity, Counter64, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "TimeTicks", "Bits", "ObjectIdentity", "Integer32", "ModuleIdentity", "Counter64", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("ERICSSON-ALARM-TC-MIB", ericssonAlarmTCMIB=ericssonAlarmTCMIB, EriAlarmRecordType=EriAlarmRecordType, EriAlarmIndex=EriAlarmIndex, EriAlarmType=EriAlarmType, PYSNMP_MODULE_ID=ericssonAlarmTCMIB, EriAdditionalText=EriAdditionalText, EriLargeAdditionalText=EriLargeAdditionalText, EriAdditionalInfo=EriAdditionalInfo, EriAlarmSpecificProblem=EriAlarmSpecificProblem, EriLargeAdditionalInfo=EriLargeAdditionalInfo, EriAlarmSequenceNumber=EriAlarmSequenceNumber)
