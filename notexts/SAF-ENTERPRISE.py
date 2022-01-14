#
# PySNMP MIB module SAF-ENTERPRISE (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saf/SAF-ENTERPRISE
# Produced by pysmi-1.1.8 at Fri Jan 14 00:00:27 2022
# On host fv-az74-435 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, enterprises, ModuleIdentity, ObjectIdentity, TimeTicks, Counter32, IpAddress, NotificationType, Gauge32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "enterprises", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Counter32", "IpAddress", "NotificationType", "Gauge32", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
saf = ModuleIdentity((1, 3, 6, 1, 4, 1, 7571))
saf.setRevisions(('2007-04-03 00:00',))
if mibBuilder.loadTexts: saf.setLastUpdated('201511120000Z')
if mibBuilder.loadTexts: saf.setOrganization('SAF Tehnika')
tehnika = ObjectIdentity((1, 3, 6, 1, 4, 1, 7571, 100))
if mibBuilder.loadTexts: tehnika.setStatus('current')
microwaveRadio = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1))
microwave = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 2))
pointToPoint = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1))
mibBuilder.exportSymbols("SAF-ENTERPRISE", microwaveRadio=microwaveRadio, PYSNMP_MODULE_ID=saf, saf=saf, pointToPoint=pointToPoint, tehnika=tehnika, microwave=microwave)
