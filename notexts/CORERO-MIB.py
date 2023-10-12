#
# PySNMP MIB module CORERO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/corero/CORERO-MIB
# Produced by pysmi-1.1.8 at Thu Oct 12 08:13:57 2023
# On host fv-az585-225 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Integer32, Counter32, MibIdentifier, ObjectIdentity, TimeTicks, Unsigned32, IpAddress, iso, enterprises, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Integer32", "Counter32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Unsigned32", "IpAddress", "iso", "enterprises", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
corero = ModuleIdentity((1, 3, 6, 1, 4, 1, 41036))
corero.setRevisions(('2017-06-16 00:00', '2014-04-24 00:00',))
if mibBuilder.loadTexts: corero.setLastUpdated('201706160000Z')
if mibBuilder.loadTexts: corero.setOrganization('Corero Network Security')
coreroRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 41036, 1))
if mibBuilder.loadTexts: coreroRegistrations.setStatus('current')
coreroProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 41036, 2))
if mibBuilder.loadTexts: coreroProducts.setStatus('current')
mibBuilder.exportSymbols("CORERO-MIB", corero=corero, coreroRegistrations=coreroRegistrations, coreroProducts=coreroProducts, PYSNMP_MODULE_ID=corero)
