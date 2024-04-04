#
# PySNMP MIB module FOKUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/FOKUS-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 13:42:16 2024
# On host fv-az984-576 platform Linux version 6.5.0-1017-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, Integer32, MibIdentifier, Bits, iso, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, IpAddress, NotificationType, Unsigned32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Integer32", "MibIdentifier", "Bits", "iso", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "IpAddress", "NotificationType", "Unsigned32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fokus = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325))
if mibBuilder.loadTexts: fokus.setLastUpdated('200202050000Z')
if mibBuilder.loadTexts: fokus.setOrganization('Fraunhofer FOKUS, CATS')
if mibBuilder.loadTexts: fokus.setContactInfo('\t\tHartmut Brandt\n\n\t     Postal:\tFraunhofer Institute for Open Communication Systems\n\t\t\tKaiserin-Augusta-Allee 31\n\t\t\t10589 Berlin\n\t\t\tGermany\n\n\t     Fax:\t+49 30 3463 7352\n\n\t     E-mail:\tharti@freebsd.org')
if mibBuilder.loadTexts: fokus.setDescription('The root of the Fokus enterprises tree.')
mibBuilder.exportSymbols("FOKUS-MIB", fokus=fokus, PYSNMP_MODULE_ID=fokus)
