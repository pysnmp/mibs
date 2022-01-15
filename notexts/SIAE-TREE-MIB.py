#
# PySNMP MIB module SIAE-TREE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-TREE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:28:51 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, ModuleIdentity, ObjectIdentity, Integer32, Gauge32, Bits, NotificationType, IpAddress, Unsigned32, MibIdentifier, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Integer32", "Gauge32", "Bits", "NotificationType", "IpAddress", "Unsigned32", "MibIdentifier", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
siaeMicroelettronicaSpa = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373))
siaeMicroelettronicaSpa.setRevisions(('2014-06-23 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: siaeMicroelettronicaSpa.setLastUpdated('201406230000Z')
if mibBuilder.loadTexts: siaeMicroelettronicaSpa.setOrganization('SIAE MICROELETTRONICA spa')
siaeMib = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103))
mibBuilder.exportSymbols("SIAE-TREE-MIB", siaeMib=siaeMib, PYSNMP_MODULE_ID=siaeMicroelettronicaSpa, siaeMicroelettronicaSpa=siaeMicroelettronicaSpa)
