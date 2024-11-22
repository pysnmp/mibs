#
# PySNMP MIB module FREEBSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/FREEBSD-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 11:59:18 2024
# On host fv-az665-602 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, NotificationType, ObjectIdentity, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, ModuleIdentity, Counter32, iso, MibIdentifier, Integer32, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "ObjectIdentity", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "ModuleIdentity", "Counter32", "iso", "MibIdentifier", "Integer32", "TimeTicks", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FREEBSD-MIB", PYSNMP_MODULE_ID=freeBSD, freeBSDVersion=freeBSDVersion, freeBSDpeoplePhk=freeBSDpeoplePhk, freeBSD=freeBSD, freeBSDpeople=freeBSDpeople, freeBSDports=freeBSDports, freeBSDsrc=freeBSDsrc)
