#
# PySNMP MIB module ERICSSON-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-ALARM-TC-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 09:42:05 2024
# On host fv-az566-8 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ericssonModules, = mibBuilder.importSymbols("ERICSSON-TOP-MIB", "ericssonModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, MibIdentifier, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, iso, Bits, IpAddress, Gauge32, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "MibIdentifier", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "iso", "Bits", "IpAddress", "Gauge32", "Counter32", "Unsigned32")
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

mibBuilder.exportSymbols("ERICSSON-ALARM-TC-MIB", ericssonAlarmTCMIB=ericssonAlarmTCMIB, EriAlarmSpecificProblem=EriAlarmSpecificProblem, EriAlarmIndex=EriAlarmIndex, PYSNMP_MODULE_ID=ericssonAlarmTCMIB, EriLargeAdditionalText=EriLargeAdditionalText, EriAdditionalInfo=EriAdditionalInfo, EriAlarmType=EriAlarmType, EriAlarmSequenceNumber=EriAlarmSequenceNumber, EriLargeAdditionalInfo=EriLargeAdditionalInfo, EriAlarmRecordType=EriAlarmRecordType, EriAdditionalText=EriAdditionalText)
