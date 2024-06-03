#
# PySNMP MIB module RITTAL-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rittal/RITTAL-SMI
# Produced by pysmi-1.1.12 at Mon Jun  3 11:01:49 2024
# On host fv-az1986-135 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, enterprises, TimeTicks, Integer32, ModuleIdentity, ObjectIdentity, MibIdentifier, iso, Counter32, Gauge32, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "enterprises", "TimeTicks", "Integer32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "iso", "Counter32", "Gauge32", "Counter64", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rittal = ModuleIdentity((1, 3, 6, 1, 4, 1, 2606))
rittal.setRevisions(('2011-04-01 00:00',))
if mibBuilder.loadTexts: rittal.setLastUpdated('201104010000Z')
if mibBuilder.loadTexts: rittal.setOrganization('RITTAL GmbH & Co. KG')
mibBuilder.exportSymbols("RITTAL-SMI-MIB", PYSNMP_MODULE_ID=rittal, rittal=rittal)
