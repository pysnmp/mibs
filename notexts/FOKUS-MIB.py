#
# PySNMP MIB module FOKUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/FOKUS-MIB
# Produced by pysmi-1.1.8 at Mon Sep 19 08:36:05 2022
# On host fv-az278-268 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, ModuleIdentity, ObjectIdentity, iso, Gauge32, IpAddress, enterprises, MibIdentifier, NotificationType, Counter64, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "iso", "Gauge32", "IpAddress", "enterprises", "MibIdentifier", "NotificationType", "Counter64", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fokus = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325))
if mibBuilder.loadTexts: fokus.setLastUpdated('200202050000Z')
if mibBuilder.loadTexts: fokus.setOrganization('Fraunhofer FOKUS, CATS')
mibBuilder.exportSymbols("FOKUS-MIB", fokus=fokus, PYSNMP_MODULE_ID=fokus)
