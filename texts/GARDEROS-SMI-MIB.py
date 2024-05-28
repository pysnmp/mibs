#
# PySNMP MIB module GARDEROS-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/garderos/GARDEROS-SMI-MIB
# Produced by pysmi-1.1.12 at Tue May 28 13:58:56 2024
# On host fv-az529-55 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, Counter32, iso, Counter64, NotificationType, IpAddress, TimeTicks, enterprises, MibIdentifier, ModuleIdentity, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "Counter32", "iso", "Counter64", "NotificationType", "IpAddress", "TimeTicks", "enterprises", "MibIdentifier", "ModuleIdentity", "Bits", "Gauge32")
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
