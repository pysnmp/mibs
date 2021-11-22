#
# PySNMP MIB module PRVT-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-LLDP-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:39:00 2021
# On host fv-az83-627 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ObjectIdentity, MibIdentifier, ModuleIdentity, Unsigned32, Counter32, NotificationType, IpAddress, TimeTicks, iso, Bits, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Counter32", "NotificationType", "IpAddress", "TimeTicks", "iso", "Bits", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
prvtLldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 145))
prvtLldpMIB.setRevisions(('2009-07-28 00:00',))
if mibBuilder.loadTexts: prvtLldpMIB.setLastUpdated('200907280000Z')
if mibBuilder.loadTexts: prvtLldpMIB.setOrganization('BATM Advanced Communication')
prvtLldpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 145, 0))
prvtLldpEnable = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 145, 0, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLldpEnable.setStatus('current')
mibBuilder.exportSymbols("PRVT-LLDP-MIB", PYSNMP_MODULE_ID=prvtLldpMIB, prvtLldpEnable=prvtLldpEnable, prvtLldpObjects=prvtLldpObjects, prvtLldpMIB=prvtLldpMIB)
