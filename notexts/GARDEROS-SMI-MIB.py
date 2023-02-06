#
# PySNMP MIB module GARDEROS-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/garderos/GARDEROS-SMI-MIB
# Produced by pysmi-1.1.8 at Mon Feb  6 15:00:48 2023
# On host fv-az357-935 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Counter32, MibIdentifier, NotificationType, iso, ModuleIdentity, enterprises, Bits, Integer32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Counter32", "MibIdentifier", "NotificationType", "iso", "ModuleIdentity", "enterprises", "Bits", "Integer32", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
garderos = ModuleIdentity((1, 3, 6, 1, 4, 1, 16108))
garderos.setRevisions(('2016-02-02 16:12',))
if mibBuilder.loadTexts: garderos.setLastUpdated('201602021612Z')
if mibBuilder.loadTexts: garderos.setOrganization('Garderos GmbH')
mibBuilder.exportSymbols("GARDEROS-SMI-MIB", PYSNMP_MODULE_ID=garderos, garderos=garderos)
