#
# PySNMP MIB module ERICSSON-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-TC-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 09:19:18 2024
# On host fv-az735-465 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ericssonModules, = mibBuilder.importSymbols("ERICSSON-TOP-MIB", "ericssonModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, NotificationType, Unsigned32, IpAddress, MibIdentifier, Counter64, iso, Integer32, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "NotificationType", "Unsigned32", "IpAddress", "MibIdentifier", "Counter64", "iso", "Integer32", "TimeTicks", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ericssonTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 183, 1))
ericssonTCMIB.setRevisions(('2017-04-13 00:00', '2016-06-24 00:00', '2008-10-17 00:00',))
if mibBuilder.loadTexts: ericssonTCMIB.setLastUpdated('201704130000Z')
if mibBuilder.loadTexts: ericssonTCMIB.setOrganization('Ericsson AB')
class EriMO(TextualConvention, OctetString):
    reference = '3GPP TS 32.106-8 V3.2, Name convention for Managed Objects'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 150)

class EriPath(TextualConvention, OctetString):
    reference = 'YANG module ericsson-yang-types; RFC 7950 , The YANG 1.1 Data Modeling Language'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 150)

mibBuilder.exportSymbols("ERICSSON-TC-MIB", EriMO=EriMO, EriPath=EriPath, ericssonTCMIB=ericssonTCMIB, PYSNMP_MODULE_ID=ericssonTCMIB)
