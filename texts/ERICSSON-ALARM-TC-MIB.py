#
# PySNMP MIB module ERICSSON-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-ALARM-TC-MIB
# Produced by pysmi-1.1.11 at Wed Apr  3 14:50:45 2024
# On host fv-az1198-695 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ericssonModules, = mibBuilder.importSymbols("ERICSSON-TOP-MIB", "ericssonModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, MibIdentifier, IpAddress, Gauge32, ModuleIdentity, NotificationType, Unsigned32, TimeTicks, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "MibIdentifier", "IpAddress", "Gauge32", "ModuleIdentity", "NotificationType", "Unsigned32", "TimeTicks", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ericssonAlarmTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 183, 3))
ericssonAlarmTCMIB.setRevisions(('2017-03-31 00:00', '2016-06-24 00:00', '2008-10-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ericssonAlarmTCMIB.setRevisionsDescriptions(('Updated as part of ERICSSON ALARM MIB 2.1 package.', 'Updated as part of ERICSSON ALARM MIB 2.0 package.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ericssonAlarmTCMIB.setLastUpdated('201703310000Z')
if mibBuilder.loadTexts: ericssonAlarmTCMIB.setOrganization('Ericsson AB')
if mibBuilder.loadTexts: ericssonAlarmTCMIB.setContactInfo('Email: <snmp.mib.contact@ericsson.com> ')
if mibBuilder.loadTexts: ericssonAlarmTCMIB.setDescription('This MIB defines textual conventions used by the\r\n                ERICSSON-ALARM-MIB.\r\n                \r\n                                Document number: 3/196 03-CXC 172 7549')
class EriAlarmType(TextualConvention, Unsigned32):
    description = 'A unique identification of the fault, not\r\n                including the managed object.  Alarm types are\r\n                used to identify if alarms indicate the same\r\n                problem or not, for lookup into external alarm\r\n                documentation, etc.  A unique alarm type is\r\n                identified using the combination of two instances\r\n                of EriAlarmType. Different managed object\r\n                types and instances can share alarm types.  But\r\n                if the same managed object reports the same alarm\r\n                type, it is to be considered to be the same alarm\r\n                state. The alarm type is a simplification of the\r\n                different X.733 and 3GPP alarm IRP alarm\r\n                correlation mechanisms based on EventType,\r\n                ProbableCause, SpecificProblem and\r\n                NotificationId.'
    status = 'current'
    displayHint = 'd'

class EriAlarmIndex(TextualConvention, Unsigned32):
    description = 'Index used in the active alarm table.  A row\r\n                shall never change its index during the lifetime\r\n                of the entry; for example renumbering entries is\r\n                not allowed when entries are deleted.\r\n                Renumbering after an agent restart is allowed.\r\n                Note that this index shall not be used to\r\n                identify alarms when performing\r\n                resynchronization, etc. The logical identity for\r\n                an alarm instance is the managed object and alarm\r\n                type.'
    status = 'current'
    displayHint = 'd'

class EriAdditionalText(TextualConvention, OctetString):
    reference = 'snmpFrameworkMIB in RFC 3411 defines\r\n                SnmpAdminString'
    description = 'The string used in additional text\r\n                notifications. This MUST contain enough\r\n                information for an operator to be able to\r\n                understand the problem. If this string contains\r\n                structure, this format should be clearly\r\n                documented for programs to be able to parse that\r\n                information. This is a small size range in order\r\n                to guarantee delivery of notifications without\r\n                fragmentation. There is a corresponding textual\r\n                convention, EriLargeAdditionalText, to be used\r\n                for scalar and columnar objects.  The string\r\n                should adhere to the rules for SnmpAdminString of\r\n                SNMPv3 framework MIBs.'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 256)

class EriLargeAdditionalText(TextualConvention, OctetString):
    reference = 'snmpFrameworkMIB in RFC 3411 defines\r\n                SnmpAdminString'
    description = 'The string used in additional text. This MUST\r\n                contain enough information for an operator to be\r\n                able to understand the problem. If this string\r\n                contains structure, this format should be clearly\r\n                documented for programs to be able to parse that\r\n                information. This is a large additional text to\r\n                be used in tables. There is a corresponding\r\n                textual convention to be used in alarm\r\n                notifications, EriAdditionalText.  The string\r\n                should adhere to the rules for SnmpAdminString of\r\n                SNMPv3 framework MIBs.'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 512)

class EriAlarmSpecificProblem(TextualConvention, OctetString):
    description = 'Unique string for the Alarm Type. No different\r\n                alarm types may share specific problem. Specific\r\n                Problem and Alarm Type have a one-to-one\r\n                correspondance.'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 64)

class EriAlarmSequenceNumber(TextualConvention, Unsigned32):
    description = 'This is a monotonically increasing counter. It\r\n                is increased every time a notification is sent.\r\n                The value is NOT increased for heartbeat\r\n                notifications.  It is carried as a varbind in the\r\n                alarm notifications as well as in the heartbeat\r\n                notifications.  Management systems can use these\r\n                varbinds to detect lost notifications.'
    status = 'current'
    displayHint = 'd'

class EriAdditionalInfo(TextualConvention, OctetString):
    reference = 'snmpFrameworkMIB in RFC 3411 defines\r\n                SnmpAdminString;\r\n                TEA (The Ericsson Architecture),\r\n                Operation & Maintenance Architecture Principles, FAE 151 01.'
    description = "Additional Information, structured in a way that is \r\n                                suitable for machine-to-machine communication. \r\n                                Comprises a number of name=value pairs, separated by a \r\n                                semicolon in the following format:\r\n                                        name1=value1;name2=value2;..\r\n                                Allowed strings for use as 'name' are defined in \r\n                                The Ericsson Architecture and updated upon internal \r\n                                requests from Ericsson organizations. \r\n                                This is a small size range in order to guarantee delivery \r\n                of notifications without fragmentation. There is a \r\n                corresponding textual convention, EriLargeAdditionalInfo,\r\n                to be used for scalar and columnar objects.\r\n                The string should adhere to the rules for SnmpAdminString\r\n                                of SNMPv3 framework MIBs."
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 256)

class EriLargeAdditionalInfo(TextualConvention, OctetString):
    reference = 'snmpFrameworkMIB in RFC 3411 defines\r\n                SnmpAdminString;\r\n                TEA (The Ericsson Architecture),\r\n                Operation & Maintenance Architecture Principles, FAE 151 01.'
    description = "Additional Information, structured in a way that is \r\n                                suitable for machine-to-machine communication. \r\n                                Comprises a number of name=value pairs, separated by a \r\n                                semicolon in the following format:\r\n                                        name1=value1;name2=value2;..\r\n                                Allowed strings for use as 'name' are defined in \r\n                                The Ericsson Architecture and updated upon internal \r\n                                requests from Ericsson organizations. \r\n                                This is a large additional info to be used in tables. \r\n                                There is a corresponding textual convention to be used \r\n                                in alarm notifications, EriAdditionalInfo.  \r\n                                The string should adhere to the rules for SnmpAdminString \r\n                                of SNMPv3 framework MIBs."
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 512)

class EriAlarmRecordType(TextualConvention, Integer32):
    description = 'This defines the alarm record type that is\r\n                being reported in an alarm notification.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("alarmNew", 0), ("alarmChange", 1))

mibBuilder.exportSymbols("ERICSSON-ALARM-TC-MIB", EriAlarmRecordType=EriAlarmRecordType, PYSNMP_MODULE_ID=ericssonAlarmTCMIB, EriAdditionalText=EriAdditionalText, EriLargeAdditionalText=EriLargeAdditionalText, EriAlarmIndex=EriAlarmIndex, EriAlarmSpecificProblem=EriAlarmSpecificProblem, EriAlarmType=EriAlarmType, EriAlarmSequenceNumber=EriAlarmSequenceNumber, EriAdditionalInfo=EriAdditionalInfo, EriLargeAdditionalInfo=EriLargeAdditionalInfo, ericssonAlarmTCMIB=ericssonAlarmTCMIB)
