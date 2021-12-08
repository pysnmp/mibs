#
# PySNMP MIB module CORERO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/corero/CORERO-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:18:34 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Integer32, Counter64, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, NotificationType, ObjectIdentity, enterprises, ModuleIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Counter64", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "NotificationType", "ObjectIdentity", "enterprises", "ModuleIdentity", "Unsigned32", "Bits", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
corero = ModuleIdentity((1, 3, 6, 1, 4, 1, 41036))
corero.setRevisions(('2017-06-16 00:00', '2014-04-24 00:00',))
if mibBuilder.loadTexts: corero.setLastUpdated('201706160000Z')
if mibBuilder.loadTexts: corero.setOrganization('Corero Network Security')
coreroRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 41036, 1))
if mibBuilder.loadTexts: coreroRegistrations.setStatus('current')
coreroProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 41036, 2))
if mibBuilder.loadTexts: coreroProducts.setStatus('current')
mibBuilder.exportSymbols("CORERO-MIB", coreroRegistrations=coreroRegistrations, coreroProducts=coreroProducts, PYSNMP_MODULE_ID=corero, corero=corero)
