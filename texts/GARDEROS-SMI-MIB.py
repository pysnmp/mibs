#
# PySNMP MIB module GARDEROS-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/garderos/GARDEROS-SMI-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 11:55:38 2024
# On host fv-az665-602 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, TimeTicks, Counter32, Integer32, iso, Bits, Gauge32, Unsigned32, MibIdentifier, ModuleIdentity, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "TimeTicks", "Counter32", "Integer32", "iso", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "NotificationType", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
garderos = ModuleIdentity((1, 3, 6, 1, 4, 1, 16108))
garderos.setRevisions(('2016-02-02 16:12',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: garderos.setRevisionsDescriptions(('Redesign',))
if mibBuilder.loadTexts: garderos.setLastUpdated('201602021612Z')
if mibBuilder.loadTexts: garderos.setOrganization('Garderos GmbH')
if mibBuilder.loadTexts: garderos.setContactInfo('Garderos GmbH\n                Balanstr. 55, D-81541 Muenchen, Germany\n                Tel. +49 (0)89/189 306-0, Fax +49 (0)89/189 306-98\n                http://www.garderos.com\n                Sitz und Registergericht Muenchen. Geschaeftsfuehrer: Hermann Knauer, Dr. Walter Hinder.\n                HRB 141001')
if mibBuilder.loadTexts: garderos.setDescription('Garderos SMI definition.')
mibBuilder.exportSymbols("GARDEROS-SMI-MIB", PYSNMP_MODULE_ID=garderos, garderos=garderos)
