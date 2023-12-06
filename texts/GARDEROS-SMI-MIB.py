#
# PySNMP MIB module GARDEROS-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/garderos/GARDEROS-SMI-MIB
# Produced by pysmi-1.1.11 at Wed Dec  6 03:01:42 2023
# On host fv-az520-882 platform Linux version 6.2.0-1016-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, Counter32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, IpAddress, Counter64, Bits, Unsigned32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Counter32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "IpAddress", "Counter64", "Bits", "Unsigned32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
garderos = ModuleIdentity((1, 3, 6, 1, 4, 1, 16108))
garderos.setRevisions(('2016-02-02 16:12',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: garderos.setRevisionsDescriptions(('Redesign',))
if mibBuilder.loadTexts: garderos.setLastUpdated('201602021612Z')
if mibBuilder.loadTexts: garderos.setOrganization('Garderos GmbH')
if mibBuilder.loadTexts: garderos.setContactInfo('Garderos GmbH\n                Balanstr. 55, D-81541 Muenchen, Germany\n                Tel. +49 (0)89/189 306-0, Fax +49 (0)89/189 306-98\n                http://www.garderos.com\n                Sitz und Registergericht Muenchen. Geschaeftsfuehrer: Hermann Knauer, Dr. Walter Hinder.\n                HRB 141001')
if mibBuilder.loadTexts: garderos.setDescription('Garderos SMI definition.')
mibBuilder.exportSymbols("GARDEROS-SMI-MIB", PYSNMP_MODULE_ID=garderos, garderos=garderos)
