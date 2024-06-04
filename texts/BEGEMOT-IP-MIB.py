#
# PySNMP MIB module BEGEMOT-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-IP-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 07:53:20 2024
# On host fv-az837-21 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, Counter64, IpAddress, ObjectIdentity, NotificationType, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, Unsigned32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "Counter64", "IpAddress", "ObjectIdentity", "NotificationType", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "Unsigned32", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
begemotIp = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 3))
if mibBuilder.loadTexts: begemotIp.setLastUpdated('200602130000Z')
if mibBuilder.loadTexts: begemotIp.setOrganization('German Aerospace Center')
if mibBuilder.loadTexts: begemotIp.setContactInfo('\t\tHartmut Brandt\n\n\t     Postal:\tGerman Aerospace Center\n\t\t\tOberpfaffenhofen\n\t\t\t82234 Wessling\n\t\t\tGermany\n\n\t     Fax:\t+49 8153 28 2843\n\n\t     E-mail:\tharti@freebsd.org')
if mibBuilder.loadTexts: begemotIp.setDescription('The MIB for IP stuff that is not in the official IP MIBs.')
begemotIpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1))
mibBuilder.exportSymbols("BEGEMOT-IP-MIB", PYSNMP_MODULE_ID=begemotIp, begemotIp=begemotIp, begemotIpObjects=begemotIpObjects)
