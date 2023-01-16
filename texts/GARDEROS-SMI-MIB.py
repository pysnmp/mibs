#
# PySNMP MIB module GARDEROS-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/garderos/GARDEROS-SMI-MIB
# Produced by pysmi-1.1.8 at Mon Jan 16 15:05:22 2023
# On host fv-az587-63 platform Linux version 5.15.0-1030-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, iso, Counter64, MibIdentifier, TimeTicks, NotificationType, Bits, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, IpAddress, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "iso", "Counter64", "MibIdentifier", "TimeTicks", "NotificationType", "Bits", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "IpAddress", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
garderos = ModuleIdentity((1, 3, 6, 1, 4, 1, 16108))
garderos.setRevisions(('2016-02-02 16:12',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: garderos.setRevisionsDescriptions(('Redesign',))
if mibBuilder.loadTexts: garderos.setLastUpdated('201602021612Z')
if mibBuilder.loadTexts: garderos.setOrganization('Garderos GmbH')
if mibBuilder.loadTexts: garderos.setContactInfo('Garderos GmbH\n                Balanstr. 55, D-81541 Muenchen, Germany\n                Tel. +49 (0)89/189 306-0, Fax +49 (0)89/189 306-98\n                http://www.garderos.com\n                Sitz und Registergericht Muenchen. Geschaeftsfuehrer: Hermann Knauer, Dr. Walter Hinder.\n                HRB 141001')
if mibBuilder.loadTexts: garderos.setDescription('Garderos SMI definition.')
mibBuilder.exportSymbols("GARDEROS-SMI-MIB", garderos=garderos, PYSNMP_MODULE_ID=garderos)
