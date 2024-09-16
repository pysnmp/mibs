#
# PySNMP MIB module BARRACUDA-REF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/barracuda/BARRACUDA-REF-MIB
# Produced by pysmi-1.1.12 at Mon Sep 16 14:51:54 2024
# On host fv-az1272-448 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, iso, Integer32, MibIdentifier, IpAddress, enterprises, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, ModuleIdentity, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "iso", "Integer32", "MibIdentifier", "IpAddress", "enterprises", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Counter64", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
barracuda = ModuleIdentity((1, 3, 6, 1, 4, 1, 20632))
if mibBuilder.loadTexts: barracuda.setLastUpdated('200906100000Z')
if mibBuilder.loadTexts: barracuda.setOrganization('Barracuda Networks, Inc.')
mibBuilder.exportSymbols("BARRACUDA-REF", PYSNMP_MODULE_ID=barracuda, barracuda=barracuda)
