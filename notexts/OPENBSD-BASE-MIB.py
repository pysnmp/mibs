#
# PySNMP MIB module OPENBSD-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-BASE-MIB
# Produced by pysmi-1.1.12 at Wed May 29 06:49:02 2024
# On host fv-az1019-850 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, Unsigned32, Counter32, MibIdentifier, NotificationType, enterprises, TimeTicks, Bits, Gauge32, Counter64, Integer32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Counter32", "MibIdentifier", "NotificationType", "enterprises", "TimeTicks", "Bits", "Gauge32", "Counter64", "Integer32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
mibBuilder.exportSymbols("OPENBSD-BASE-MIB", memMIBObjects=memMIBObjects, sensorsMIBObjects=sensorsMIBObjects, localSystem=localSystem, PYSNMP_MODULE_ID=openBSD, pfMIBObjects=pfMIBObjects, carpMIBObjects=carpMIBObjects, openBSD=openBSD, localTest=localTest, relaydMIBObjects=relaydMIBObjects, openBSDDefaultObjectID=openBSDDefaultObjectID)
