#
# PySNMP MIB module ERICSSON-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-TC-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 13:31:17 2024
# On host fv-az975-559 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ericssonModules, = mibBuilder.importSymbols("ERICSSON-TOP-MIB", "ericssonModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, Counter64, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, MibIdentifier, ObjectIdentity, TimeTicks, ModuleIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Counter64", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "MibIdentifier", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ericssonTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 183, 1))
ericssonTCMIB.setRevisions(('2017-04-13 00:00', '2016-06-24 00:00', '2008-10-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ericssonTCMIB.setRevisionsDescriptions(('Updated as part of ERICSSON ALARM MIB 2.1 package.', 'Updated version of this MIB module. Included XPath\r\n\t\t\t\tinstance identifier.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ericssonTCMIB.setLastUpdated('201704130000Z')
if mibBuilder.loadTexts: ericssonTCMIB.setOrganization('Ericsson AB')
if mibBuilder.loadTexts: ericssonTCMIB.setContactInfo('Email: Enda.Murphy@ericsson.com ')
if mibBuilder.loadTexts: ericssonTCMIB.setDescription('This MIB document includes textual conventions\r\n                that can be used by all of the Ericsson group.\r\n                The intention is to have shared definitions such\r\n                that integration and SNMP development are made\r\n                easier.\r\n\t\t\t\tDocument number: 2/196 03-CXC 172 7549.')
class EriMO(TextualConvention, OctetString):
    reference = '3GPP TS 32.106-8 V3.2, Name convention for\r\n                Managed Objects'
    description = "The 3GPP naming convention shall be used as the\r\n                format for the managed object parameter.  Note\r\n                that the granularity MUST be sufficient to\r\n                guarantee unique alarm states and relevant\r\n                resource identification to the operator.\r\n\t\t\t\tNOTE: The DN should be *relative* to the Managed\r\n\t\t\t\tElement's *own* root."
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 150)

class EriPath(TextualConvention, OctetString):
    reference = 'YANG module ericsson-yang-types;\r\n\t\t\t\tRFC 7950 , The YANG 1.1 Data Modeling Language'
    description = "An Abridged YANG Instance-Identifier that references a\r\n\t\t\t\tresource within the Managed Element. Prefixes used MUST\r\n\t\t\t\tbe the ones defined in the YANG module statement's prefix\r\n\t\t\t\tsubstatement. A prefix SHALL be omitted if it is the same\r\n\t\t\t\tas the previous prefix on the ancestor axis.\r\n\t\t\t\tFor example:\r\n\t\t\t\t/ex:system/server[ip='192.0.2.1'][port='80']\r\n\t\t\t\tSee: YANG module ericsson-yang-types.\r\n\t\t\t\tSee also: RFC 7950 Section 9.13.\r\n\t\t\t\tNOTE: The granularity must be good enough to guarantee\r\n\t\t\t\tunique alarm states and relevant resource identification\r\n\t\t\t\tto the operator."
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 150)

mibBuilder.exportSymbols("ERICSSON-TC-MIB", EriMO=EriMO, PYSNMP_MODULE_ID=ericssonTCMIB, ericssonTCMIB=ericssonTCMIB, EriPath=EriPath)
