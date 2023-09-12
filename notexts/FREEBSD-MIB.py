#
# PySNMP MIB module FREEBSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/FREEBSD-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 08:12:07 2023
# On host fv-az447-19 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter64, Integer32, Counter32, ObjectIdentity, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, TimeTicks, MibIdentifier, IpAddress, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "Integer32", "Counter32", "ObjectIdentity", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "TimeTicks", "MibIdentifier", "IpAddress", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
freeBSD = ModuleIdentity((1, 3, 6, 1, 4, 1, 2238))
freeBSD.setRevisions(('2006-10-31 08:00',))
if mibBuilder.loadTexts: freeBSD.setLastUpdated('200610311000Z')
if mibBuilder.loadTexts: freeBSD.setOrganization('The FreeBSD Project.')
freeBSDsrc = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 1))
if mibBuilder.loadTexts: freeBSDsrc.setStatus('current')
freeBSDports = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 2))
if mibBuilder.loadTexts: freeBSDports.setStatus('current')
freeBSDpeople = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 3))
if mibBuilder.loadTexts: freeBSDpeople.setStatus('current')
freeBSDpeoplePhk = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 3, 1))
if mibBuilder.loadTexts: freeBSDpeoplePhk.setStatus('current')
freeBSDVersion = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 4))
if mibBuilder.loadTexts: freeBSDVersion.setStatus('current')
mibBuilder.exportSymbols("FREEBSD-MIB", freeBSD=freeBSD, freeBSDsrc=freeBSDsrc, PYSNMP_MODULE_ID=freeBSD, freeBSDVersion=freeBSDVersion, freeBSDpeoplePhk=freeBSDpeoplePhk, freeBSDpeople=freeBSDpeople, freeBSDports=freeBSDports)
