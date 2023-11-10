#
# PySNMP MIB module GARDEROS-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/garderos/GARDEROS-SMI-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 08:44:11 2023
# On host fv-az566-171 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, TimeTicks, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, Integer32, IpAddress, Counter32, Bits, NotificationType, Counter64, iso, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "Integer32", "IpAddress", "Counter32", "Bits", "NotificationType", "Counter64", "iso", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
garderos = ModuleIdentity((1, 3, 6, 1, 4, 1, 16108))
garderos.setRevisions(('2016-02-02 16:12',))
if mibBuilder.loadTexts: garderos.setLastUpdated('201602021612Z')
if mibBuilder.loadTexts: garderos.setOrganization('Garderos GmbH')
mibBuilder.exportSymbols("GARDEROS-SMI-MIB", PYSNMP_MODULE_ID=garderos, garderos=garderos)
