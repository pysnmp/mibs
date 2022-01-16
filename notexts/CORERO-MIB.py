#
# PySNMP MIB module CORERO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/corero/CORERO-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:56:35 2022
# On host fv-az74-933 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, iso, enterprises, MibIdentifier, Gauge32, Counter32, Bits, TimeTicks, ModuleIdentity, ObjectIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "iso", "enterprises", "MibIdentifier", "Gauge32", "Counter32", "Bits", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
corero = ModuleIdentity((1, 3, 6, 1, 4, 1, 41036))
corero.setRevisions(('2017-06-16 00:00', '2014-04-24 00:00',))
if mibBuilder.loadTexts: corero.setLastUpdated('201706160000Z')
if mibBuilder.loadTexts: corero.setOrganization('Corero Network Security')
coreroRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 41036, 1))
if mibBuilder.loadTexts: coreroRegistrations.setStatus('current')
coreroProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 41036, 2))
if mibBuilder.loadTexts: coreroProducts.setStatus('current')
mibBuilder.exportSymbols("CORERO-MIB", corero=corero, coreroRegistrations=coreroRegistrations, PYSNMP_MODULE_ID=corero, coreroProducts=coreroProducts)
