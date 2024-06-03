#
# PySNMP MIB module FREEBSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/FREEBSD-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 03:07:50 2024
# On host fv-az736-440 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, iso, NotificationType, IpAddress, Bits, Counter64, MibIdentifier, Integer32, ObjectIdentity, enterprises, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "iso", "NotificationType", "IpAddress", "Bits", "Counter64", "MibIdentifier", "Integer32", "ObjectIdentity", "enterprises", "Gauge32")
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
mibBuilder.exportSymbols("FREEBSD-MIB", freeBSDsrc=freeBSDsrc, freeBSDpeoplePhk=freeBSDpeoplePhk, PYSNMP_MODULE_ID=freeBSD, freeBSDVersion=freeBSDVersion, freeBSDpeople=freeBSDpeople, freeBSD=freeBSD, freeBSDports=freeBSDports)
