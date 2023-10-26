#
# PySNMP MIB module OPENBSD-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-BASE-MIB
# Produced by pysmi-1.1.10 at Thu Oct 26 12:35:20 2023
# On host fv-az583-292 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, MibIdentifier, IpAddress, NotificationType, Integer32, Unsigned32, TimeTicks, Counter32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Gauge32, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "IpAddress", "NotificationType", "Integer32", "Unsigned32", "TimeTicks", "Counter32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Gauge32", "Counter64", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
openBSD = ModuleIdentity((1, 3, 6, 1, 4, 1, 30155))
openBSD.setRevisions(('2012-01-31 00:00', '2008-12-23 00:00',))
if mibBuilder.loadTexts: openBSD.setLastUpdated('201201310000Z')
if mibBuilder.loadTexts: openBSD.setOrganization('OpenBSD')
pfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 1))
sensorsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 2))
relaydMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 3))
memMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 5))
carpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 6))
localSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 23))
openBSDDefaultObjectID = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 23, 1))
localTest = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 42))
mibBuilder.exportSymbols("OPENBSD-BASE-MIB", PYSNMP_MODULE_ID=openBSD, openBSD=openBSD, relaydMIBObjects=relaydMIBObjects, memMIBObjects=memMIBObjects, carpMIBObjects=carpMIBObjects, localTest=localTest, pfMIBObjects=pfMIBObjects, sensorsMIBObjects=sensorsMIBObjects, openBSDDefaultObjectID=openBSDDefaultObjectID, localSystem=localSystem)
