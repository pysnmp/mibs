#
# PySNMP MIB module GARDEROS-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/garderos/GARDEROS-SMI-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 12:23:33 2024
# On host fv-az1530-743 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, Bits, Counter64, NotificationType, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, ModuleIdentity, MibIdentifier, TimeTicks, enterprises, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Bits", "Counter64", "NotificationType", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "enterprises", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
garderos = ModuleIdentity((1, 3, 6, 1, 4, 1, 16108))
garderos.setRevisions(('2016-02-02 16:12',))
if mibBuilder.loadTexts: garderos.setLastUpdated('201602021612Z')
if mibBuilder.loadTexts: garderos.setOrganization('Garderos GmbH')
mibBuilder.exportSymbols("GARDEROS-SMI-MIB", PYSNMP_MODULE_ID=garderos, garderos=garderos)
