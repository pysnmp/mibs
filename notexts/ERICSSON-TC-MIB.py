#
# PySNMP MIB module ERICSSON-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-TC-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 08:45:06 2023
# On host fv-az447-590 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ericssonModules, = mibBuilder.importSymbols("ERICSSON-TOP-MIB", "ericssonModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Integer32, TimeTicks, MibIdentifier, NotificationType, Counter64, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Integer32", "TimeTicks", "MibIdentifier", "NotificationType", "Counter64", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("ERICSSON-TC-MIB", EriPath=EriPath, EriMO=EriMO, PYSNMP_MODULE_ID=ericssonTCMIB, ericssonTCMIB=ericssonTCMIB)
