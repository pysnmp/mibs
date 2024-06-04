#
# PySNMP MIB module ERICSSON-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-TC-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 08:18:08 2024
# On host fv-az530-683 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ericssonModules, = mibBuilder.importSymbols("ERICSSON-TOP-MIB", "ericssonModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, Counter64, ObjectIdentity, Bits, NotificationType, MibIdentifier, Unsigned32, TimeTicks, iso, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Counter64", "ObjectIdentity", "Bits", "NotificationType", "MibIdentifier", "Unsigned32", "TimeTicks", "iso", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
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

mibBuilder.exportSymbols("ERICSSON-TC-MIB", PYSNMP_MODULE_ID=ericssonTCMIB, ericssonTCMIB=ericssonTCMIB, EriPath=EriPath, EriMO=EriMO)
