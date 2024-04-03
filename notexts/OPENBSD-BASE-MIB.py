#
# PySNMP MIB module OPENBSD-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-BASE-MIB
# Produced by pysmi-1.1.11 at Wed Apr  3 14:02:20 2024
# On host fv-az1200-481 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, iso, Gauge32, Counter32, ObjectIdentity, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Integer32, IpAddress, MibIdentifier, Counter64, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Gauge32", "Counter32", "ObjectIdentity", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Integer32", "IpAddress", "MibIdentifier", "Counter64", "enterprises")
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
mibBuilder.exportSymbols("OPENBSD-BASE-MIB", localTest=localTest, openBSD=openBSD, relaydMIBObjects=relaydMIBObjects, PYSNMP_MODULE_ID=openBSD, carpMIBObjects=carpMIBObjects, memMIBObjects=memMIBObjects, localSystem=localSystem, openBSDDefaultObjectID=openBSDDefaultObjectID, sensorsMIBObjects=sensorsMIBObjects, pfMIBObjects=pfMIBObjects)
