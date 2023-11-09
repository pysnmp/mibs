#
# PySNMP MIB module GARDEROS-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/garderos/GARDEROS-SMI-MIB
# Produced by pysmi-1.1.10 at Thu Nov  9 13:47:38 2023
# On host fv-az564-151 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, ModuleIdentity, Counter32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, NotificationType, Integer32, IpAddress, Counter64, Bits, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ModuleIdentity", "Counter32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "NotificationType", "Integer32", "IpAddress", "Counter64", "Bits", "Gauge32", "MibIdentifier")
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
