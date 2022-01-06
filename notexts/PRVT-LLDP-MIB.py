#
# PySNMP MIB module PRVT-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-LLDP-MIB
# Produced by pysmi-1.1.8 at Thu Jan  6 20:31:37 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, Integer32, iso, ModuleIdentity, Gauge32, ObjectIdentity, Unsigned32, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Integer32", "iso", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "TimeTicks")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
prvtLldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 145))
prvtLldpMIB.setRevisions(('2009-07-28 00:00',))
if mibBuilder.loadTexts: prvtLldpMIB.setLastUpdated('200907280000Z')
if mibBuilder.loadTexts: prvtLldpMIB.setOrganization('BATM Advanced Communication')
prvtLldpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 145, 0))
prvtLldpEnable = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 145, 0, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLldpEnable.setStatus('current')
mibBuilder.exportSymbols("PRVT-LLDP-MIB", prvtLldpMIB=prvtLldpMIB, prvtLldpObjects=prvtLldpObjects, prvtLldpEnable=prvtLldpEnable, PYSNMP_MODULE_ID=prvtLldpMIB)
