#
# PySNMP MIB module ERICSSON-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-ALARM-TC-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 13:28:38 2024
# On host fv-az883-167 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ericssonModules, = mibBuilder.importSymbols("ERICSSON-TOP-MIB", "ericssonModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Integer32, iso, TimeTicks, IpAddress, MibIdentifier, Counter64, NotificationType, ObjectIdentity, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Integer32", "iso", "TimeTicks", "IpAddress", "MibIdentifier", "Counter64", "NotificationType", "ObjectIdentity", "Gauge32", "Bits")
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

mibBuilder.exportSymbols("ERICSSON-ALARM-TC-MIB", EriAlarmType=EriAlarmType, EriAlarmSequenceNumber=EriAlarmSequenceNumber, EriLargeAdditionalInfo=EriLargeAdditionalInfo, EriAlarmRecordType=EriAlarmRecordType, PYSNMP_MODULE_ID=ericssonAlarmTCMIB, EriAdditionalText=EriAdditionalText, EriAlarmSpecificProblem=EriAlarmSpecificProblem, EriAdditionalInfo=EriAdditionalInfo, EriLargeAdditionalText=EriLargeAdditionalText, EriAlarmIndex=EriAlarmIndex, ericssonAlarmTCMIB=ericssonAlarmTCMIB)
