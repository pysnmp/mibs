#
# PySNMP MIB module SIAE-TREE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-TREE-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 10:10:20 2024
# On host fv-az1771-969 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, iso, Counter32, IpAddress, enterprises, Gauge32, Integer32, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "iso", "Counter32", "IpAddress", "enterprises", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
siaeMicroelettronicaSpa = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373))
siaeMicroelettronicaSpa.setRevisions(('2014-06-23 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: siaeMicroelettronicaSpa.setRevisionsDescriptions(('Changed the module name from smTreeMib to siaeMicroelettronicaSpa\n             Renoved the definition of siaeMicroelettronicaSpa object identifier\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: siaeMicroelettronicaSpa.setLastUpdated('201406230000Z')
if mibBuilder.loadTexts: siaeMicroelettronicaSpa.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: siaeMicroelettronicaSpa.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: siaeMicroelettronicaSpa.setDescription('SIAE MIB tree root\n            ')
siaeMib = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103))
mibBuilder.exportSymbols("SIAE-TREE-MIB", siaeMicroelettronicaSpa=siaeMicroelettronicaSpa, siaeMib=siaeMib, PYSNMP_MODULE_ID=siaeMicroelettronicaSpa)
