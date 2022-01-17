#
# PySNMP MIB module OPENBSD-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-BASE-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 17:59:48 2022
# On host fv-az74-933 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, NotificationType, Bits, Counter32, Gauge32, MibIdentifier, Unsigned32, Integer32, iso, TimeTicks, enterprises, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "NotificationType", "Bits", "Counter32", "Gauge32", "MibIdentifier", "Unsigned32", "Integer32", "iso", "TimeTicks", "enterprises", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
openBSD = ModuleIdentity((1, 3, 6, 1, 4, 1, 30155))
openBSD.setRevisions(('2012-01-31 00:00', '2008-12-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: openBSD.setRevisionsDescriptions(("Document relayd(8)'s use of the openBSD.3 OID; move the CARP MIB to\n            openBSD.6 to avoid a conflict with relayd.", 'Updated for MIB for the OpenBSD snmpd(8) implementation.',))
if mibBuilder.loadTexts: openBSD.setLastUpdated('201201310000Z')
if mibBuilder.loadTexts: openBSD.setOrganization('OpenBSD')
if mibBuilder.loadTexts: openBSD.setContactInfo('Editor:    Reyk Floeter\n\t    EMail:      reyk@openbsd.org\n\t    WWW:        http://www.openbsd.org/\n\n\t    Editor:     Joel Knight\n\t    EMail:      knight.joel@gmail.com\n\t    WWW:        http://www.packetmischief.ca/openbsd-snmp-mibs/')
if mibBuilder.loadTexts: openBSD.setDescription('The base MIB module for the OpenBSD project.')
pfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 1))
sensorsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 2))
relaydMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 3))
memMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 5))
carpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 6))
localSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 23))
openBSDDefaultObjectID = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 23, 1))
localTest = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 42))
mibBuilder.exportSymbols("OPENBSD-BASE-MIB", localTest=localTest, carpMIBObjects=carpMIBObjects, PYSNMP_MODULE_ID=openBSD, pfMIBObjects=pfMIBObjects, localSystem=localSystem, openBSDDefaultObjectID=openBSDDefaultObjectID, memMIBObjects=memMIBObjects, relaydMIBObjects=relaydMIBObjects, openBSD=openBSD, sensorsMIBObjects=sensorsMIBObjects)
