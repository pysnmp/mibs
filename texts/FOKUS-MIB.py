#
# PySNMP MIB module FOKUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/FOKUS-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 12:00:26 2024
# On host fv-az1530-743 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Gauge32, TimeTicks, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Unsigned32, enterprises, Bits, ObjectIdentity, iso, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "TimeTicks", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Unsigned32", "enterprises", "Bits", "ObjectIdentity", "iso", "Integer32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fokus = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325))
if mibBuilder.loadTexts: fokus.setLastUpdated('200202050000Z')
if mibBuilder.loadTexts: fokus.setOrganization('Fraunhofer FOKUS, CATS')
if mibBuilder.loadTexts: fokus.setContactInfo('\t\tHartmut Brandt\n\n\t     Postal:\tFraunhofer Institute for Open Communication Systems\n\t\t\tKaiserin-Augusta-Allee 31\n\t\t\t10589 Berlin\n\t\t\tGermany\n\n\t     Fax:\t+49 30 3463 7352\n\n\t     E-mail:\tharti@freebsd.org')
if mibBuilder.loadTexts: fokus.setDescription('The root of the Fokus enterprises tree.')
mibBuilder.exportSymbols("FOKUS-MIB", PYSNMP_MODULE_ID=fokus, fokus=fokus)
