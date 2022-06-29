#
# PySNMP MIB module SAF-ENTERPRISE (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saf/SAF-ENTERPRISE
# Produced by pysmi-1.1.8 at Wed Jun 29 13:42:03 2022
# On host fv-az128-12 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, iso, NotificationType, Unsigned32, Counter64, Gauge32, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, enterprises, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "iso", "NotificationType", "Unsigned32", "Counter64", "Gauge32", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "enterprises", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
saf = ModuleIdentity((1, 3, 6, 1, 4, 1, 7571))
saf.setRevisions(('2007-04-03 00:00',))
if mibBuilder.loadTexts: saf.setLastUpdated('201511120000Z')
if mibBuilder.loadTexts: saf.setOrganization('SAF Tehnika')
tehnika = ObjectIdentity((1, 3, 6, 1, 4, 1, 7571, 100))
if mibBuilder.loadTexts: tehnika.setStatus('current')
microwaveRadio = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1))
microwave = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 2))
pointToPoint = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1))
mibBuilder.exportSymbols("SAF-ENTERPRISE", microwave=microwave, pointToPoint=pointToPoint, saf=saf, microwaveRadio=microwaveRadio, tehnika=tehnika, PYSNMP_MODULE_ID=saf)
