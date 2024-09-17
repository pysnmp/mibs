#
# PySNMP MIB module RITTAL-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rittal/RITTAL-SMI
# Produced by pysmi-1.1.12 at Tue Sep 17 13:01:57 2024
# On host fv-az1215-438 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, IpAddress, Bits, NotificationType, ObjectIdentity, TimeTicks, Integer32, iso, Gauge32, ModuleIdentity, enterprises, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "IpAddress", "Bits", "NotificationType", "ObjectIdentity", "TimeTicks", "Integer32", "iso", "Gauge32", "ModuleIdentity", "enterprises", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rittal = ModuleIdentity((1, 3, 6, 1, 4, 1, 2606))
rittal.setRevisions(('2011-04-01 00:00',))
if mibBuilder.loadTexts: rittal.setLastUpdated('201104010000Z')
if mibBuilder.loadTexts: rittal.setOrganization('RITTAL GmbH & Co. KG')
mibBuilder.exportSymbols("RITTAL-SMI-MIB", rittal=rittal, PYSNMP_MODULE_ID=rittal)
