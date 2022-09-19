#
# PySNMP MIB module SAF-ENTERPRISE (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saf/SAF-ENTERPRISE
# Produced by pysmi-1.1.8 at Mon Sep 19 08:35:41 2022
# On host fv-az152-47 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, enterprises, Counter64, Integer32, Bits, iso, Unsigned32, NotificationType, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "enterprises", "Counter64", "Integer32", "Bits", "iso", "Unsigned32", "NotificationType", "Gauge32", "Counter32")
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
mibBuilder.exportSymbols("SAF-ENTERPRISE", microwaveRadio=microwaveRadio, pointToPoint=pointToPoint, microwave=microwave, PYSNMP_MODULE_ID=saf, tehnika=tehnika, saf=saf)
