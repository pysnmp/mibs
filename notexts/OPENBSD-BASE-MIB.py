#
# PySNMP MIB module OPENBSD-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-BASE-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 13:32:33 2024
# On host fv-az883-167 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
enterprises, Counter64, NotificationType, iso, Unsigned32, TimeTicks, ModuleIdentity, Bits, Gauge32, IpAddress, ObjectIdentity, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter64", "NotificationType", "iso", "Unsigned32", "TimeTicks", "ModuleIdentity", "Bits", "Gauge32", "IpAddress", "ObjectIdentity", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
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
mibBuilder.exportSymbols("OPENBSD-BASE-MIB", localSystem=localSystem, memMIBObjects=memMIBObjects, pfMIBObjects=pfMIBObjects, sensorsMIBObjects=sensorsMIBObjects, openBSD=openBSD, openBSDDefaultObjectID=openBSDDefaultObjectID, carpMIBObjects=carpMIBObjects, PYSNMP_MODULE_ID=openBSD, localTest=localTest, relaydMIBObjects=relaydMIBObjects)
