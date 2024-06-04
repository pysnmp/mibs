#
# PySNMP MIB module OPENBSD-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-BASE-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 12:24:31 2024
# On host fv-az1789-327 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Integer32, ModuleIdentity, Counter32, NotificationType, Counter64, ObjectIdentity, IpAddress, TimeTicks, MibIdentifier, Bits, Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "ModuleIdentity", "Counter32", "NotificationType", "Counter64", "ObjectIdentity", "IpAddress", "TimeTicks", "MibIdentifier", "Bits", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
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
mibBuilder.exportSymbols("OPENBSD-BASE-MIB", sensorsMIBObjects=sensorsMIBObjects, openBSDDefaultObjectID=openBSDDefaultObjectID, PYSNMP_MODULE_ID=openBSD, memMIBObjects=memMIBObjects, pfMIBObjects=pfMIBObjects, localSystem=localSystem, carpMIBObjects=carpMIBObjects, openBSD=openBSD, localTest=localTest, relaydMIBObjects=relaydMIBObjects)
