#
# PySNMP MIB module BEGEMOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-MIB
# Produced by pysmi-1.1.8 at Fri Jan 27 14:03:34 2023
# On host fv-az401-610 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
fokus, = mibBuilder.importSymbols("FOKUS-MIB", "fokus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ObjectIdentity, IpAddress, Gauge32, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, NotificationType, TimeTicks, Counter32, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "IpAddress", "Gauge32", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "NotificationType", "TimeTicks", "Counter32", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
begemot = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1))
if mibBuilder.loadTexts: begemot.setLastUpdated('200201300000Z')
if mibBuilder.loadTexts: begemot.setOrganization('Fraunhofer FOKUS, CATS')
if mibBuilder.loadTexts: begemot.setContactInfo('\t\tHartmut Brandt\n\n\t     Postal:\tFraunhofer Institute for Open Communication Systems\n\t\t\tKaiserin-Augusta-Allee 31\n\t\t\t10589 Berlin\n\t\t\tGermany\n\n\t     Fax:\t+49 30 3463 7352\n\n\t     E-mail:\tharti@freebsd.org')
if mibBuilder.loadTexts: begemot.setDescription('The root of the Begemot subtree of the fokus tree.')
mibBuilder.exportSymbols("BEGEMOT-MIB", begemot=begemot, PYSNMP_MODULE_ID=begemot)
