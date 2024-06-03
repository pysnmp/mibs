#
# PySNMP MIB module SIAE-TREE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-TREE-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 13:13:22 2024
# On host fv-az883-299 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Integer32, iso, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, enterprises, Counter64, Counter32, ObjectIdentity, MibIdentifier, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Integer32", "iso", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "enterprises", "Counter64", "Counter32", "ObjectIdentity", "MibIdentifier", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
siaeMicroelettronicaSpa = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373))
siaeMicroelettronicaSpa.setRevisions(('2014-06-23 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: siaeMicroelettronicaSpa.setLastUpdated('201406230000Z')
if mibBuilder.loadTexts: siaeMicroelettronicaSpa.setOrganization('SIAE MICROELETTRONICA spa')
siaeMib = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103))
mibBuilder.exportSymbols("SIAE-TREE-MIB", siaeMicroelettronicaSpa=siaeMicroelettronicaSpa, siaeMib=siaeMib, PYSNMP_MODULE_ID=siaeMicroelettronicaSpa)
