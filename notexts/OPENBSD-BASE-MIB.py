#
# PySNMP MIB module OPENBSD-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-BASE-MIB
# Produced by pysmi-1.1.8 at Thu Jan  5 11:35:03 2023
# On host fv-az280-773 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, NotificationType, enterprises, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, IpAddress, Integer32, ObjectIdentity, ModuleIdentity, Counter32, MibIdentifier, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "enterprises", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "IpAddress", "Integer32", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibIdentifier", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("OPENBSD-BASE-MIB", openBSDDefaultObjectID=openBSDDefaultObjectID, relaydMIBObjects=relaydMIBObjects, localTest=localTest, carpMIBObjects=carpMIBObjects, pfMIBObjects=pfMIBObjects, sensorsMIBObjects=sensorsMIBObjects, PYSNMP_MODULE_ID=openBSD, openBSD=openBSD, memMIBObjects=memMIBObjects, localSystem=localSystem)
