#
# PySNMP MIB module FOKUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/FOKUS-MIB
# Produced by pysmi-1.1.8 at Thu Dec 15 08:32:42 2022
# On host fv-az193-683 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, ModuleIdentity, ObjectIdentity, enterprises, IpAddress, Integer32, Bits, TimeTicks, NotificationType, Counter64, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "ModuleIdentity", "ObjectIdentity", "enterprises", "IpAddress", "Integer32", "Bits", "TimeTicks", "NotificationType", "Counter64", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fokus = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325))
if mibBuilder.loadTexts: fokus.setLastUpdated('200202050000Z')
if mibBuilder.loadTexts: fokus.setOrganization('Fraunhofer FOKUS, CATS')
if mibBuilder.loadTexts: fokus.setContactInfo('\t\tHartmut Brandt\n\n\t     Postal:\tFraunhofer Institute for Open Communication Systems\n\t\t\tKaiserin-Augusta-Allee 31\n\t\t\t10589 Berlin\n\t\t\tGermany\n\n\t     Fax:\t+49 30 3463 7352\n\n\t     E-mail:\tharti@freebsd.org')
if mibBuilder.loadTexts: fokus.setDescription('The root of the Fokus enterprises tree.')
mibBuilder.exportSymbols("FOKUS-MIB", fokus=fokus, PYSNMP_MODULE_ID=fokus)
